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
```
fireducks-vs-pandas-benchmark
├── 🐍 generate_dataset.py
├── 🐼 benchmark_pandas.py
├── 🔥 benchmark_fireducks.py
├── 📊 visualize_results.py
├── 📄 requirements.txt
└── 📘 README.md
```
# 🛠 Tools & Technologies Used
- #### pandas: Comparison baseline
- #### fireducks: Fast dataframe engine
- #### sklearn: For creating and preprocessing synthetic ML data
- #### matplotlib: Plotting
- #### time: Benchmarking measurement

### 📂 Files and Directories

- **generate_dataset.py**: This script generates a synthetic dataset to be used for benchmarking.
- **benchmark_pandas.py**: This script benchmarks the performance of data processing tasks using the Pandas library.
- **benchmark_fireducks.py**: This script benchmarks the performance of data processing tasks using the Fireducks library.
- **visualize_results.py**: This script visualizes the results of the benchmarks, comparing the performance of Fireducks and Pandas.
- **requirements.txt**: This file contains a list of dependencies required to run the scripts.
- **README.md**: This file contains information about the project.

# 🚀 Getting Started

## ⚙️ Setup & Installation

### 📥 Clone the Repository
```bash
!git clone https://github.com/soumita654/fireducks-vs-pandas-benchmark.git
cd fireducks-vs-pandas-benchmark
```
### 📦 Prerequisites

Make sure you have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
### 🧪 Enable FireDucks Benchmarking Mode

```bash
export FIREDUCKS_BENCHMARK=1  # For Unix/Mac

set FIREDUCKS_BENCHMARK=1   # For Windows (CMD)
```
## 🧪 Run the Benchmark

1. **Generate Dataset**: First, generate the dataset by running the `generate_dataset.py` script.

    ```bash
    python generate_dataset.py
    ```

2. **Benchmark with Pandas**: Run the `benchmark_pandas.py` script to benchmark the performance with the Pandas library.

    ```bash
    python benchmark_pandas.py
    ```

3. **Benchmark with Fireducks**: Run the `benchmark_fireducks.py` script to benchmark the performance with the Fireducks library.

    ```bash
    python benchmark_fireducks.py
    ```

4. **Visualize Results**: Finally, visualize the benchmark results by running the `visualize_results.py` script.

    ```bash
    python visualize_results.py
    ```

## ✅ Results

The results of the benchmarks will be visualized and saved as images in the `results` directory. These visualizations will help in comparing the performance of Fireducks and Pandas for various data processing tasks.

## 🤝 Contributing

WFound a bug? Want to add more comparisons or improve benchmarks?

✅ Fork this repo

✅ Create a new branch

✅ Submit a pull request

Or just open an issue – we’d love to hear from you!

## 📄 License
This project is licensed under the MIT License. 
Feel free to use, modify, and share! ✨
