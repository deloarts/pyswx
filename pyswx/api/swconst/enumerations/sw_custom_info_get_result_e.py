"""
swCustomInfoGetResult_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoGetResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomInfoGetResultE(IntEnum):
    """Result codes when getting custom properties."""

    SW_CUSTOM_INFO_GET_RESULT_CACHED_VALUE = 0  # Cached value was returned
    SW_CUSTOM_INFO_GET_RESULT_NOT_PRESENT = 1  # Custom property does not exist
    SW_CUSTOM_INFO_GET_RESULT_RESOLVED_VALUE = 2  # Resolved value was returned
