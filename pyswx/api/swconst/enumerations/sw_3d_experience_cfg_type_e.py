"""
sw3DExperienceCfgType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceCfgType_e.html

Status: 🟢
"""

from enum import IntEnum


class SW3DExperienceCfgTypeE(IntEnum):
    """Enumeration for types of configurations viewed in SOLIDWORKS Connected."""

    SW_NOT_3DEXPERIENCE_TYPE = 0  # Default SOLIDWORKS configuration
    SW_PHYSICAL_PRODUCT = 1  # Family member
    SW_REPRESENTATION = (
        2  # Break view, section view, or other representation of the physical product
    )
