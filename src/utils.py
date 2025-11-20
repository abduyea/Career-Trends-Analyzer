from __future__ import annotations

from typing import Dict

import pandas as pd

try:
    from IPython.display import display
except ImportError:
    display = print  # fallback


def peek(df: pd.DataFrame, n: int = 5) -> None:
    # shape + preview
    print(df.shape)
    display(df.head(n))


def missing_summary(df: pd.DataFrame, n: int = 20) -> None:
    # columns with most missing values
    miss = df.isna().sum().sort_values(ascending=False)
    print(miss.head(n))


def summarize_tables(tables: Dict[str, pd.DataFrame]) -> None:
    # shape of each table in dict
    for name, frame in tables.items():
        print(f"{name}: {frame.shape}")
