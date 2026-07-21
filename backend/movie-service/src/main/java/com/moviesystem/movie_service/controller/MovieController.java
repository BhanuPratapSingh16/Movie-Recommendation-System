package com.moviesystem.movie_service.controller;

import com.moviesystem.movie_service.dto.MovieResponse;
import com.moviesystem.movie_service.service.MovieService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/movies")
@RequiredArgsConstructor
public class MovieController {

    private final MovieService movieService;

    @GetMapping("/")
    public ResponseEntity<List<MovieResponse>> getAllMovies(){
        return ResponseEntity.status(HttpStatus.OK).body(movieService.getAllMovies());
    }

    @GetMapping("/{id}")
    public ResponseEntity<MovieResponse> getMovieById(@PathVariable String id){
        return ResponseEntity.status(HttpStatus.OK).body(movieService.getMovieById(Integer.parseInt(id)));
    }
}
