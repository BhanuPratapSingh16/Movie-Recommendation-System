import numpy as np
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


# Global variables
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_DIR = BASE_DIR / "dataset" / "processed"
MODEL_DIR = BASE_DIR / "ml_service" / "saved_models"

# Load the dataframe and split into training and testing set
data_df = pd.read_csv(PROCESSED_DATA_DIR / "ratings.csv").drop(columns=["timestamp"])
train_df, test_df = train_test_split(data_df, test_size=0.2, random_state=42)
movies = pd.read_csv(PROCESSED_DATA_DIR / "movies.csv")["movie_id"]


# Convert to numpy array for faster calculations
train_data = train_df.to_numpy()
test_data = test_df.to_numpy()


class CollaborativeRecommender:
    def __init__(self, num_users, num_movies, latent_factors=20):
        self.latent_factors = latent_factors
        self.P = np.random.normal(0, 0.01, (num_users, latent_factors))
        self.Q = np.random.normal(0, 0.01, (num_movies, latent_factors))

    def train(self, epochs, train_data, learning_rate=0.01, regularization=0.02):
        for epoch in range(epochs):
            total_loss = 0
            for user_id, movie_id, rating in train_data:
                user_vector = self.P[user_id-1].copy()
                movie_vector = self.Q[movie_id-1].copy()

                # Predict the rating
                prediction = np.dot(user_vector, movie_vector)

                # Calculate the loss
                error = rating - prediction
                loss = error ** 2
                total_loss += loss

                # Update the parameters
                self.P[user_id-1] += learning_rate * (error * movie_vector - regularization * user_vector)

                self.Q[movie_id-1] += learning_rate * (error * user_vector - regularization * movie_vector)

            average_loss = total_loss / len(train_data)
            print(f"Epoch : {epoch+1}, Loss : {average_loss}")
        

    def test(self, test_data):
        y_true = []
        y_predicted = []
        for user_id, movie_id, rating in test_data:
            # Predict the rating
            prediction = self.predict(user_id, movie_id)

            y_true.append(rating)
            y_predicted.append(prediction)

        rmse = np.sqrt(np.mean((np.array(y_true) - np.array(y_predicted)) ** 2))
        return rmse, y_true, y_predicted

    def loss_fn(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
    
    def predict(self, user_id, movie_id):
        user_vector = self.P[user_id-1].copy()
        movie_vector = self.Q[movie_id-1].copy()

        prediction = np.dot(user_vector, movie_vector)
        prediction = np.clip(prediction, 0, 5)
        
        return prediction

    def save_state(self):
        np.save(MODEL_DIR / "Collaborative_P.npy", self.P)
        np.save(MODEL_DIR / "Collaborative_Q.npy", self.Q)

    def load_state(self):
        self.P = np.load(MODEL_DIR / "Collaborative_P.npy")
        self.Q = np.load(MODEL_DIR / "Collaborative_Q.npy")

    def recommend(self, user_id, watch_history, top_n=100):
        self.load_state()
        movie_ids = [x[0] for x in watch_history]
        
        # Get the new user vector
        new_user_vector = np.random.normal(0, 0.01, self.latent_factors)
        
        lr = 0.01
        reg = 0.02

        for epoch in range(50):
            for movie_id, rating in watch_history:
                prediction = np.dot(new_user_vector, self.Q[movie_id-1])
                error = rating - prediction

                new_user_vector += lr * (error * self.Q[movie_id - 1] - reg * new_user_vector)
        
        # Predict top movies for the new user
        movie_scores = {}

        for movie_id in movies:
            if movie_id not in movie_ids:
                prediction = np.dot(new_user_vector, self.Q[movie_id-1])
                prediction = np.clip(prediction, 0, 5)
                movie_scores[movie_id] = prediction
        
        # Return the top n best movies
        return dict(sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)[:top_n])