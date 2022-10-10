import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "IPYNBRENDERER"
AUTHOR_USER_NAME = "Prakhyath07"
SRC_REPO = "IPYNBRENDERER"
AUTHOR_EMAIL = "prakhyathb07@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package to render ipynb",
    long_description= long_description,
    url=f"https://github.com//{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker":f"https://github.com//{AUTHOR_USER_NAME}/{REPO_NAME}/issues" 
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src")

)
