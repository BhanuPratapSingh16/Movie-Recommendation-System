package com.moviesystem.movie_service.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;
import io.jsonwebtoken.Jwts;

import javax.crypto.SecretKey;
import java.util.Date;

@Service
public class JwtService {
    private final String secretKey;

    public JwtService(@Value("${jwt.secret}") String secretKey){
        this.secretKey = secretKey;
    }

    public String generateAccessToken(CustomUserDetails userDetails){
        long now = System.currentTimeMillis();

        return Jwts.builder()
                .subject(userDetails.getId())
                .claim("type", "access")
                .issuedAt(new Date(now))
                .expiration(new Date(now + 1000 * 60 * 60 * 24))
                .signWith(getSigningKey())
                .compact();
    }

    public String generateRefreshToken(CustomUserDetails userDetails) {
        long now = System.currentTimeMillis();

        return Jwts.builder()
                .subject(userDetails.getId())
                .claim("type", "refresh")
                .issuedAt(new Date(now))
                .expiration(new Date(now + 1000L * 60 * 60 * 24 * 7))
                .signWith(getSigningKey())
                .compact();
    }

    public String extractUserId(String token) {
        return extractAllClaims(token).getSubject();
    }

    public boolean isAccessTokenValid(String token, CustomUserDetails userDetails) {
        String userId = extractUserId(token);
        String tokenType = extractTokenType(token);
        return userId.equals(userDetails.getId()) && tokenType.equals("access") && !isTokenExpired(token);
    }

    public boolean isRefresTokenValid(String token, CustomUserDetails userDetails) {
        String userId = extractUserId(token);
        String tokenType = extractTokenType(token);
        return userId.equals(userDetails.getId()) && tokenType.equals("refresh") && !isTokenExpired(token);
    }

    public String extractTokenType(String token){
        return extractAllClaims(token).get("type", String.class);
    }

    private SecretKey getSigningKey() {
        byte[] keyBytes = Decoders.BASE64.decode(secretKey);
        return Keys.hmacShaKeyFor(keyBytes);
    }

    private Claims extractAllClaims(String token) {
        return Jwts.parser()
                .verifyWith(getSigningKey())
                .build()
                .parseSignedClaims(token)
                .getPayload();
    }

    private boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    private Date extractExpiration(String token) {
        return extractAllClaims(token).getExpiration();
    }
}
