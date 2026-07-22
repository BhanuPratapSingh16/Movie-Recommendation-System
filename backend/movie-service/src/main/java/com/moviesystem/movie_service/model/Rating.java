package com.moviesystem.movie_service.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "ratings")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Rating {
    @Id
    private String id;
    private String userId;
    private Integer movieId;
    private Integer rating;
}
