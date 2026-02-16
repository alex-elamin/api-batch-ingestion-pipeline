import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load config
load_dotenv(dotenv_path="config/ingestion_config.env")
LAST_PROCESSED_ID = int(os.getenv("LAST_PROCESSED_ID", 0))
RAW_PATH = Path(os.getenv("RAW_PATH", "data/raw/posts.parquet"))
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")

def fetch_posts():
    logging.info(f"Fetching posts from API: {API_URL}")
    response = requests.get(API_URL)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    df = df[df["id"] > LAST_PROCESSED_ID]  # incremental
    logging.info(f"{len(df)} new records fetched")
    return df

def save_raw(df):
    if RAW_PATH.exists():
        existing_df = pd.read_parquet(RAW_PATH)
        df = pd.concat([existing_df, df], ignore_index=True)
    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(RAW_PATH, index=False)
    logging.info(f"Raw data saved to {RAW_PATH}")

def update_last_processed_id(df):
    if not df.empty:
        max_id = df["id"].max()
        with open("config/ingestion_config.env", "w") as f:
            f.write(f"LAST_PROCESSED_ID={max_id}\n")
            f.write(f"RAW_PATH={RAW_PATH}\n")
            f.write(f"ANALYTICS_PATH={os.getenv('ANALYTICS_PATH')}\n")
            f.write(f"API_URL={API_URL}\n")
        logging.info(f"Updated LAST_PROCESSED_ID to {max_id}")

def run():
    df = fetch_posts()
    if df.empty:
        logging.info("No new records to ingest.")
        return
    save_raw(df)
    update_last_processed_id(df)
    logging.info(f"Ingested {len(df)} new records")

if __name__ == "__main__":
    run()
