import matplotlib.pyplot as plt

def write_report(scored, outdir: str, top_n: int=50):
    scored.head(top_n).to_csv(f"{outdir}/anomalies.csv", index=False)
    plt.figure()
    plt.plot(range(top_n), scored.head(top_n)["anomaly_score"].values, marker="o")
    plt.title("Top Anomalous Users")
    plt.xlabel("Rank")
    plt.ylabel("Anomaly Score")
    plt.tight_layout()
    plt.savefig(f"{outdir}/anomalies.png")
    plt.close()
