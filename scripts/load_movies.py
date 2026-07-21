import pandas as pd
from pymongo import MongoClient
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]
MOVIES_PATH = BASE_DIR / "dataset" / "processed" / "movies.csv"

MONGO_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGO_URI)

db = client["moviesdb"]
movies_collection = db["movies"]

movies_df = pd.read_csv(MOVIES_PATH)

genres = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]

movies = []

for _, row in movies_df.iterrows():

    movie_genres = [genre for genre in genres if row[genre] == 1]

    movie = {
        "_id": int(row["movie_id"]),
        "title": row["title"],
        "genres": movie_genres
    }

    movies.append(movie)

movies_collection.insert_many(movies)

print(f"Inserted {len(movies)} movies.")