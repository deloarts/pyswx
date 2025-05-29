"""
swTaskPaneTab_e Enumeration

Reference:
https://help.solidworks.com/2019/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneTab_e.html
"""

from enum import IntEnum


class SWTaskPaneTabE(IntEnum):
    SW_TASK_PANE_TAB_SOLIDWORKS_RESOURCES = 0  # SolidWorks Resources tab
    SW_TASK_PANE_TAB_DESIGN_LIBRARY = 1  # Design Library tab
    SW_TASK_PANE_TAB_FILE_EXPLORER = 2  # File Explorer tab
    SW_TASK_PANE_TAB_VIEW_PALETTE = 3  # View Palette tab
    SW_TASK_PANE_TAB_APPEARANCES = 4  # Appearances, Scenes, and Decals tab
    SW_TASK_PANE_TAB_CUSTOM_PROPERTIES = 5  # Custom Properties tab
    SW_TASK_PANE_TAB_SOLIDWORKS_ADDINS = 6  # SolidWorks Add-Ins tab
