"""
swFileLoadError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html

Status: 🟢
"""

from enum import IntEnum


class SWFileLoadErrorE(IntEnum):
    """File load errors. Bitmask."""

    SW_GENERIC_ERROR = 1  # Another error was encountered
    SW_FILE_NOT_FOUND_ERROR = 2  # Unable to locate the file; the file is not loaded or the referenced file is suppressed
    SW_INVALID_FILE_TYPE_ERROR = 1024  # File type argument is not valid
    SW_FUTURE_VERSION = 8192  # The document was saved in a future version of SOLIDWORKS
    SW_FILE_WITH_SAME_TITLE_ALREADY_OPEN = (
        65536  # A document with the same name is already open
    )
    SW_LIQUID_MACHINE_DOC = 131072  # File encrypted by Liquid Machines
    SW_LOW_RESOURCES_ERROR = 262144  # File is open and blocked because the system memory is low, or the number of GDI handles has exceeded the allowed maximum
    SW_NO_DISPLAY_DATA = 524288  # File contains no display data
    SW_FILE_REQUIRES_REPAIR_ERROR = (
        2097152  # A document has non-critical custom property data corruption
    )
    SW_FILE_CRITICAL_DATA_REPAIR_ERROR = (
        4194304  # A document has critical data corruption
    )
    SW_ADDIN_INTERRUPT_ERROR = 1048576  # The user attempted to open a file, and then interrupted the open-file routine to open a different file
    SW_APPLICATION_BUSY = 8388608  # File open is blocked when application is busy
    SW_CONNECTED_IS_OFFLINE = 16777216  # Connected is offline
