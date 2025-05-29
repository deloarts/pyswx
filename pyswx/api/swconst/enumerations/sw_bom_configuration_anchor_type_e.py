"""
swBOMConfigurationAnchorType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMConfigurationAnchorType_e.html

Status: 🟢
"""

from enum import IntEnum


class SWBOMConfigurationAnchorTypeE(IntEnum):
    """BOM table configuration anchor types."""

    SW_BOM_CONFIGURATION_ANCHOR_TOP_LEFT = 1  # Upper-left corner
    SW_BOM_CONFIGURATION_ANCHOR_TOP_RIGHT = 2  # Upper-right corner
    SW_BOM_CONFIGURATION_ANCHOR_BOTTOM_LEFT = 3  # Lower-left corner
    SW_BOM_CONFIGURATION_ANCHOR_BOTTOM_RIGHT = 4  # Lower-right corner
