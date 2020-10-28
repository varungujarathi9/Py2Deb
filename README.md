# Python-to-Deb

This repo contains steps and sample to convert a python package to deb package which can be install on any debian-supported OS
___
## Steps
### 1. First install python-stdeb

```sudo apt install python-stdeb```

### 2. The folder structure should be same as
```
ThisRepo/
    README.md
    PyToDeb/
        setup.py
        PyToDeb/
            __init__.py
            PyToDeb.py
```

### 3. Now copy the `setup.py` from [here](PyToDeb/setup.py)
Copy PyToDeb.py
___
pip3 install stem stdeb

