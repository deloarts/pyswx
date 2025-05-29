"""
swSaveAsOptions_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html
"""

from enum import IntEnum


class SWSaveAsOptionsE(IntEnum):
    SW_SAVE_AS_OPTIONS_SILENT = 1
    SW_SAVE_AS_OPTIONS_COPY = 2  # Save the document as a copy and continue editing
    SW_SAVE_AS_OPTIONS_SAVE_REFERENCED = 4  # Save all referenced components
    SW_SAVE_AS_OPTIONS_AVOID_REBUILD_ON_SAVE = 8
    SW_SAVE_AS_OPTIONS_UPDATE_INACTIVE_VIEWS = (
        16  # Only applies to multi-sheet drawings
    )
    SW_SAVE_AS_OPTIONS_OVERRIDE_SAVE_EMODEL = (
        32  # Overrides the Save eDrawings data setting
    )
    SW_SAVE_AS_OPTIONS_IGNORE_BIOGRAPHY = (
        256  # Prune revision history to current file name
    )
    SW_SAVE_AS_OPTIONS_COPY_AND_OPEN = 512  # Save as copy and open
    SW_SAVE_AS_OPTIONS_INCLUDE_VIRTUAL_SUB_ASM_COMPS = (
        1024  # Save components in virtual subassemblies
    )
    SW_SAVE_AS_OPTIONS_EXPORT_TO_2D_PDF_FROM_INSPECTION = (
        2048  # Export drawing sheets from Inspection to 2D PDF
    )
