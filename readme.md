# create env with conda
conda create --name deep python=3.10

# activate env
conda activate deep

# exit env
conda deactivate

# show list env
conda env list

# delete env
conda env remove --name deep

# install lib opencv
pip install opencv-python

# show file install already
pip show opencv-pyhthon

# show all lib
pip list