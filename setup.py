import os
from setuptools import setup
# from nvpy import nvpy

setup(
    name = "PyToDeb",
    version = "1.0",
    author = "Varun Gujarathi",
    author_email = "v.gujarathi777@gmail.com",
    description = "Demo of packaging a Python script as DEB",
    license = "MIT",
    url = "https://github.com/varungujarathi9/Python-to-Deb",
    packages=['PyToDeb'],
    entry_points = {
        'console_scripts' : ['PyToDeb = PyToDeb.PyToDeb:main']
    },
    data_files = [
        ('share/applications/', ['PyToDeb.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)

# install_requires=[
#         'utm',
#         'SQLAlchemy>=0.6',
#         'BrokenPackage>=0.7,<1.0',
#     ],