import matplotlib.pyplot as plt

labels = ['Load Parquet', 'Preprocessing']
pandas_times = [load_pandas_time, preprocess_pandas_time]
fireducks_times = [load_fd_time, preprocess_fd_time]

bar_width = 0.35
index = range(len(labels))

plt.figure(figsize=(10, 6))
plt.bar(index, pandas_times, bar_width, label='Pandas', color='skyblue')
plt.bar([i + bar_width for i in index], fireducks_times, bar_width, label='FireDucks', color='salmon')

plt.xlabel('Operation')
plt.ylabel('Time (seconds)')
plt.title('Benchmark: Pandas vs FireDucks')
plt.xticks([i + bar_width / 2 for i in index], labels)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
