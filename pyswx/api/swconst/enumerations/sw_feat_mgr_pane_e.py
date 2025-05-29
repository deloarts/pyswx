"""
swFeatMgrPane_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html
"""

from enum import IntEnum


class SWFeatMgrPaneE(IntEnum):
    """Available panes and states."""

    SW_FEAT_MGR_PANE_TOP = 0  # Top pane
    SW_FEAT_MGR_PANE_BOTTOM = 1  # Bottom pane
    SW_FEAT_MGR_PANE_TOP_HIDDEN = 2  # Top pane hidden
    SW_FEAT_MGR_PANE_BOTTOM_HIDDEN = 3  # Bottom pane hidden
    SW_FEAT_MGR_PANE_FLYOUT = 4  # Flyout pane
