import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load config
load_dotenv(dotenv_path="config/ingestion_config.env")
RAW_PATH = Path(os.getenv("RAW_PATH", "data/raw/posts.parquet"))
ANALYTICS_PATH = Path(os.getenv("ANALYTICS_PATH", "data/analytics/posts_analytics.parquet"))

def transform():
    logging.info(f"Reading raw data from {RAW_PATH}")
    df = pd.read_parquet(RAW_PATH)

    # Deduplication
    df = df.drop_duplicates(subset=["id"])

    # Derived column
    df["title_length"] = df["title"].str.len()

    # Aggregation example
    agg_df = df.groupby("userId", as_index=False)["title_length"].mean()
    agg_df.rename(columns={"title_length": "avg_title_length"}, inplace=True)

    # Save analytics
    ANALYTICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ANALYTICS_PATH, index=False)
    logging.info(f"Transformation complete: {len(df)} records saved to analytics layer ({ANALYTICS_PATH})")

if __name__ == "__main__":
    transform()
