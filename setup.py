
import os
import sys
from setuptools import setup

if sys.version_info[:2] < (3, 7):
    error = (
        "PyTropical 0.0.1+ requires Python 3.7 or later (%d.%d detected). \n"
        #"For Python 2.7, please install version x using: \n"
        #"$ pip install 'pytropical==x'" % sys.version_info[:2]
    )
    sys.stderr.write(error + "\n")
    sys.exit(1)

with open("pytropical/__init__.py") as fid:
    for line in fid:
        if line.startswith("__version__"):
            version = line.strip().split()[-1][1:-1]
            break

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering",
]


setup(
name='pytropical',
version='0.0.1',
description='PyTropical is a Python package for tropical mathematics.',
url='https://github.com/heitorbaldo/pytropical',
author='Heitor Baldo',
author_email='heitorbaldo@gmail.com',
maintainer = 'PyTropical Developers',
keywords=['Max-Plus Algebra', 'Min-Plus Algebra', 'Tropical Algebra'],
platforms = ["Linux", "Mac OSX", "Windows", "Unix"],
classifiers=classifiers,
license='MIT License',
install_requires=['numpy', 'math'],
packages=['pytropical'],
zip_safe=False
)
