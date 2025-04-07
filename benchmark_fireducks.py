import fireducks as fd
from sklearn.preprocessing import MinMaxScaler
from src.config import DATA_PATH
from src.evaluate import evaluate

def benchmark_fireducks():
    load_fd = evaluate("FireDucks Load", lambda: fd.read_parquet(DATA_PATH))
    scaler = MinMaxScaler()
    _ = evaluate("FireDucks Preprocessing", lambda: scaler.fit_transform(load_fd.drop("target").to_numpy()))
