import argparse, os
from ingest import read_events
from feature_engineering import make_features
from detect_anomalies import score_anomalies
from report import write_report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--outdir", required=True)
    args=ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    events=read_events(args.input)
    feats=make_features(events)
    scored=score_anomalies(feats)
    write_report(scored,args.outdir)
    print("Wrote reports to",args.outdir)

if __name__=="__main__":
    main()
