"""
swCustomLinkSetResult_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomLinkSetResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCustomLinkSetResultE(IntEnum):
    """Error codes when linking and unlinking custom properties."""

    SW_CUSTOM_LINK_SET_RESULT_OK = 0  # Success
    SW_CUSTOM_LINK_SET_RESULT_NOT_PRESENT = 1  # Custom property does not exist
    SW_CUSTOM_LINK_SET_RESULT_LEGACY = 2  # Legacy properties cannot be linked/unlinked
    SW_CUSTOM_LINK_SET_RESULT_USER_PROP = (
        3  # User-defined properties cannot be linked/unlinked
    )
