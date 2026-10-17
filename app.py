import streamlit as st
import pickle

st.set_page_config(page_title="DA-12 Predictor App", page_icon=":moneybag:", layout="wide")
st.header("DA-12 Predictor App")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

yoe = st.number_input ("Year of Experience", min_value=0.0, max_value=10.0, value=2.0, step=0.5, key="year_of_experience")


if st.button("Predict"):
    prediction = model.predict([[yoe]])
    st.success(prediction)