# fireducks-vs-pandas-benchmark
# Simplifying AI/ML Pipelines with FireDucks: A Threat to Pandas
Welcome to the official repository of the blog "Simplifying AI/ML Pipelines with FireDucks: A Threat to Pandas" — a hands-on benchmarking project exploring how FireDucks dramatically accelerates AI data workflows compared to traditional tools like pandas.

This repo contains synthetic dataset generation, benchmarking scripts, preprocessing pipelines, and visual comparisons using FireDucks and pandas.

# Overview
In the age of large-scale AI and real-time ML, data ingestion and preprocessing can become bottlenecks. While pandas is a widely adopted data tool, it lacks GPU acceleration, multi-threading, and memory efficiency.
FireDucks is here to fix that — it’s a blazing-fast dataframe engine powered by DuckDB and PyTorch, enabling:

1) Parallel, columnar data loading
2) Lazy evaluation
3) GPU/CPU hybrid execution
4) pandas-like API with high-speed performance

# Project Structure
├── generate_dataset.py         
├── benchmark_pandas.py         
├── benchmark_fireducks.py      
├── visualize_results.py        
├── requirements.txt            
└── README.md                   

# Setup & Installation
# Clone the Repo
git clone https://github.com/soumita654/fireducks-vs-pandas-benchmark.git

cd fireducks-vs-pandas-benchmark

# Install Dependencies
pip install -r requirements.txt

# Enable Benchmark Mode for FireDucks
export FIREDUCKS_BENCHMARK=1  # For Unix/Mac

set FIREDUCKS_BENCHMARK=1     # For Windows (CMD)

