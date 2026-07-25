package com.moviesystem.movie_service.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class RecommendationItem {
    @JsonProperty("movie_id")
    private Integer movieId;
    private String title;
    private Double score;
}
