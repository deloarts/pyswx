"""
swCustomPropertyAddOption_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomPropertyAddOption_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomPropertyAddOptionE(IntEnum):
    """Options when adding custom properties."""

    SW_CUSTOM_PROPERTY_ONLY_IF_NEW = 0  # Add only if the property is new
    SW_CUSTOM_PROPERTY_DELETE_AND_ADD = 1  # Delete existing and add new property
    SW_CUSTOM_PROPERTY_REPLACE_VALUE = 2  # Replace value of existing property
