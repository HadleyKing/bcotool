#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    setup script for a pip package
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-HadleyKing", # Replace with your own username
    version="0.0.1",
    author="Hadley King",
    author_email="Hadley_King@gwu.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
