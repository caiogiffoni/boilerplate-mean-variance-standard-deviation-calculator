import numpy as np
import pandas as pd


def calculate(arr):
  if len(arr) != 9: raise ValueError('List must contain nine numbers.')
  df = pd.DataFrame([arr[0:3], arr[3:6], arr[6:]])
  return {
    "mean": [df.mean().tolist(),
             df.mean(axis=1).tolist(),
             df.stack().mean()],
    "variance": [
      df.var(ddof=0).to_list(),
      df.var(ddof=0, axis=1).tolist(),
      df.stack().var(ddof=0)
    ],
    'standard deviation': [
      df.std(ddof=0).tolist(),
      df.std(ddof=0, axis=1).tolist(),
      df.stack().std(ddof=0)
    ],
    'max': [df.max().tolist(),
            df.max(axis=1).tolist(),
            df.stack().max()],
    'min': [df.min().tolist(),
            df.min(axis=1).tolist(),
            df.stack().min()],
    'sum': [df.sum().tolist(),
            df.sum(axis=1).tolist(),
            df.stack().sum()]
  }
