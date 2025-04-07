import matplotlib.pyplot as plt

def plot_benchmark(pandas_times, fd_times):
    labels = ['Load', 'Preprocess']
    bar_width = 0.35
    index = range(len(labels))

    plt.figure(figsize=(10,6))
    plt.bar(index, pandas_times, bar_width, label='pandas', color='skyblue')
    plt.bar([i + bar_width for i in index], fd_times, bar_width, label='FireDucks', color='salmon')

    plt.xlabel('Task')
    plt.ylabel('Time (sec)')
    plt.title('FireDucks vs Pandas Benchmark')
    plt.xticks([i + bar_width / 2 for i in index], labels)
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    plt.show()
