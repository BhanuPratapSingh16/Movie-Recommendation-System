package com.moviesystem.movie_service.config;


import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestClient;

@Configuration
public class RestClientConfig {
    @Bean
    public RestClient aiRestClient(){
        return RestClient.builder().baseUrl("https://localhost:8080").build();
    }
}
