import os
from src.config import FIREDUCKS_BENCHMARK
from src.data_generator import generate_and_save_data
from src.benchmark_pandas import benchmark_pandas
from src.benchmark_fireducks import benchmark_fireducks

# Set benchmarking mode
os.environ["FIREDUCKS_BENCHMARK"] = FIREDUCKS_BENCHMARK

if __name__ == "__main__":
    generate_and_save_data()
    benchmark_pandas()
    benchmark_fireducks()
