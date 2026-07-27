import api from "./axios";

export const register = (user) => {
    return api.post("/auth/register", user);
};

export const login = (credentials) => {
    return api.post("/auth/login", credentials);
};