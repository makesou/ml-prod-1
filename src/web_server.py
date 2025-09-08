from fastapi import FastAPI
from fastapi.responses import Response 
from pydantic import BaseModel
import joblib
from sklearn.linear_model import LinearRegression
import pandas as pd

class PredictionRequest(BaseModel):
    size: float
    nb_rooms: int
    garden: bool

def load_model() -> LinearRegression:
    return joblib.load('models/regression.joblib')

app = FastAPI()
model = load_model()

@app.get("/predict")
def get_prediction():
    return {"y_pred": 2}

@app.post("/predict")
def send_prediction(request: PredictionRequest):
    X = pd.DataFrame([[request.size, request.nb_rooms, int(request.garden)]], ['size', 'nb_rooms', 'garden'])
    prediction = model.predict(X)
    return {"y_pred": prediction[0]}