"""
swActivateDocError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html

Status: 🟢
"""

from enum import IntEnum


class SWDocActivateErrorE(IntEnum):
    """Document activation errors. Bitmask."""

    SW_GENERIC_ACTIVATE_ERROR = 1  # Unspecified error; document not activated
    SW_DOC_NEEDS_REBUILD_WARNING = 2  # Activated document needs to be rebuilt
