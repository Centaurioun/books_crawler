# Automatically created by: shub deploy
from setuptools import find_packages
from setuptools import setup

setup(
    name="project",
    version="1.0",
    packages=find_packages(),
    entry_points={"scrapy": ["settings = books.settings"]},
)
