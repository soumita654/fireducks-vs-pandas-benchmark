!pip install fireducks
import pandas as pd
import fireducks.pandas as pd
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=10_000_000, n_features=20, random_state=42)
columns = [f'feature_{i}' for i in range(20)]

df_pd = pd.DataFrame(X, columns=columns)
df_pd['target'] = y

# Save as Parquet (used for both tools)
df_pd.to_parquet('benchmark_dataset.parquet')
