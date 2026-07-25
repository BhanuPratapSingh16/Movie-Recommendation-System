package com.moviesystem.movie_service.client;

import com.moviesystem.movie_service.dto.RecommendationResponse;
import com.moviesystem.movie_service.security.CustomUserDetails;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

@Service
@RequiredArgsConstructor
public class AIServiceClient {
    private final RestClient aiRestClient;

    public RecommendationResponse getRecommendations(@AuthenticationPrincipal CustomUserDetails userDetails){
        return aiRestClient
                .post()
                .uri("/recommend")
                .body(request)
                .retrieve()
                .body(RecommendationResponse.class);
    }

}
