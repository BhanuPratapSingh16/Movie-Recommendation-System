from pathlib import Path
import pandas as pd
from ml_service.services.user_history_service import get_user_history
from ml_service.recommenders.popularity_recommender import PopularityRecommender
from ml_service.recommenders.content_based_recommender import ContentBasedRecommender
from ml_service.recommenders.collaborative_recommender import CollaborativeRecommender
from ml_service.preprocessing.feature_engineering import build_popularity_table


BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"
movies_df = pd.read_csv(PROCESSED_DATA_DIR / "movies.csv")

class HybridRecommender:
    def __init__(self, popularity_recommender, content_recommender, collaborative_recommender):
        self.popularity_recommender = popularity_recommender
        self.content_recommender = content_recommender
        self.collaborative_recommender = collaborative_recommender
    
    def recommend(self, user_id, top_n=10):
        user_history = get_user_history(user_id=user_id)
        print(len(user_history))
        if(len(user_history) == 0):
            return self.popularity_recommender.recommend()
        elif(len(user_history) < 10):
            return self.content_recommender.recommend(user_history)
        else:
            return self.collaborative_recommender.recommend(user_id, user_history)
