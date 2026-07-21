package com.moviesystem.movie_service.service;

import com.moviesystem.movie_service.dto.MovieResponse;
import com.moviesystem.movie_service.model.Movie;
import com.moviesystem.movie_service.repository.MovieRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class MovieService {
    private final MovieRepository movieRepository;

    public List<MovieResponse> getAllMovies(){
        List<Movie> movies = movieRepository.findAll();
        List<MovieResponse> response = new ArrayList<>();
        for(Movie movie:movies){
            MovieResponse movieResponse = new MovieResponse(movie.getId(), movie.getTitle(), movie.getGenres());
            response.add(movieResponse);
        }
        return response;
    }

    public MovieResponse getMovieById(Integer id){
        Movie movie = movieRepository.findById(id).orElseThrow(() -> new RuntimeException("Movie not found!"));
        return new MovieResponse(movie.getId(), movie.getTitle(), movie.getGenres());
    }
}
