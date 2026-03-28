# Crypto Data Platform (Databricks)

## Overview
This project implements a scalable, metadata-driven data pipeline using Databricks.

## Architecture
- Bronze: Raw ingestion from CoinGecko API
- Silver: Data cleaning, deduplication, merge
- Gold: Aggregated reporting tables

## Features
- Dynamic DAG creation using Databricks Jobs API
- Config-driven pipeline onboarding
- Delta Lake storage
- Partitioning and deduplication

## How to Run

1. Upload code to Databricks Repos
2. Create cluster
3. Run:
   python orchestrator/create_jobs.py

## Future Improvements
- Add streaming ingestion
- Add data quality checks
- CI/CD pipeline