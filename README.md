# Maya Pip Qt plugin

A Maya plugin to add [pip-qt](https://github.com/hannesdelbeke/pip-qt) to the menu. 

## Install
### manual install
- copy plugin file to a Maya plugins folder, e.g. `C:\Users\%username%\Documents\maya\2022\plug-ins`
- pip install dependencies to a Maya target folder, e.g. `C:\Users\%username%\Documents\maya\2022\scripts`

install dependencies
```
python -m pip install pip-qt --target "C:/Users/%username%/Documents/Maya/scripts"
```
install plugin without dependencies
```
python -m pip --no-dependencies install https://github.com/hannesdelbeke/maya-pip-qt/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins"
```
