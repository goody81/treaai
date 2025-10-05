#!/usr/bin/env python3
"""
Setup script for LuminaAI v2.0
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="luminaai-v2",
    version="2.0.0",
    author="treaai",
    description="LuminaAI v2.0 - Advanced AI System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goody81/treaai",
    py_modules=["luminaai_v2", "utils", "examples"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "luminaai=luminaai_v2:main",
        ],
    },
)
