"""
swCustomInfoAddResult_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoAddResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomInfoAddResultE(IntEnum):
    """Result codes when adding custom properties."""

    SW_CUSTOM_INFO_ADD_RESULT_ADDED_OR_CHANGED = 0  # Success
    SW_CUSTOM_INFO_ADD_RESULT_GENERIC_FAIL = 1  # Failed to add the custom property
    SW_CUSTOM_INFO_ADD_RESULT_MISMATCH_EXISTING_TYPE = (
        2  # Existing property with same name has different type
    )
    SW_CUSTOM_INFO_ADD_RESULT_MISMATCH_SPECIFIED_TYPE = (
        3  # Value doesn't match the specified type
    )
