#!/bin/bash

# Install any dependencies you have in this shell script.

# E.g. pip install tensorflow

pip install --ignore-installed evalml
pip install WordCloud nltk flaml nbconvert==5.6.1 jupyter-client==5.3.5
conda install python-graphviz -y