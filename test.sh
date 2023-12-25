#!/bin/bash
#source ../miniconda3/etc/profile.d/conda.sh
sudo apt-get update
sudo apt-get install libgl1-mesa-glx
pip install PyQt5
pip install orange3
python -m Orange.canvas
