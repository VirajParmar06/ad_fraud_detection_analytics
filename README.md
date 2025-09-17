# Ad Fraud Detection & Campaign Analytics

End-to-end project to simulate suspicious activity detection in ad campaigns.

## Features
- Synthetic clickstream dataset
- ETL + feature engineering
- Isolation Forest anomaly detection
- Rule-based policy enforcement (CTR, burstiness, device variety)
- Reports: CSV + chart
- FastAPI scoring endpoint
- Docker + Makefile for deployment

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py --input data/sample_events.csv --model_out models/isoforest.pkl
python src/pipeline.py --input data/sample_events.csv --outdir reports
uvicorn app.main:app --reload --port 8000
```
