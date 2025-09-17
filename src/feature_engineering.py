import pandas as pd

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    df=df.copy()
    df["minute"]=df["event_time"].dt.floor("min")
    per_user=df.groupby("user_id").agg(impressions=("is_click","count"),clicks=("is_click","sum")).reset_index()
    per_user["ctr"]=(per_user["clicks"]/per_user["impressions"]).fillna(0.0)
    burst=df.groupby(["user_id","minute"]).size().reset_index(name="events_per_min")
    burstiness=burst.groupby("user_id")["events_per_min"].max().reset_index(name="max_events_per_min")
    dev=df.groupby("user_id")["device"].nunique().reset_index(name="device_variety")
    feats=per_user.merge(burstiness,on="user_id",how="left").merge(dev,on="user_id",how="left")
    feats["device_variety"]=feats["device_variety"].fillna(1)
    return feats
