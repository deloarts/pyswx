"""
swFileSaveError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html
"""

from enum import IntEnum


class SWFileSaveErrorE(IntEnum):
    SW_GENERIC_SAVE_ERROR = 1
    SW_READ_ONLY_SAVE_ERROR = 2
    SW_FILE_NAME_EMPTY = 4  # File name cannot be empty
    SW_FILE_NAME_CONTAINS_AT_SIGN = 8  # File name cannot contain the at symbol (@)
    SW_FILE_LOCK_ERROR = 16
    SW_FILE_SAVE_FORMAT_NOT_AVAILABLE = 32  # Save As file type is not valid
    SW_FILE_SAVE_AS_DO_NOT_OVERWRITE = 128  # Do not overwrite an existing file
    SW_FILE_SAVE_AS_INVALID_FILE_EXTENSION = 256  # File name extension mismatch
    SW_FILE_SAVE_AS_NO_SELECTION = 512  # Invalid for IModelDocExtension::SaveAs
    SW_FILE_SAVE_AS_NAME_EXCEEDS_MAX_PATH_LENGTH = (
        2048  # File name too long (>255 characters)
    )
    SW_FILE_SAVE_AS_NOT_SUPPORTED = (
        4096  # Save As is not supported or might be incomplete
    )
    SW_FILE_SAVE_REQUIRES_SAVING_REFERENCES = (
        8192  # Renamed components require reference saving
    )
    SW_FILE_SAVE_AS_DETACHED_DRAWINGS_NOT_SUPPORTED = (
        16384  # Detached drawing Save As not supported
    )
    SW_FILE_SAVE_AS_BAD_EDRAWINGS_VERSION = 1024
