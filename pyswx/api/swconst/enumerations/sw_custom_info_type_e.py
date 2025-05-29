"""
swCustomInfoType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomInfoTypeE(IntEnum):
    """Custom property types."""

    SW_CUSTOM_INFO_UNKNOWN = 0  # Unknown type
    SW_CUSTOM_INFO_NUMBER = 3  # Number
    SW_CUSTOM_INFO_DOUBLE = 5  # Double
    SW_CUSTOM_INFO_YES_OR_NO = 11  # Yes or No (boolean)
    SW_CUSTOM_INFO_TEXT = 30  # Text
    SW_CUSTOM_INFO_DATE = 64  # Date
