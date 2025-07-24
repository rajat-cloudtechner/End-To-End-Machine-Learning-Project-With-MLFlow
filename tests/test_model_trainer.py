import os
import pandas as pd
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

def test_model_trainer_saves_model():
    pipeline = ModelTrainerTrainingPipeline()
    pipeline.main()
    output = os.path.join("artifacts/model_trainer", "model.pkl")
    assert os.path.exists(output), f"Model file not found: {output}"
