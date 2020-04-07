import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="data_enhancer_v2",
    version="2.0",
    author="Ridhima, Vipul, Praneet",
    description="An End-To-End Question Answering System for Data Enhancer",
    install_requires=read("requirements.txt").split(),
)