"""
swApplicationType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swApplicationType_e.html

Status: 🟢
"""

from enum import IntEnum


class SWApplicationTypeE(IntEnum):
    """Types of SOLIDWORKS application."""

    SW_APPLICATION_TYPE_DESKTOP = 0  # Desktop SOLIDWORKS
    SW_APPLICATION_TYPE_3DEXPERIENCE = 1  # 3DEXPERIENCE SOLIDWORKS
    SW_APPLICATION_TYPE_WITH_CONNECTOR = 2  # SOLIDWORKS with 3DEXPERIENCE connector
