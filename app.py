import streamlit as st
from src.config import DATA_PATH
from src.data_preprocessing.preprocess import load_data, clean_data
from src.feature_engineering.vectorizer import FeatureBuilder
from src.model.recommender import RestaurantRecommender

df = load_data(DATA_PATH)
df = clean_data(df)

feature_builder = FeatureBuilder()
feature_builder.fit_transform(df)

recommender = RestaurantRecommender(df, feature_builder)

st.title("🍽 Restaurant Recommendation System")

cuisine = st.text_input("Enter Preferred Cuisine")
price = st.selectbox("Select Price Range", [1,2,3,4])

if st.button("Recommend"):
    result = recommender.recommend(cuisine, price)
    st.write(result)