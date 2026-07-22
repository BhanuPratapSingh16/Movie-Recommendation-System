package com.moviesystem.movie_service.controller;

import com.moviesystem.movie_service.dto.RatingRequest;
import com.moviesystem.movie_service.dto.RatingResponse;
import com.moviesystem.movie_service.model.Rating;
import com.moviesystem.movie_service.security.CustomUserDetails;
import com.moviesystem.movie_service.service.RatingService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/ratings")
@RequiredArgsConstructor
public class RatingController {

    private final RatingService ratingService;

    @PostMapping("/rate")
    public ResponseEntity<RatingResponse> setRating(@RequestBody RatingRequest request,@AuthenticationPrincipal CustomUserDetails userDetails){
        return ResponseEntity.status(HttpStatus.OK).body(ratingService.rateMovie(request, userDetails.getId()));
    }

    @GetMapping("/me")
    public ResponseEntity<List<RatingResponse>> getRating(@AuthenticationPrincipal CustomUserDetails userDetails){
        return ResponseEntity.status(HttpStatus.OK).body(ratingService.getRatingsByUser(userDetails.getId()));
    }
}
