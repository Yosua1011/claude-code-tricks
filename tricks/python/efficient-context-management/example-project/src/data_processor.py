"""
Data processing utilities for cleaning and transforming raw data.
"""
import pandas as pd
from pathlib import Path
from typing import Optional


class DataProcessor:
    """Process raw data files into clean datasets."""

    def __init__(self, data_dir: str):
        """
        Initialize the data processor.

        Args:
            data_dir: Directory containing raw data files
        """
        self.data_dir = Path(data_dir)
        self.processed_data: Optional[pd.DataFrame] = None

    def load_data(self, filename: str) -> pd.DataFrame:
        """Load a CSV file from the data directory."""
        file_path = self.data_dir / filename
        return pd.read_csv(file_path)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the dataset by removing nulls and duplicates.

        Args:
            df: Raw dataframe

        Returns:
            Cleaned dataframe
        """
        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing values
        df = df.fillna(df.mean(numeric_only=True))

        return df

    def process(self) -> pd.DataFrame:
        """Run the full processing pipeline."""
        # Load raw data
        df = self.load_data("input.csv")

        # Clean data
        df = self.clean_data(df)

        # Store processed data
        self.processed_data = df

        return df
