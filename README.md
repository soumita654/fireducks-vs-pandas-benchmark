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

<pre> 📂 fireducks-vs-pandas-benchmark

├── 🐍 generate_dataset.py         
├── 🐼 benchmark_pandas.py
├── 🔥 benchmark_fireducks.py      
├── 📊 visualize_results.py        
├── 📄 requirements.txt            
└── 📘 README.md </pre>                  

# ⚙️ Setup & Installation

# 📥 Clone the Repository

<pre>git clone https://github.com/soumita654/fireducks-vs-pandas-benchmark.git

cd fireducks-vs-pandas-benchmark</pre>

# 📦 Install Requirements

<pre> pip install -r requirements.txt</pre>

# 🧪 Enable FireDucks Benchmarking Mode

<pre> export FIREDUCKS_BENCHMARK=1  # For Unix/Mac

set FIREDUCKS_BENCHMARK=1   # For Windows (CMD) </pre>


# 🧪 Run the Benchmark

# 🧬 Generate the Dataset

<pre> python benchmark_pandas.py </pre>

# 🐼 Benchmark pandas

<pre> python benchmark_pandas.py</pre>

# 🔥 Benchmark FireDucks

<pre> python benchmark_fireducks.py </pre>

# 📊 Visualize Results

<pre> python visualize_results.py </pre>

# 🤝 Contributing

WFound a bug? Want to add more comparisons or improve benchmarks?

✅ Fork this repo

✅ Create a new branch

✅ Submit a pull request

Or just open an issue – we’d love to hear from you!

# 📄 License
This project is licensed under the MIT License. 
Feel free to use, modify, and share! ✨
