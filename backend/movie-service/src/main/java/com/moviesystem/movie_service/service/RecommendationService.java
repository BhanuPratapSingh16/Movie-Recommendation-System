package com.moviesystem.movie_service.service;

import com.moviesystem.movie_service.client.AIServiceClient;
import com.moviesystem.movie_service.dto.AIRatingRequest;
import com.moviesystem.movie_service.dto.RatingRequest;
import com.moviesystem.movie_service.dto.RecommendationRequest;
import com.moviesystem.movie_service.dto.RecommendationResponse;
import com.moviesystem.movie_service.model.Rating;
import com.moviesystem.movie_service.repository.RatingRepository;
import com.moviesystem.movie_service.security.CustomUserDetails;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class RecommendationService {

    private final RatingRepository ratingRepository;
    private final AIServiceClient aIServiceClient;

    public RecommendationResponse getRecommendations(CustomUserDetails user) {
        String userId = user.getId();
        List<Rating> ratings = ratingRepository.findAllByUserId(userId);
        List<AIRatingRequest> ratingRequests = ratings.stream().map(
                r -> new AIRatingRequest(r.getMovieId(), r.getRating())
        ).toList();
        RecommendationRequest request = new RecommendationRequest();
        request.setRatings(ratingRequests);
        return aIServiceClient.getRecommendations(request);
    }
}