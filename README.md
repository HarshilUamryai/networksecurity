### network security project for phising data ###

Run `python main.py` from the project root. If MongoDB is unavailable, ingestion falls back to `network_data/phisingData.csv` and records a warning in the logs. To ingest from MongoDB, start the MongoDB service and configure `MONGO_URL` in `.env`.