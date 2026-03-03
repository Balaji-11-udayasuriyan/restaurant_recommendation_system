from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FeatureBuilder:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = None

    def fit_transform(self, df):
        df["combined_features"] = (
            df["Cuisines"] + " " +
            df["Price range"].astype(str)
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(df["combined_features"])
        return self.tfidf_matrix

    def transform_user_input(self, user_input):
        return self.vectorizer.transform([user_input])

    def compute_similarity(self, user_vector):
        return cosine_similarity(user_vector, self.tfidf_matrix)