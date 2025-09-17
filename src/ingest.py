import pandas as pd

def read_events(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")
    df = df.dropna(subset=["event_time"])
    return df
