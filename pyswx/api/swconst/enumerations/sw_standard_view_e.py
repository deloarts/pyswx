# Filename: sw_standard_view_e.py

"""
swStandardViews_e Enumeration

Standard view types.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html

Status: 🟢
"""

from enum import IntEnum


class SWStandardViewsE(IntEnum):
    SW_BACK_VIEW = 2
    SW_BOTTOM_VIEW = 6
    SW_DIMETRIC_VIEW = 9
    SW_FRONT_VIEW = 1
    SW_ISOMETRIC_VIEW = 7
    SW_LEFT_VIEW = 3
    SW_RIGHT_VIEW = 4
    SW_TOP_VIEW = 5
    SW_TRIMETRIC_VIEW = 8
