"""
Utility functions for the application.
"""
import logging
import sys
from pathlib import Path


def setup_logging(level: int = logging.INFO):
    """
    Configure logging for the application.

    Args:
        level: Logging level (default: INFO)
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("app.log"),
        ],
    )


def ensure_dir_exists(path: Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent
