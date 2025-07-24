import os
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

def test_data_ingestion_creates_artifacts():
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    assert os.path.exists("artifacts/data_ingestion"), "Data ingestion directory missing"
