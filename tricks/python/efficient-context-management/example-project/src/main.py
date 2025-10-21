"""
Main application module for the ML data processing pipeline.
"""
import logging
from pathlib import Path

from src.data_processor import DataProcessor
from src.model import MLModel
from src.utils import setup_logging


def main():
    """Run the main application pipeline."""
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting ML pipeline...")

    # Initialize components
    processor = DataProcessor(data_dir="data/raw")
    model = MLModel(model_path="models/trained_model.pkl")

    # Process data
    logger.info("Processing data...")
    processed_data = processor.process()

    # Train or predict
    logger.info("Running model inference...")
    results = model.predict(processed_data)

    logger.info(f"Pipeline complete. Processed {len(results)} predictions.")
    return results


if __name__ == "__main__":
    main()
