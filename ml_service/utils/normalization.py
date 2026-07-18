def min_max_norm(scores):
    values = list(scores.values())
    min_score = min(values)
    max_score = max(values)

    return {movie_id : (score - min_score) / (max_score - min_score) for movie_id, score in scores.items()}