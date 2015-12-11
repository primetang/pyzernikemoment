import os
from setuptools import setup

setup(
    name="pyzernikemoment",
    version="0.0.1",
    author="Gefu Tang",
    author_email="tanggefu@gmail.com",
    description=("pyzernikemoment is a python module to find the Zernike moments for an N x N binary ROI."),
    long_description=open("README.md").read().strip() if os.path.exists(
        "README.md") else "",
    license="GNU",
    keywords="zernike moment",
    url="https://github.com/primetang/pyzernikemoment",
    packages=['pyzernikemoment'],
    package_dir={'pyzernikemoment': 'src'},
)
