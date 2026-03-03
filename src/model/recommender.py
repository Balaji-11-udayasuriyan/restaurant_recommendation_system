class RestaurantRecommender:

    def __init__(self, df, feature_builder):
        self.df = df
        self.feature_builder = feature_builder

    def recommend(self, cuisine, price_range, top_n=5):

        user_input = cuisine + " " + str(price_range)
        user_vector = self.feature_builder.transform_user_input(user_input)

        similarity_scores = self.feature_builder.compute_similarity(user_vector)
        similar_indices = similarity_scores.argsort()[0][-top_n:][::-1]

        recommendations = self.df.iloc[similar_indices][
            ["Restaurant Name", "Cuisines", "Price range", "Aggregate rating"]
        ]

        return recommendations