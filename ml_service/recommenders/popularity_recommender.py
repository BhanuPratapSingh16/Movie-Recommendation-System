class PopularityRecommender:
    def __init__(self, popularity_table):
        self.popularity_table = popularity_table

    def recommend(self, top_n=10):
        return self.popularity_table.head(top_n)