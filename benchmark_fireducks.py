# Load with FireDucks
import time # Import the time module here
import fireducks.pandas as pd  # Import fireducks.pandas as pd here

start = time.time()
df_fd = pd.read_parquet('benchmark_dataset.parquet')
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
