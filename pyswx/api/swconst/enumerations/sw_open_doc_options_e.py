"""
swOpenDocOptions_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOpenDocOptions_e.html?id=9bba448a555b46fc8ee9e9abae302e42#Pg0
"""

from enum import IntEnum


class SWOpenDocOptionsE(IntEnum):
    SW_OPEN_DOC_SILENT = 1  #: Open document silently
    SW_OPEN_DOC_READ_ONLY = 2  #: Open document read-only
    SW_OPEN_DOC_VIEW_ONLY = (
        4  #: Open document in Large Design Review mode (assemblies only)
    )
    SW_OPEN_DOC_LOAD_MODEL = (
        16  #: Load detached model upon opening document (drawings only)
    )
    SW_OPEN_DOC_OPEN_DETAILING_MODE = 1024  #: Open document in detailing mode
    SW_OPEN_DOC_LOAD_LIGHTWEIGHT = 128  #: Open assembly document as lightweight
    SW_OPEN_DOC_LOAD_EXTERNAL_REFERENCES_IN_MEMORY = (
        512  #: Open external references in memory only
    )
    SW_OPEN_DOC_OVERRIDE_DEFAULT_LOAD_LIGHTWEIGHT = 64  #: Override default setting whether to open an assembly document as lightweight
    SW_OPEN_DOC_LDR_EDIT_ASSEMBLY = 2048  #: Open in Large Design Review (resolved) mode with edit assembly enabled; use in combination with SW_OPEN_DOC_VIEW_ONLY
    SW_OPEN_DOC_SPEEDPAK = 4096  #: Open document using the SpeedPak option
    SW_OPEN_DOC_RAPID_DRAFT = 8  #: Convert document to Detached format (drawings only)
    SW_OPEN_DOC_ADVANCED_CONFIG = 8192  #: Open assembly using an advanced configuration
    SW_OPEN_DOC_AUTO_MISSING_CONFIG = 32  #: Obsolete; do not use
