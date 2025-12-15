from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent

requirements = (BASE_DIR / "requirements.txt").read_text().splitlines()

setup(
    name="demo_venv_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "demo-app=demo_app.main:main"
        ]
    }
)
