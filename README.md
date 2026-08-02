# 🎬 Movie Recommendation System

A scalable movie recommendation system built with **Spring Boot**, **FastAPI**, and **Machine Learning**. The project combines secure REST APIs with a hybrid recommendation engine to provide personalized movie recommendations.

## Features

- User registration and authentication using JWT
- Access and refresh token support
- Secure REST APIs with Spring Security
- Movie rating management
- Personalized movie recommendations
- Hybrid recommendation engine
- Spring Boot ↔ FastAPI communication
- MongoDB for persistent storage

---

## Tech Stack

### Backend
- Java 21
- Spring Boot
- Spring Security
- Spring Data MongoDB
- JWT Authentication
- Maven

### Machine Learning Service
- FastAPI
- Python
- Pandas
- NumPy
- Scikit-learn

### Database
- MongoDB

---

## System Architecture

```
                +----------------------+
                |      REST Client     |
                | (Postman / Frontend) |
                +----------+-----------+
                           |
                           |
                    HTTP REST APIs
                           |
                           v
    +------------------------------------------------+
    |               Spring Boot Backend              |
    |------------------------------------------------|
    | Authentication                                 |
    | JWT Security                                   |
    | User Management                                |
    | Movie Ratings                                  |
    | Recommendation Service                         |
    +-----------------------+------------------------+
                        |
                        | REST
                        |
                        v
    +------------------------------------------------+
    |           FastAPI ML Recommendation Service    |
    |------------------------------------------------|
    | Popularity Recommender                         |
    | Content-Based Recommender                      |
    | Collaborative Filtering                        |
    | Hybrid Recommender                             |
    +-----------------------+------------------------+
                        |
                        |
                  MovieLens Dataset
```

---

## Recommendation Pipeline

1. User registers and logs in.
2. Spring Boot issues JWT access and refresh tokens.
3. User submits movie ratings.
4. Ratings are stored in MongoDB.
5. Spring Boot fetches the user's ratings.
6. Ratings are sent to the FastAPI ML service.
7. The hybrid recommendation engine generates recommendations.
8. Spring Boot returns the recommendations to the client.

---

## Hybrid Recommendation Strategy

The recommendation engine combines multiple approaches:

### Popularity-Based Filtering

Used for cold-start users with no rating history.

### Content-Based Filtering

Uses movie similarity to recommend movies related to those rated by the user.

### Collaborative Filtering

Matrix factorization based recommendation using latent factors.

### Hybrid Logic

- New users → Popularity recommendations
- Users with limited history → Popularity + Content-Based
- Users with sufficient history → Collaborative + Content-Based

---


## Security

- JWT Authentication
- Access Tokens
- Refresh Tokens
- BCrypt Password Encoding
- Stateless Authentication
- Spring Security Filter Chain

---

## Machine Learning

The recommendation engine includes:

- Popularity-Based Recommender
- Content-Based Filtering
- Collaborative Filtering (Matrix Factorization)
- Hybrid Recommendation Model

---

## Dataset

MovieLens dataset is used for training and evaluation.

Dataset includes:

- Movies
- Ratings
- Genres
- User interactions

---

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd movie-recommendation-system
```

### Start MongoDB

Ensure MongoDB is running.

### Configure Environment Variables

Set the following environment variables in your IDE or operating system before starting the application:

```text
MONGODB_URI=<your_mongodb_connection_string>
JWT_SECRET=<your_base64_encoded_secret>
```

The application reads these values from the environment at startup.


### Start Spring Boot

```bash
cd backend/movie-service
mvn spring-boot:run
```

### Start FastAPI

```bash
cd ml_service
uvicorn app:app --reload
```

---

## Future Improvements

- Docker Compose deployment
- Redis caching
- Model retraining pipeline
- Recommendation explanation API
- Movie poster integration
- Recommendation metrics dashboard

---
