import pandas as pd
from sklearn.datasets import make_classification
from src.config import NUM_SAMPLES, NUM_FEATURES, SEED, DATA_PATH

def generate_and_save_data():
    X, y = make_classification(
        n_samples=NUM_SAMPLES,
        n_features=NUM_FEATURES,
        random_state=SEED
    )
    columns = [f"feature_{i}" for i in range(NUM_FEATURES)]
    df = pd.DataFrame(X, columns=columns)
    df["target"] = y
    df.to_parquet(DATA_PATH)
    print(f"Dataset saved to {DATA_PATH}")
