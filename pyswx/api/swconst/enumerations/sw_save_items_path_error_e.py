"""
swSaveItemsPathError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveItemsPathError_e.html
"""

from enum import IntEnum


class SWSaveItemsPathErrorE(IntEnum):
    """Error return codes for ModifyItemsNameAndPath."""

    SW_SAVE_ITEMS_PATH_ERROR_SUCCEEDED = 0  # Operation succeeded
    SW_SAVE_ITEMS_PATH_ERROR_ARRAY_SIZE_NOT_MATCHING = (
        1  # Input arrays must be the same size
    )
    SW_SAVE_ITEMS_PATH_ERROR_INVALID_PATH = 2  # Invalid path or no write access
    SW_SAVE_ITEMS_PATH_ERROR_WRONG_COMPONENT_NAME = 3  # Unsupported component name
