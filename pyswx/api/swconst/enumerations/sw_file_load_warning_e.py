"""
swFileLoadWarning_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html
"""

from enum import IntEnum


class SWFileLoadWarningE(IntEnum):
    SW_FILELOADWARNING_ID_MISMATCH = (
        1  #: Internal ID mismatch with referencing document
    )
    SW_FILELOADWARNING_SHARING_VIOLATION = 4  #: Document is being used by another user
    SW_FILELOADWARNING_READ_ONLY = 2  #: Document is read-only
    SW_FILELOADWARNING_NEEDS_REGEN = 32  #: Document needs to be rebuilt
    SW_FILELOADWARNING_MODEL_OUT_OF_DATE = (
        8192  #: Drawing views are out of date with external models
    )
    SW_FILELOADWARNING_SHEET_SCALE_UPDATE = (
        16  #: Sheet scale applied to sketch entities
    )
    SW_FILELOADWARNING_DRAWING_ANSI_UPDATE = (
        8  #: Radial dimension arrows displayed outside
    )
    SW_FILELOADWARNING_REVOLVE_DIM_TOLERANCE = (
        4096  #: Tolerances of revolved feature dimensions not synchronized
    )
    SW_FILELOADWARNING_BASE_PART_NOT_LOADED = (
        64  #: Document defined in context of another existing document not loaded
    )
    SW_FILELOADWARNING_ALREADY_OPEN = 128  #: Document is already open
    SW_FILELOADWARNING_AUTOMATIC_REPAIR = (
        262144  #: Non-critical data in the document was automatically repaired
    )
    SW_FILELOADWARNING_CRITICAL_DATA_REPAIR = (
        524288  #: Critical data in the document was automatically repaired
    )
    SW_FILELOADWARNING_DIMENSIONS_REFERENCED_INCORRECTLY_TO_MODELS = (
        16384  #: Dimensions referenced incorrectly to models
    )
    SW_FILELOADWARNING_DRAWING_SF_SYMBOL_CONVERT = (
        2048  #: Prompt to convert drawing's surface finish symbols
    )
    SW_FILELOADWARNING_DRAWINGS_ONLY_RAPIDDRAFT = (
        256  #: Only RapidDraft format conversion can take place
    )
    SW_FILELOADWARNING_INVISIBLE_DOC_LINKED_DESIGN_TABLE_UPDATE_FAIL = (
        65536  #: Invisible document with linked design table update failed
    )
    SW_FILELOADWARNING_MISSING_DESIGN_TABLE = 131072  #: Design table is missing
    SW_FILELOADWARNING_MISSING_EXTERNAL_REFERENCES = (
        1048576  #: One or more references are missing
    )
    SW_FILELOADWARNING_COMPONENT_MISSING_REFERENCED_CONFIG = (
        32768  #: Component missing referenced configuration
    )
    SW_FILELOADWARNING_VIEW_MISSING_REFERENCED_CONFIG = (
        1024  #: Drawing view referencing missing configuration
    )
    SW_FILELOADWARNING_VIEW_ONLY_RESTRICTIONS = (
        512  #: Document is view-only with non-default configuration set
    )
