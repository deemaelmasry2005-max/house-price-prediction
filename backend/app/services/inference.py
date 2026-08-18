import json
import joblib
import pandas as pd

from app.core.config import settings


class ModelService:
    def __init__(self):
        self.model = None
        self.locations = []

    def load_artifacts(self):
        self.model = joblib.load(settings.MODEL_PATH)

        with open(settings.LOCATIONS_PATH, "r", encoding="utf-8") as f:
            self.locations = json.load(f)

    def predict(self, payload_dict: dict):
        if self.model is None:
            self.load_artifacts()

        df = pd.DataFrame([payload_dict])

        # Rename API fields to the names expected by the ML model
        df = df.rename(columns={
            "bathroom": "Bathroom",
            "balcony": "Balcony",
            "furnishing": "Furnishing",
            "transaction": "Transaction",
            "ownership": "Ownership"
        })

        prediction = self.model.predict(df)

        return float(prediction[0])


model_service = ModelService()