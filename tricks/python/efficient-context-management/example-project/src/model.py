"""
Machine learning model wrapper for predictions.
"""
import pickle
from pathlib import Path
from typing import Any, List
import numpy as np


class MLModel:
    """Wrapper for machine learning model operations."""

    def __init__(self, model_path: str):
        """
        Initialize the ML model.

        Args:
            model_path: Path to the serialized model file
        """
        self.model_path = Path(model_path)
        self.model = None

    def load_model(self):
        """Load the trained model from disk."""
        if self.model_path.exists():
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            raise FileNotFoundError(f"Model not found at {self.model_path}")

    def predict(self, data: Any) -> List[float]:
        """
        Make predictions on the input data.

        Args:
            data: Input data for prediction

        Returns:
            List of predictions
        """
        if self.model is None:
            self.load_model()

        # Simulate predictions
        predictions = self.model.predict(data)
        return predictions.tolist()

    def save_model(self, output_path: str):
        """Save the model to disk."""
        with open(output_path, "wb") as f:
            pickle.dump(self.model, f)
