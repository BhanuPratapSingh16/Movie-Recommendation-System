package com.moviesystem.movie_service.service;

import com.moviesystem.movie_service.dto.RatingRequest;
import com.moviesystem.movie_service.dto.RatingResponse;
import com.moviesystem.movie_service.model.Rating;
import com.moviesystem.movie_service.repository.RatingRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class RatingService {
    private final RatingRepository ratingRepository;

    public RatingResponse rateMovie(RatingRequest request, String userId){
        Rating rating = new Rating();
        rating.setUserId(userId);
        rating.setMovieId(request.getMovieId());
        rating.setRating(request.getRating());

        Rating savedRating = ratingRepository.save(rating);

        RatingResponse response = new RatingResponse();
        response.setId(savedRating.getId());
        response.setMovieId(savedRating.getMovieId());
        response.setRating(savedRating.getRating());
        return response;
    }

    public List<RatingResponse> getRatingsByUser(String userId){
        List<Rating> ratings = ratingRepository.findAllByUserId(userId);
        List<RatingResponse> response = new ArrayList<>();
        for(Rating rating:ratings){
            RatingResponse ratingResponse = new RatingResponse();
            ratingResponse.setId(rating.getId());
            ratingResponse.setMovieId(rating.getMovieId());
            ratingResponse.setRating(rating.getRating());
            response.add(ratingResponse);
        }
        return response;
    }
}
