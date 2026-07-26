package com.moviesystem.movie_service.controller;

import com.moviesystem.movie_service.dto.RecommendationResponse;
import com.moviesystem.movie_service.security.CustomUserDetails;
import com.moviesystem.movie_service.service.RecommendationService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/recommendations")
@RequiredArgsConstructor
public class RecommendationController {
    private final RecommendationService recommendationService;

    @GetMapping("/")
    public ResponseEntity<RecommendationResponse> getRecommendations(@AuthenticationPrincipal CustomUserDetails user){
        return ResponseEntity.status(HttpStatus.OK).body(recommendationService.getRecommendations(user));
    }
}
