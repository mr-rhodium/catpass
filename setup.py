import os
from setuptools import setup

VERSION = "0.0.1"


def description():
    """
    Reads the content of the README.md
    """
    file_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(file_path, "r") as fh:
        return fh.read()


setup(
    name="cat-pass",
    description="The console utility for generate strong passwords",
    long_description=description(),
    long_discription_content_type="text/markdown",
    version=VERSION,
    url="https://github.com/mr-rhodium/catpass.git",
    author="Taras Nytiaha",
    author_email="taras.nytiaha@gmail.com",
    entry_points={
        "console_scripts": [
            "catp = cat_password.gen:main",
            "catpass = cat_password.gen:main",
            "cat-pass = cat_password.gen:main",
        ]
    },
)
