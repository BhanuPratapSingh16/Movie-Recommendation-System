from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"

class ContentBasedRecommender:
    def __init__(self, similarity_df):
        self.similarity_df = similarity_df

    def recommendByMovie(self, movie_id, top_n=50):
        scores = self.similarity_df.loc[movie_id].sort_values(ascending=False).head(top_n+1)
        return scores[1:]

    def recommend(self, watched_movies, top_n=100):
        # Store movies and their scores
        movie_scores = {}
        watched_movie_ids = set([movie[0] for movie in watched_movies])
        
        # Iterate and get recommendations considering all the movies user watched
        for movie_id, rating in watched_movies:
            movie_recoms = self.recommendByMovie(movie_id)
            movie_recoms *= rating / 5   # Normalize the score

            # Update the score
            for recom_movie_id, recom_movie_score in movie_recoms.items():
                if recom_movie_id not in watched_movie_ids:
                    movie_scores[recom_movie_id] = movie_scores.get(recom_movie_id, 0) + recom_movie_score
        
        # Return the top n best movies
        return dict(sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)[:top_n])
