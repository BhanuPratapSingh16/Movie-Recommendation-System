import pandas as pd
from pathlib import Path
from fastapi import FastAPI
from ml_service.recommenders.engine import RecommendationEngine

# Data directory
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"
MOVIES_DF = pd.read_csv(PROCESSED_DATA_DIR / "movies.csv").set_index("movie_id")

# Recommendation engine
recommender = RecommendationEngine()


app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Movie Recommendation API"}


@app.get("/recommend/{user_id}")
def recommend(user_id):
    recoms = recommender.recommend(int(user_id))
    recommendations = []

    for movie_id, score in recoms.items():
        recommendations.append({
            "movie_id": movie_id,
            "title": MOVIES_DF.loc[movie_id]["title"],
            "score": score
        })

    return {
        "recommendations": recommendations
    }