"""
swGeometryToSave_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometryToSave_e.html

Status: 🟢
"""

from enum import IntEnum


class SWGeometryToSaveE(IntEnum):
    """Geometry to save options for IAdvancedSaveAsOptions::GeometryToSave."""

    SW_GEOMETRY_TO_SAVE_ALL_COMPONENTS = 0  # Save all components
    SW_GEOMETRY_TO_SAVE_EXTERIOR_FACES = 1  # Save only exterior faces
    SW_GEOMETRY_TO_SAVE_INCLUDE_SPECIFIC_COMPONENTS = 2  # Include specific components
