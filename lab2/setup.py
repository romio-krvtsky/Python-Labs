# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="finalparser",
    version="5.2.3",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/romio-krvtsky?tab=repositories",
    author="Roman krivetskiy",
    author_email="romik.krivetskiy@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,


)