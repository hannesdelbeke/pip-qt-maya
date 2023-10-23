# Maya Pip Qt plugin

A Maya plugin to add [pip-qt](https://github.com/hannesdelbeke/pip-qt) to the menu. 

## Install
1. install dependencies to `Documents/Maya/scripts`
```
python -m pip install pip-qt --target "C:/Users/%username%/Documents/Maya/scripts"
```
2. install plugin (from repo) without dependencies to `Documents/Maya/plug-ins`
```
python -m pip --no-dependencies install https://github.com/hannesdelbeke/maya-pip-qt/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins"
```
