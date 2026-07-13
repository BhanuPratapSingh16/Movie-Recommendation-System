from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = BASE_DIR / "dataset" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"

def prepare_dataset():
    '''
        Reads raw data and generates:
        - movies.csv
        - ratings.csv
        - users.csv
        - movies_dataset.csv
    '''

    # Load raw ratings data
    raw_ratings = pd.read_csv(RAW_DATA_DIR / "u.data",
                              sep = "\t",
                              names = ["user_id", "movie_id", "rating", "timestamp"])
    
    # Load raw movies data
    movie_columns = [
        "movie_id", "title", "release_date", "video_release_date",
        "imdb_url", "unknown", "Action", "Adventure", "Animation",
        "Children", "Comedy", "Crime", "Documentary", "Drama",
        "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
        "Romance", "Sci-Fi", "Thriller", "War", "Western"
    ]

    raw_movies = pd.read_csv(
        RAW_DATA_DIR / "u.item",
        sep="|",
        names=movie_columns,
        encoding="latin-1"
    )
    raw_movies = raw_movies.drop(columns=["video_release_date"]) # null column

    # Load raw users data
    raw_users = pd.read_csv(
        RAW_DATA_DIR / "u.user",
        sep="|",
        names=["user_id", "age", "gender", "occupation", "zip_code"]
    )

    # Merge the ratings with users
    movies_ratings_merged = raw_ratings.merge(raw_movies, on="movie_id")

    # Merge the above merged data with user
    merged_df = movies_ratings_merged.merge(raw_users, on="user_id")
    merged_df = merged_df.drop(columns=["timestamp", "occupation", "zip_code"]) # Remove unnecessary columns

    # Save the processed data as csv files
    raw_ratings.to_csv(PROCESSED_DATA_DIR / "ratings.csv", index=False)
    raw_movies.to_csv(PROCESSED_DATA_DIR / "movies.csv", index=False)
    raw_users.to_csv(PROCESSED_DATA_DIR / "users.csv", index=False)
    merged_df.to_csv(PROCESSED_DATA_DIR / "movies_dataset.csv", index=False)



if __name__ == '__main__':
    prepare_dataset()