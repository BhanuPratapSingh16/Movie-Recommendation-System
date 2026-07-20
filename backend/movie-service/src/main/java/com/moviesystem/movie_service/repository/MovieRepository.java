package com.moviesystem.movie_service.repository;

import com.moviesystem.movie_service.model.Movie;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MovieRepository extends MongoRepository<Movie, Integer> {
}
