# Maya Pip Qt plugin

A Maya plugin to add [pip-qt](https://github.com/hannesdelbeke/pip-qt) to the menu.  
![image](https://github.com/hannesdelbeke/maya-pip-qt/assets/3758308/26dd3524-9589-4cab-9ff6-3745577ea262)

## Install
To install for a specific Maya version only, e.g. 2022, replace `Maya/scripts` with `Maya/2022/scripts`
1. install dependencies to `Documents/Maya/scripts`
```
python -m pip install pip-qt --target "C:/Users/%username%/Documents/Maya/scripts"
```
2. install plugin (from repo) without dependencies to `Documents/Maya/plug-ins`
```
python -m pip --no-dependencies install https://github.com/hannesdelbeke/maya-pip-qt/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins"
```
3. Open the plugin manager, and load the plugin.
4. A new menu should show `Tools`, open the window from here.
