"""
swDocumentTypes_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html

Status: 🟢
"""

from enum import IntEnum


class SWDocumentTypesE(IntEnum):
    """Document types."""

    SW_DOC_NONE = 0  # No document
    SW_DOC_PART = 1  # Part document
    SW_DOC_ASSEMBLY = 2  # Assembly document
    SW_DOC_DRAWING = 3  # Drawing document
    SW_DOC_SDM = 4  # SDM document
    SW_DOC_LAYOUT = 5  # Layout document
    SW_DOC_IMPORTED_PART = 6  # Imported part (Multi-CAD)
    SW_DOC_IMPORTED_ASSEMBLY = 7  # Imported assembly (Multi-CAD)
