package com.moviesystem.movie_service.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class RatingResponse {
    private String id;
    private Integer movieId;
    private Integer rating;
}
