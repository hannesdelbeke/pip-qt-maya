import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds


MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase
MENU_LABEL = "Tools"  # spaces are fine in labels
MENU_ENTRY_LABEL = "My cool tool"

MENU_PARENT = "MayaWindow"  # do not change


def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0

# =============================== Menu ===========================================
def show(*args):
    # TODO import our custom module
    print("hello")


def loadMenu():
    if not cmds.menu(MENU_NAME, exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    cmds.menuItem(label=MENU_ENTRY_LABEL, command=show)  # , parent=MENU_NAME)  


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
