"""
Tests for the DataProcessor class.
"""
import pytest
import pandas as pd
from src.data_processor import DataProcessor


class TestDataProcessor:
    """Test suite for DataProcessor."""

    def test_initialization(self):
        """Test processor initialization."""
        processor = DataProcessor("data/raw")
        assert processor.data_dir.name == "raw"

    def test_clean_data_removes_duplicates(self):
        """Test that clean_data removes duplicate rows."""
        processor = DataProcessor("data/raw")

        # Create test dataframe with duplicates
        df = pd.DataFrame({
            "col1": [1, 2, 2, 3],
            "col2": [4, 5, 5, 6]
        })

        cleaned = processor.clean_data(df)
        assert len(cleaned) == 3  # One duplicate removed

    def test_clean_data_fills_nulls(self):
        """Test that clean_data fills null values."""
        processor = DataProcessor("data/raw")

        # Create test dataframe with nulls
        df = pd.DataFrame({
            "col1": [1, 2, None, 4],
            "col2": [5, None, 7, 8]
        })

        cleaned = processor.clean_data(df)
        assert cleaned.isnull().sum().sum() == 0  # No nulls remain
