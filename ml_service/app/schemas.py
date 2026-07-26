from pydantic import BaseModel

class RatingInput(BaseModel):
    movie_id:int
    rating:int

class RecommendationRequest(BaseModel):
    ratings: list[RatingInput]