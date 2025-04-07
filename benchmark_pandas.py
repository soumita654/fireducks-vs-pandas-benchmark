import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src.config import DATA_PATH
from src.evaluate import evaluate

def benchmark_pandas():
    load_pandas = evaluate("Pandas Load", lambda: pd.read_parquet(DATA_PATH))
    scaler = MinMaxScaler()
    _ = evaluate("Pandas Preprocessing", lambda: scaler.fit_transform(load_pandas.drop("target", axis=1)))
