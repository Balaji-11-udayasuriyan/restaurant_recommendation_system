from src.config import DATA_PATH, TOP_N
from src.data_preprocessing.preprocess import load_data, clean_data
from src.feature_engineering.vectorizer import FeatureBuilder
from src.model.recommender import RestaurantRecommender
from src.utils.helper import print_header

def main():

    print_header("Restaurant Recommendation System")

    # Load & Clean
    df = load_data(DATA_PATH)
    df = clean_data(df)

    # Feature Engineering
    feature_builder = FeatureBuilder()
    feature_builder.fit_transform(df)

    # Model
    recommender = RestaurantRecommender(df, feature_builder)

    # Sample Test
    cuisine = "North Indian"
    price_range = 2

    recommendations = recommender.recommend(cuisine, price_range, TOP_N)

    print("\nTop Recommendations:\n")
    print(recommendations)


if __name__ == "__main__":
    main()