package com.moviesystem.movie_service.repository;

import com.moviesystem.movie_service.model.Rating;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RatingRepository extends MongoRepository<Rating, String> {
}
