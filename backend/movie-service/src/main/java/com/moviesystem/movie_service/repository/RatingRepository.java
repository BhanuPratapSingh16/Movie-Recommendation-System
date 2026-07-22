package com.moviesystem.movie_service.repository;

import com.moviesystem.movie_service.model.Rating;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface RatingRepository extends MongoRepository<Rating, String> {
    List<Rating> findAllByUserId(String userId);
}
