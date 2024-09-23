"""
Utility functions like data loader, logger, etc.
"""
import os
from typing import Any, Dict
import yaml
from rich.progress import track
import pandas as pd


def load_data(folder_path: str) -> pd.DataFrame:
    """
    folder_path: str: Path to the folder containing the data
    """
    full_df = pd.DataFrame()

    for train_data in track(os.listdir(folder_path), description="Loading data"):
        if train_data.endswith('.csv'):
            data = pd.read_csv(f"{folder_path}/{train_data}")
            full_df = pd.concat([full_df, data], axis=0)

    return full_df


def load_yaml(config_path: str) -> Dict[str, Any]:
    """
    load yaml file
    """
    with open(config_path, 'r', encoding='utf-8') as yml_file:
        config = yaml.safe_load(yml_file)

    return config


def date_time_transfer(col: pd.Series) -> pd.Series:
    """
    col: pd.Series -> Date and Time column
    """
    return pd.to_datetime(col).astype(int) // 1e9