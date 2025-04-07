import os
from dotenv import load_dotenv

load_dotenv()

FIREDUCKS_BENCHMARK = os.getenv("FIREDUCKS_BENCHMARK", "1")
DATA_PATH = os.getenv("DATA_PATH", "./data/benchmark_dataset.parquet")
NUM_SAMPLES = int(os.getenv("NUM_SAMPLES", 10_000_000))
NUM_FEATURES = int(os.getenv("NUM_FEATURES", 20))
SEED = int(os.getenv("SEED", 42))
