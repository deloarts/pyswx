"""
swCustomInfoDeleteResult_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoDeleteResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomInfoDeleteResultE(IntEnum):
    """Result codes when deleting custom properties."""

    SW_CUSTOM_INFO_DELETE_RESULT_OK = 0  # Success
    SW_CUSTOM_INFO_DELETE_RESULT_NOT_PRESENT = 1  # Property does not exist
    SW_CUSTOM_INFO_DELETE_RESULT_LINKED_PROP = (
        2  # Property is linked and cannot be deleted
    )
