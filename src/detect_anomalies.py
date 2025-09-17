import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURE_COLS=["ctr","max_events_per_min","device_variety"]

def score_anomalies(feats: pd.DataFrame, contamination: float=0.02) -> pd.DataFrame:
    X=feats[FEATURE_COLS].fillna(0.0)
    model=IsolationForest(random_state=42,contamination=contamination)
    model.fit(X)
    scores=-model.decision_function(X)
    out=feats.copy()
    out["anomaly_score"]=scores
    return out.sort_values("anomaly_score",ascending=False)
