import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhampel", # Replace with your own username
    version="0.1.1",
    author="Py Hampel",
    author_email="pyhampel@gmail.com",
    description="A flexible package to apply Hampel filter to time series data.  Identify outliers and filter time series.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dwervin/pyhampel",
    project_urls={
        "Bug Tracker": "https://github.com/dwervin/pyhampel/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

