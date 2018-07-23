from setuptools import setup, find_packages

setup(
    name="scriptdog-compiler",
    version="0.1",
    packages=find_packages(),
    python_requires='>=3',
    scripts=["bin/scriptdog-compile"]
)
