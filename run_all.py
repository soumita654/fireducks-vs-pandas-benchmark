from IPython import get_ipython
from IPython.display import display
# %%
#Enable FireDucks Benchmark Mode
import os
os.environ["FIREDUCKS_BENCHMARK"] = "1"
# %%
def evaluate(label, func):
    import time
    start = time.time()
    result = func()
    end = time.time()
    print(f"{label}: {end - start:.4f} sec")
    return result

# %%
!pip install fireducks
import pandas as pd
import fireducks.pandas as fpd # Change to fpd to avoid conflict
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=10_000_000, n_features=20, random_state=42)
columns = [f'feature_{i}' for i in range(20)]

df_pd = pd.DataFrame(X, columns=columns)
df_pd['target'] = y

# Save as Parquet (used for both tools)
df_pd.to_parquet('benchmark_dataset.parquet')
# %%

# %%
# Removed conflicting import - import pandas as pd
# Removed conflicting import - import fireducks.pandas as pd
# %%

# %%
import time
from sklearn.preprocessing import MinMaxScaler
import pandas as pd # Make sure pandas is imported and aliased as pd

# Load with pandas
start = time.time()
df_pandas = pd.read_parquet('benchmark_dataset.parquet') # Now pd refers to pandas
df_pandas.head()  # Force evaluation
load_pandas_time = time.time() - start

# Preprocessing with pandas
start = time.time()
scaler = MinMaxScaler()
scaled_pandas = scaler.fit_transform(df_pandas.drop('target', axis=1))
_ = scaled_pandas.mean()  # Force evaluation
preprocess_pandas_time = time.time() - start
# %%
# Load with FireDucks
import time # Import the time module here
import fireducks.pandas as fpd  # Import fireducks.pandas as fpd here

start = time.time()
df_fd = fpd.read_parquet('benchmark_dataset.parquet') # Use fpd to call read_parquet
df_fd.head()  # Force evaluation
load_fd_time = time.time() - start

# Preprocessing
start = time.time()
# Use the columns attribute to select columns to drop
fd_values = df_fd[[col for col in df_fd.columns if col != 'target']].to_numpy()

# Assuming 'scaler' is defined in a previous cell
# If not, you'll need to define it before using it here
from sklearn.preprocessing import MinMaxScaler # import MinMaxScaler
scaler = MinMaxScaler() # define scaler

scaled_fd = scaler.fit_transform(fd_values)
_ = scaled_fd.mean()  # Force evaluation
preprocess_fd_time = time.time() - start
# %%
print("\n=== Benchmark Summary ===")
print(f"Pandas Load Time         : {load_pandas_time:.2f} sec")
print(f"FireDucks Load Time      : {load_fd_time:.2f} sec")
print(f"Pandas Preprocessing Time: {preprocess_pandas_time:.2f} sec")
print(f"FireDucks Preprocessing  : {preprocess_fd_time:.2f} sec")
