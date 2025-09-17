import argparse, joblib, os
from ingest import read_events
from feature_engineering import make_features
from detect_anomalies import FEATURE_COLS
from sklearn.ensemble import IsolationForest

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model_out", required=True)
    args=ap.parse_args()
    events=read_events(args.input)
    feats=make_features(events)
    X=feats[FEATURE_COLS].fillna(0.0)
    model=IsolationForest(random_state=42, contamination=0.02)
    model.fit(X)
    os.makedirs(os.path.dirname(args.model_out), exist_ok=True)
    joblib.dump(model,args.model_out)
    print("Model saved to",args.model_out)

if __name__=="__main__":
    main()
