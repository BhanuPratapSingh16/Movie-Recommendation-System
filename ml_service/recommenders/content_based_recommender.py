from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"

class ContentBasedRecommender:
    def __init__(self, similarity_df):
        self.similarity_df = similarity_df

    def recommend(self, movie_id, top_n=10):
        scores = self.similarity_df.loc[movie_id].sort_values(ascending=False).head(top_n+1)
        return scores[1:]

