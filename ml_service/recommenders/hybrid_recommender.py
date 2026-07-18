from ml_service.utils.normalization import min_max_norm


# Constants
W_CONTENT_RECOM = {
    "w_pop":0.3,
    "w_con":0.7
}

W_HYBRID_RECOM = {
    "w_pop" : 0.1,
    "w_con":0.25,
    "w_collab": 0.65
}

class HybridRecommender:
    def __init__(self, popularity_recommender, content_recommender, collaborative_recommender):
        self.popularity_recommender = popularity_recommender
        self.content_recommender = content_recommender
        self.collaborative_recommender = collaborative_recommender
    
    def recommend(self, user_id, watch_history, top_n=10):
        num_watched_movies = len(watch_history)

        # Get popularity recommendation and normalize the score
        popularity_recom = self.popularity_recommender.recommend()
        popularity_recom = min_max_norm(popularity_recom)

        if(num_watched_movies == 0): # No watched movies -> return most popular movies
            return popularity_recom
        elif(num_watched_movies < 10):  # Few watched movies -> Start personalizing with content based
            content_recom = self.content_recommender.recommend(watch_history)
            # Normalize the score
            content_recom = min_max_norm(content_recom)

            # Add the scores of popularity and content Recommendations with weightage
            recom_movie_ids = popularity_recom.keys() | content_recom.keys()

            recoms = {}

            for movie_id in recom_movie_ids:
                recoms[movie_id] = W_CONTENT_RECOM["w_pop"] * popularity_recom.get(movie_id, 0) + W_CONTENT_RECOM["w_con"] * content_recom.get(movie_id, 0)

            return dict(sorted(recoms.items(), key=lambda x: x[1], reverse=True)[:top_n])
        else:  # Many watched movies -> hybrid with collabarotive
            content_recom = self.content_recommender.recommend(watch_history[:10]) # Limit content based to top rated movies
            collaborative_recom = self.collaborative_recommender.recommend(user_id, watch_history)
            print(sorted(collaborative_recom.items(), key=lambda x: x[1], reverse=True)[:10])

            # Normalize the scores
            content_recom = min_max_norm(content_recom)
            collaborative_recom = min_max_norm(collaborative_recom)

            # Add the scores of popularity, content and collaborative recommendations with weightage
            recom_movie_ids = popularity_recom.keys() | content_recom.keys() | collaborative_recom.keys()

            recoms = {}

            for movie_id in recom_movie_ids:
                recoms[movie_id] = [W_HYBRID_RECOM["w_pop"] * popularity_recom.get(movie_id, 0) + W_HYBRID_RECOM["w_con"] * content_recom.get(movie_id, 0) + W_HYBRID_RECOM["w_collab"] * collaborative_recom.get(movie_id, 0),  popularity_recom.get(movie_id, 0), content_recom.get(movie_id, 0), collaborative_recom.get(movie_id, 0)]
            return dict(sorted(recoms.items(), key=lambda x: x[1], reverse=True)[:top_n])
