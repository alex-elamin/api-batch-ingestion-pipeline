# API Batch Ingestion Pipeline

## Overview
This project is a **production-style data engineering pipeline** that ingests data from an API, stores it in a raw layer, transforms it, and outputs analytics-ready data.

**Features:**
- Incremental ingestion with tracking of last processed records
- Raw and analytics layers stored in Parquet format
- Transformation with deduplication, derived columns, and aggregation
- Configurable paths and API endpoint via `.env` file
- Logging with timestamps for better observability
- One-command pipeline runner (`pipeline.py`)

## Data Flow


## Sample Analytics Output

![Analytics Sample](docs/posts_analytics_sample.png)
