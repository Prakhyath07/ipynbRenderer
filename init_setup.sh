echo [$(date)]: "START"

echo [$(date)]: "creating conda env with python 3.8"
conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activate env"
source activate ./env

echo [$(date)]: "installing dev requirments"
pip install -r requirements_dev.txt

echo [$(date)]: "DONE"