"""
swChildComponentInBOMOption_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swChildComponentInBOMOption_e.html

Status: 🟢
"""

from enum import IntEnum


class SWChildComponentInBOMOptionE(IntEnum):
    """Child component BOM display options for assemblies."""

    SW_CHILD_COMPONENT_HIDE = (
        1  # Child components might be listed individually depending on BOM settings
    )
    SW_CHILD_COMPONENT_SHOW = 2  # Subassembly appears as a single item in the BOM
    SW_CHILD_COMPONENT_PROMOTE = (
        3  # Assembly's configuration dissolves in BOM; children promoted one level
    )
