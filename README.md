# API Batch Ingestion Pipeline

## Overview
This project demonstrates a production-style data engineering pipeline that ingests data from external APIs, performs incremental ingestion, applies PySpark transformations, and outputs analytics-ready Parquet datasets.

The solution covers the complete lifecycle:

-Raw data ingestion from API

-Incremental record tracking

-Data transformation and enrichment

-Analytics-ready outputs for further consumption

---

## Architecture Overview

**API → Raw Layer → Transformations → Analytics Layer**

### Architecture Diagram
![api-batch-ingestion pipeline](blob/main/docs/posts_analytics_sample.png)

### Data Flow

#### Raw Layer
- Data ingested from external API (JSONPlaceholder)
- Stored as Parquet in data/raw
- Tracks LAST_PROCESSED_ID for incremental ingestion

#### Transformations Layer
- Deduplication & derived columns
- Example: title_length derived from post titles
- Prepares data for analytics consumption

#### Analytics Layer
- Transformed data saved as data/analytics/posts_analytics.parquet
- Ready for Pandas, PySpark, or BI tools


---

## Key Concepts Demonstrated

- Incremental ingestion & idempotent pipelines
- PySpark transformations for scalable processing
- Analytics-ready data outputs
- Config-driven pipelines (.env)
- Logging and monitoring for production workflows

---

## Repository Structure

```text
api-batch-ingestion-pipeline/
├── config/
│   └── ingestion_config.env
├── data/
│   ├── raw/
│   └── analytics/
├── src/
│   ├── ingestion/
│   │   └── api_ingestion.py
│   ├── transformations/
│   │   └── transform_posts.py
│   └── pipeline/
│       └── pipeline.py
├── docs/
│   └── posts_analytics_sample.png
├── requirements.txt
└── README.md



Technologies Used

 Python 3.x
 PySpark
 Pandas
 Parquet format for data storage
 dotenv for configuration


How to Run

Activate virtual environment:venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run pipeline: python -m src.pipeline.pipeline



👤 Author

Alex Elamin
Data Engineer | Python | PySpark | Analytics Pipelines

🔗 GitHub: https://github.com/alex-elamin/api-batch-ingestion-pipeline

🔗 LinkedIn: https://www.linkedin.com/in/alexelamin
