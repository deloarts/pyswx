# Filename: sw_body_type_e.py

"""
swBodyType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html
"""

from enum import IntEnum


class SWBodyTypeE(IntEnum):
    """Defines valid types of bodies in SolidWorks models."""

    SW_SOLID_BODY = 0  # Solid body
    SW_SHEET_BODY = 1  # Sheet body
    SW_WIRE_BODY = 2  # Wire body
    SW_MINIMUM_BODY = 3  # Point body
    SW_GENERAL_BODY = 4  # General, nonmanifold body
    SW_EMPTY_BODY = 5  # NULL body
    SW_MESH_BODY = 6  # Mesh body
    SW_GRAPHICS_BODY = 7  # Graphics body
    SW_ALL_BODIES = -1  # All solid and sheet bodies
