import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pyhampel", # Replace with your own username
    version="0.3.4",
    author="Py Hampel",
    author_email="pyhampel@gmail.com",
    description="A flexible package to apply Hampel filter to time series data.  Identify outliers and filter time series.",
    long_description=README,
    long_description_contet_type="text/markdown",
    url="https://github.com/dwervin/pyhampel",
    project_urls={
        "Bug Tracker": "https://github.com/dwervin/pyhampel/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["pyhampel","pyhampel.src","pyhampel.utils","pyhampel.ingestion","pyhampel.dataviz"],
    python_requires=">=3.7",
)

