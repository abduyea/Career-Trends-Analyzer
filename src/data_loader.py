# Drive mount + loading + master join
from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

from .config import RAW_DIR  # relative import from src package

try:
    from google.colab import drive
except ImportError:
    drive = None


def mount_drive() -> None:
    # mount only in Colab
    if drive:
        drive.mount("/content/drive", force_remount=False)


def _load_csv(path: Path) -> pd.DataFrame:
    # load single csv
    if not path.is_file():
        raise FileNotFoundError(f"CSV not found: {path}")
    return pd.read_csv(path)


def load_postings() -> pd.DataFrame:
    # postings.csv
    return _load_csv(RAW_DIR / "postings.csv")


def _load_folder(name: str) -> Dict[str, pd.DataFrame]:
    # load all csvs in raw/<name>
    folder = RAW_DIR / name
    if not folder.is_dir():
        return {}
    return {p.stem: pd.read_csv(p) for p in folder.glob("*.csv")}


def load_companies() -> Dict[str, pd.DataFrame]:
    # raw/companies
    return _load_folder("companies")


def load_jobs() -> Dict[str, pd.DataFrame]:
    # raw/jobs
    return _load_folder("jobs")


def load_mappings() -> Dict[str, pd.DataFrame]:
    # raw/mappings
    return _load_folder("mappings")


def build_master(
    postings: pd.DataFrame,
    companies: Dict[str, pd.DataFrame],
    jobs: Dict[str, pd.DataFrame],
    mappings: Dict[str, pd.DataFrame],
) -> pd.DataFrame:
    # safe merges
    df = postings.copy()

    c = companies.get("companies")
    if c is not None and "company_id" in df and "company_id" in c:
        df = df.merge(c, on="company_id", how="left", suffixes=("", "_company"))

    s = jobs.get("salaries")
    if s is not None and "job_id" in df and "job_id" in s:
        df = df.merge(s, on="job_id", how="left", suffixes=("", "_salary"))

    return df
