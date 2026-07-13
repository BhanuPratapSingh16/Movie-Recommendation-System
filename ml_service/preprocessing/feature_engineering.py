from pathlib import Path
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"

def load_data():
    '''
        Loads and returns the dataset
    '''
    dataset_df = pd.read_csv(PROCESSED_DATA_DIR / "movies_dataset.csv")
    movies_df = pd.read_csv(PROCESSED_DATA_DIR / "movies.csv")
    return dataset_df, movies_df

def build_popularity_table(minimum_votes=50):
    '''
        Computes the average rating, number of ratings and weighted average rating of all movies

        Parameters:
        minimum_votes - Parameter to calculate weighted average rating
    '''

    # Load the data
    dataset_df, movies_df = load_data()
    
    movie_stats = dataset_df.groupby("movie_id")["rating"].agg(
        average_rating = "mean",
        number_of_ratings = "count"
    )
    
    # Parameters to calculate weighted average rating
    C = movie_stats["average_rating"].mean()
    vote_denom = (movie_stats["number_of_ratings"] + minimum_votes)

    movie_stats["weighted_rating"] = (
        (movie_stats["number_of_ratings"] / vote_denom) * movie_stats["average_rating"] 
        +
        (minimum_votes / vote_denom) * C
    )

    # Sort by weighted average rating
    movie_stats = movie_stats.sort_values(
        by = "weighted_rating",
        ascending = False
    )

    # Add the title to the stats
    movie_stats = movie_stats.merge(movies_df[["movie_id", "title"]], on = "movie_id")

    return movie_stats



def build_similarity_matrix():
    '''
        Computes the cosine similarity score of the movies
    '''

    # Load the data
    _, movies_df = load_data()

    genres = ["unknown", "Action", "Adventure", "Animation",
            "Children", "Comedy", "Crime", "Documentary", "Drama",
            "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
            "Romance", "Sci-Fi", "Thriller", "War", "Western"
            ]
    
    movie_features = movies_df[genres]

    similarity = cosine_similarity(movie_features)

    similarity_df = pd.DataFrame(
        similarity,
        index = movies_df["movie_id"],
        columns = movies_df["movie_id"]
    )

    similarity_df.to_pickle(PROCESSED_DATA_DIR / "cosine_similarity.pkl")
