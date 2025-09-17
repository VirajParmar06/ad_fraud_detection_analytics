from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd, joblib, os
from src.feature_engineering import make_features
from src.detect_anomalies import FEATURE_COLS

app=FastAPI(title="Ad Fraud Scoring API")
MODEL_PATH="models/isoforest.pkl"
model=None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model=joblib.load(MODEL_PATH)

class Event(BaseModel):
    event_time:str
    user_id:str
    campaign_id:str
    country:str
    device:str
    is_click:int

class Batch(BaseModel):
    events:list[Event]

@app.post("/score")
def score(batch: Batch):
    df=pd.DataFrame([e.dict() for e in batch.events])
    df["event_time"]=pd.to_datetime(df["event_time"], errors="coerce")
    feats=make_features(df)
    if model is None:
        return {"error":"Model not loaded"}
    scores=-model.decision_function(feats[FEATURE_COLS].fillna(0.0))
    feats["anomaly_score"]=scores
    return feats.sort_values("anomaly_score",ascending=False).head(20).to_dict(orient="records")
