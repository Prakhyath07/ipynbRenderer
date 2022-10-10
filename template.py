import os
from pathlib import Path ## to make independent of OS
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s:%(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        break

logging.info(f"creating project by name: {project_name}")

#list of files: 
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"

]
## gitkeep is a dummy file which can be deleted later created
## only since empty folder cant be uploaded to github
## init_setup.sh will help to do all basic envnironment setup
## pypoject.toml as per python packaging documentatin
## tox.ini to help test in different environments

for filepath in list_of_files:
    filepath=Path(filepath) ## to create based on os 
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    ## create file only if it doesnt exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating a new file: {filename} at path {filepath}")
    else:
        logging.info(f"{filename} is already present at path: {filepath}")