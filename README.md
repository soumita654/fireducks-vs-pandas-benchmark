# fireducks-vs-pandas-benchmark
# 🔥 Simplifying AI/ML Pipelines with FireDucks: A Threat to Pandas 🐼

Welcome to the official GitHub repo for the blog:
"Simplifying AI/ML Pipelines with FireDucks: A Threat to Pandas" 🧠💻
This project showcases how FireDucks, a powerful DuckDB + PyTorch-powered dataframe engine, outperforms traditional pandas in handling large-scale AI/ML data workflows. Fast, memory-efficient, and supercharged for modern data pipelines! ⚡


# Overview
In the age of large-scale AI and real-time ML, data ingestion and preprocessing can become bottlenecks. While pandas is a widely adopted data tool, it lacks GPU acceleration, multi-threading, and memory efficiency.
FireDucks is here to fix that — it’s a blazing-fast dataframe engine powered by DuckDB and PyTorch, enabling:

1) Parallel, columnar data loading
2) Lazy evaluation
3) GPU/CPU hybrid execution
4) pandas-like API with high-speed performance

# 📁 Project Structure

📂 fireducks-vs-pandas-benchmark

├── 🐍 generate_dataset.py         
├── 🐼 benchmark_pandas.py
├── 🔥 benchmark_fireducks.py      
├── 📊 visualize_results.py        
├── 📄 requirements.txt            
└── 📘 README.md                  

# ⚙️ Setup & Installation

# 📥 Clone the Repository

git clone https://github.com/soumita654/fireducks-vs-pandas-benchmark.git

cd fireducks-vs-pandas-benchmark

# 📦 Install Requirements

``` pip install -r requirements.txt ``` 

# 🧪 Enable FireDucks Benchmarking Mode

```export FIREDUCKS_BENCHMARK=1```  # For Unix/Mac

```set FIREDUCKS_BENCHMARK=1```    # For Windows (CMD)


# 🧪 Run the Benchmark

# 🧬 Generate the Dataset

```python generate_dataset.py```

# 🐼 Benchmark pandas

```python benchmark_pandas.py```

# 🔥 Benchmark FireDucks

```python benchmark_fireducks.py```

# 📊 Visualize Results

```python visualize_results.py```

# 🤝 Contributing

WFound a bug? Want to add more comparisons or improve benchmarks?

✅ Fork this repo

✅ Create a new branch

✅ Submit a pull request

Or just open an issue – we’d love to hear from you!

# 📄 License
This project is licensed under the MIT License. 
Feel free to use, modify, and share! ✨
