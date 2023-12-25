#!/bin/bash
#source ../miniconda3/etc/profile.d/conda.sh
conda create -n orange 
conda activate orange
conda install -c conda-forge orange3
python -m Orange.canvas
