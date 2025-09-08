import streamlit as st
import joblib
from sklearn.linear_model import LinearRegression
import pandas as pd

def load_model() -> LinearRegression:
    return joblib.load('models/regression.joblib')

def start_app(model: LinearRegression):
    st.title("House Price Prediction")
    size = st.number_input("House Size (sq ft)", min_value=0.0, value=20.0, step=10.0)
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=1, step=1)
    garden = int(st.checkbox("Has Garden"))

    X = pd.DataFrame([[size, bedrooms, garden]], columns=['size', 'nb_rooms', 'garden'])
    price_prediction = model.predict(X)
    
    st.markdown("---")
    st.subheader("Predicted House Price")
    st.metric(
        label="Estimated Price",
        value=f"${price_prediction[0]:,.2f}",
        delta=None
    )
    return
    
def main():
    model = load_model()
    start_app(model)

main()