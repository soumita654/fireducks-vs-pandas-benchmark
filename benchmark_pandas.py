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
