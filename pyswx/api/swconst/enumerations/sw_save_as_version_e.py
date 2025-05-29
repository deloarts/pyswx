"""
swSaveAsVersion_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsVersion_e.html
"""

from enum import IntEnum


class SWSaveAsVersionE(IntEnum):
    SW_SAVE_AS_CURRENT_VERSION = 0
    SW_SAVE_AS_FORMAT_PRO_E = 2
    SW_SAVE_AS_STANDARD_DRAWING = 3
    SW_SAVE_AS_DETACHED_DRAWING = 4
