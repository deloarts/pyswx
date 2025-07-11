"""
swFileSaveWarning_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html
"""

from enum import IntEnum


class SWFileSaveWarningE(IntEnum):
    SW_FILE_SAVE_WARNING_REBUILD_ERROR = 1
    SW_FILE_SAVE_WARNING_NEEDS_REBUILD = 2
    SW_FILE_SAVE_WARNING_VIEWS_NEED_UPDATE = 4
    SW_FILE_SAVE_WARNING_ANIMATOR_NEED_TO_SOLVE = 8
    SW_FILE_SAVE_WARNING_ANIMATOR_FEATURE_EDITS = 16
    SW_FILE_SAVE_WARNING_EDRWINGS_BAD_SELECTION = 32
    SW_FILE_SAVE_WARNING_ANIMATOR_LIGHT_EDITS = 64
    SW_FILE_SAVE_WARNING_ANIMATOR_CAMERA_VIEWS = 128
    SW_FILE_SAVE_WARNING_ANIMATOR_SECTION_VIEWS = 256
    SW_FILE_SAVE_WARNING_MISSING_OLE_OBJECTS = 512
    SW_FILE_SAVE_WARNING_OPENED_VIEW_ONLY = 1024
    SW_FILE_SAVE_WARNING_XML_INVALID = 2048
