import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds


MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase
MENU_LABEL = "Tools"  # no spaces in names, use CamelCase
MENU_ENTRY_LABEL = "Python package manager"

MENU_PARENT = "MayaWindow"  # do not change

_pip_qt_widget = None

def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0

# =============================== Menu ===========================================
def show(*args):
    import pip_qt
    
    # hookup interpeter to prevent freezing during py-pip install
    if not sys.executable.endswith("maya.exe"):
        raise Exception(sys.executable, "doesn't end in maya.exe, can't hookup python interpreter")
    py_pip.python_interpreter = sys.executable.replace("maya.exe", "mayapy.exe")
    
    global _pip_qt_widget
    _pip_qt_widget = pip_qt.show()


def loadMenu():
    if not cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    cmds.menuItem(label=MENU_ENTRY_LABEL, command=show, parent=f"{MENU_PARENT}|{MENU_NAME}")  


def unloadMenuItem():
    if cmds.menu(MENU_NAME, exists=True):
        menu_item_long_name = MENU_NAME + "|" + MENU_ENTRY_LABEL
        # Check if the menu item exists; if it does, delete it
        if cmds.menuItem(menu_item_long_name, exists=True):
            cmds.deleteUI(menu_item_long_name, menuItem=True)
        # Check if the menu is now empty; if it is, delete the menu
        if not cmds.menu(MENU_NAME, query=True, itemArray=True):
            cmds.deleteUI(MENU_NAME, menu=True)


# =============================== Plugin (un)load ===========================================
def initializePlugin(plugin):
    loadMenu()


def uninitializePlugin(plugin):
    unloadMenuItem()
