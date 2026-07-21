package com.moviesystem.movie_service.service;

import com.moviesystem.movie_service.dto.*;
import com.moviesystem.movie_service.model.User;
import com.moviesystem.movie_service.repository.UserRepository;
import com.moviesystem.movie_service.security.CustomUserDetails;
import com.moviesystem.movie_service.security.CustomUserDetailsService;
import com.moviesystem.movie_service.security.JwtService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final JwtService jwtService;
    private final CustomUserDetailsService userDetailsService;

    public RegisterResponse register(RegisterRequest request){
        if(userRepository.existsByEmail((request.getEmail()))){
            throw new RuntimeException("User already exists! Try login!");
        }
        User user = new User();
        user.setEmail(request.getEmail());
        user.setName(request.getName());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        userRepository.save(user);

        RegisterResponse response = new RegisterResponse();
        response.setId(user.getId());
        response.setName(user.getName());
        response.setEmail(user.getEmail());
        return response;
    }

    public LoginResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail()).orElseThrow(() -> new UsernameNotFoundException("User not found!"));
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                    request.getEmail(),
                    request.getPassword()
                )
        );

        CustomUserDetails userDetails = (CustomUserDetails) authentication.getPrincipal();
        String accessToken = jwtService.generateAccessToken(userDetails);
        String refreshToken = jwtService.generateRefreshToken(userDetails);

        LoginResponse response = new LoginResponse();
        response.setId(user.getId());
        response.setName(user.getName());
        response.setEmail(user.getEmail());
        response.setAccessToken(accessToken);
        response.setRefreshToken(refreshToken);
        return response;
    }

    public RefreshTokenResponse refreshToken(RefreshTokenRequest request){
        String refreshToken = request.getRefreshToken();

        String userId = jwtService.extractUserId(refreshToken);

        CustomUserDetails userDetails = userDetailsService.loadUserById(userId);

        if(!jwtService.isRefresTokenValid(refreshToken, userDetails)){
            throw new RuntimeException("Refresh token invalid!");
        }
        RefreshTokenResponse response = new RefreshTokenResponse();
        response.setAccessToken(jwtService.generateAccessToken(userDetails));
        return response;
    }
}
