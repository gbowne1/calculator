from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "calc=calculator.cli:main",
        ],
    },
    python_requires=">=3.0",
)
