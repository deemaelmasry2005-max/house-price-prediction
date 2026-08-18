import os
from pathlib import Path
from pydantic_settings import BaseSettings

# تحديد مجلد house-price-project الرئيسي
BASE_DIR = Path(__file__).resolve().parents[3]

def find_file(filename: str, possible_subdirs: list[str]) -> str:
    for subdir in possible_subdirs:
        path = BASE_DIR / subdir / filename if subdir else BASE_DIR / filename
        if path.exists():
            return str(path)
    return str(BASE_DIR / filename)

class Settings(BaseSettings):
    PROJECT_NAME: str = "House Price Prediction API"
    
    MODEL_PATH: str = find_file(
        "house_price_random_forest.pkl", 
        ["models", "backend/models", ""]
    )
    
    LOCATIONS_PATH: str = find_file(
        "locations.json", 
        ["models", "data", "backend", ""]
    )
    
    ALLOWED_ORIGINS: list[str] = ["*"]

settings = Settings()

print(f"\n[DEBUG] Project Directory: {BASE_DIR}")
print(f"[DEBUG] MODEL_PATH: {settings.MODEL_PATH} | (Exists: {os.path.exists(settings.MODEL_PATH)})")
print(f"[DEBUG] LOCATIONS_PATH: {settings.LOCATIONS_PATH} | (Exists: {os.path.exists(settings.LOCATIONS_PATH)})\n")