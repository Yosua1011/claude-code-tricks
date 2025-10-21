"""
Setup configuration for the ML pipeline package.
"""
from setuptools import setup, find_packages

setup(
    name="ml-pipeline",
    version="0.1.0",
    description="A machine learning data processing pipeline",
    author="Example Author",
    author_email="author@example.com",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
