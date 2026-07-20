package com.moviesystem.movie_service.model;

import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@Document(collection = "movies")
public class Movie {
    Integer movieId;
    String name;
    List<String> genres;
}
