package com.moviesystem.movie_service.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "ratings")
public class Rating {
    @Id
    String id;
    String userId;
    Integer movieId;
    Integer rating;
}
