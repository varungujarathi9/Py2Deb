# Python-to-Deb

This repo contains steps and sample to convert a python package to deb package which can be install on any debian-supported OS
___

## Steps

### 1. First install stdeb

```
sudo apt install python-stdeb
pip3 install stem stdeb
```

### 2. The folder structure should be same as

```
This_Repo/
    README.md
    setup.py
    PyToDeb/
        __init__.py
        PyToDeb.py
```

### 3. Now copy the `setup.py` from [here](setup.py)

Change the necessary fields in setup.py

### 4. Now copy the `PyToDeb.py` from [here](PyToDeb/PyToDeb.py)

### 5. Now run the command

```
python setup.py --command-packages=stdeb.command bdist_deb
```

### 6. A .deb file would be created in deb_dist folder

Run the .deb file to install the software
