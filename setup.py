from pathlib import Path

from setuptools import find_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs", "mkdocstrings"]

style_packages = ["black", "flake8", "isort"]

# Define our package
setup(
    name="Grant_Guide",
    version=0.1,
    description="Generative AI for grant writing",
    author="Ryan Melvin",
    author_email="rmelvin@uabmc.edu",
    url="https://github.com/UABPeriopAI/Grant_Guide.git",
    python_requires=">=3.10",
    packages=find_packages(),  # only look in directores with __init__.py
    install_requires=[required_packages],
    extras_require={"dev": docs_packages + style_packages, "docs": docs_packages},
)
