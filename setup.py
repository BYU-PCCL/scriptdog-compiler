from setuptools import setup, find_packages

setup(
    name="scriptdog-compiler",
    version="0.1",
    packages=find_packages(),
    scripts=["bin/scriptdog-compile"]
)
