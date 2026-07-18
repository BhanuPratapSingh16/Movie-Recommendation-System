from pathlib import Path
import pandas as pd
from ml_service.services.user_history_service import get_user_history
from ml_service.recommenders.popularity_recommender import PopularityRecommender
from ml_service.recommenders.content_based_recommender import ContentBasedRecommender
from ml_service.recommenders.collaborative_recommender import CollaborativeRecommender
from ml_service.recommenders.hybrid_recommender import HybridRecommender
from ml_service.preprocessing.feature_engineering import build_popularity_table


# Global variables
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"
MOVIES_DF = pd.read_csv(PROCESSED_DATA_DIR / "movies.csv")
POPULARITY_TABLE = build_popularity_table()
SIMILARITY_MATRIX = pd.read_pickle(PROCESSED_DATA_DIR / "cosine_similarity.pkl")

class RecommendationEngine:
    def __init__(self):
        self.popularity_recommender = PopularityRecommender(POPULARITY_TABLE)
        self.content_recommender = ContentBasedRecommender(SIMILARITY_MATRIX)
        self.collaborative_recommender = CollaborativeRecommender(943, 1682)
        self.hybrid_recommender = HybridRecommender(self.popularity_recommender, self.content_recommender, self.collaborative_recommender)
    
    def recommend(self, user_id):
        # Get user watch history
        watch_history = get_user_history(user_id=user_id)

        # Generate the recommendations
        recommendation =  self.hybrid_recommender.recommend(user_id, watch_history)

        # Format and return the recommendations
        return recommendation
