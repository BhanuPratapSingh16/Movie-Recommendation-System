from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"

data_df = pd.read_csv(PROCESSED_DATA_DIR / "ratings.csv")

def get_user_history(user_id):
    '''
        Returns the movies rated by user along with the ratings
    '''
    if(user_id > 943):
        return []
    return data_df[data_df["user_id"] == user_id][["movie_id", "rating"]].sort_values("rating", ascending=False).values.tolist()