import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "formalarg",
    version = "0.0.1",
    author = "Emmanuel Hadoux",
    author_email = "emmanuel.hadoux@gmail.com",
    description = ("Library for formal argumentation systems."),
    license = "MIT",
    keywords = "argumentation library artificial intelligence",
    url = "http://packages.python.org/formalarg",
    packages=['formalarg', 'tests'],
    install_requires=["graphviz"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
)