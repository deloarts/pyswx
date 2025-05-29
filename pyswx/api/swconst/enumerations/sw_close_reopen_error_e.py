"""
swCloseReopenError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenError_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCloseReopenErrorE(IntEnum):
    """Close and reopen errors."""

    SW_CLOSE_REOPEN_NO_ERROR = 0  # No error
    SW_CLOSE_REOPEN_UNKNOWN_ERROR = 1  # Unknown error
    SW_CLOSE_REOPEN_NO_INPUT_DOC_ERROR = 2  # Input document is null
    SW_CLOSE_REOPEN_OUTPUT_DOC_POINTER_ERROR = 3  # Output document is null
    SW_CLOSE_REOPEN_INVALID_DOC_ERROR = 4  # Document is not a drawing
    SW_CLOSE_REOPEN_CLOSE_DOC_ERROR = 5  # Error occurred during close
    SW_CLOSE_REOPEN_LOAD_GENERIC_ERROR = 6  # Error occurred during reopen
    SW_CLOSE_REOPEN_LOAD_FILE_NOT_FOUND_ERROR = 7  # File path specified does not exist
    SW_CLOSE_REOPEN_LOAD_INVALID_FILE_TYPE_ERROR = 8  # File type is not valid
    SW_CLOSE_REOPEN_LOAD_FUTURE_VERSION_ERROR = 9  # File to reopen is a future version
    SW_CLOSE_REOPEN_LOAD_SAME_TITLE_ALREADY_OPEN_ERROR = (
        10  # File with same title is already open
    )
    SW_CLOSE_REOPEN_LOAD_LIQUID_MACHINE_DOC_ERROR = 11  # LiquidMachine document error
    SW_CLOSE_REOPEN_MODIFIED_ERROR = 12  # Cannot close due to unsaved changes
    SW_CLOSE_REOPEN_LOAD_FILE_PATH_EMPTY_ERROR = 13  # File path is empty
    SW_CLOSE_REOPEN_LOAD_FILE_PATH_NON_DRAWING_ERROR = 14  # File is not a drawing
