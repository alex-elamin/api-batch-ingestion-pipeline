from src.ingestion import api_ingestion
from src.transformations import transform_posts

def run_pipeline():
    print("Starting pipeline...")
    api_ingestion.run()
    transform_posts.transform()
    print("Pipeline finished successfully.")

if __name__ == "__main__":
    run_pipeline()
