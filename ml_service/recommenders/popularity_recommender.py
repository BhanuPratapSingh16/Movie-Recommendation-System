class PopularityRecommender:
    def __init__(self, popularity_table):
        self.popularity_table = popularity_table

    def recommend(self, top_n=100):
        recoms = self.popularity_table.head(top_n)[["movie_id", "weighted_rating"]]
        return dict(zip(recoms["movie_id"].astype(int), recoms["weighted_rating"].astype(float)))