"""
swFeatMgrPane_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html

Status: 🟢
"""

from enum import Enum


class swFeatMgrPane_e(Enum):
    """
    Available panes and states for the Feature Manager.
    """

    swFeatMgrPaneTop = 0
    swFeatMgrPaneBottom = 1
    swFeatMgrPaneTopHidden = 2
    swFeatMgrPaneBottomHidden = 3
    swFeatMgrPaneFlyout = 4
