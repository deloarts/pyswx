"""
swCustomInfoSetResult_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoSetResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomInfoSetResultE(IntEnum):
    """Result codes when setting custom properties."""

    SW_CUSTOM_INFO_SET_RESULT_OK = 0  # Success
    SW_CUSTOM_INFO_SET_RESULT_NOT_PRESENT = 1  # Property does not exist
    SW_CUSTOM_INFO_SET_RESULT_TYPE_MISMATCH = 2  # Incorrect value type
    SW_CUSTOM_INFO_SET_RESULT_LINKED_PROP = (
        3  # Property is linked and cannot be modified
    )
