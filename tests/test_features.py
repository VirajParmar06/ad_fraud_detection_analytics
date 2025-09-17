import pandas as pd
from src.feature_engineering import make_features

def test_ctr():
    df=pd.DataFrame({
        "event_time": pd.to_datetime(["2025-01-01 00:00:00","2025-01-01 00:00:10"]),
        "user_id":["u1","u1"],"campaign_id":["c1","c1"],"country":["US","US"],"device":["web","web"],"is_click":[0,1]
    })
    feats=make_features(df)
    assert round(feats.loc[0,"ctr"],2)==0.5
