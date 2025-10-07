"""
swDwgPaperSizes_e Enumeration

Defines standard and user-defined drawing paper sizes.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html

Status: 🟢
"""

from enum import IntEnum


class SWDwgPaperSizesE(IntEnum):
    """Drawing paper sizes."""

    SW_DWG_PAPER_ASIZE = 0  # ANSI A (landscape)
    SW_DWG_PAPER_ASIZE_VERTICAL = 1  # ANSI A (portrait)
    SW_DWG_PAPER_BSIZE = 2  # ANSI B
    SW_DWG_PAPER_CSIZE = 3  # ANSI C
    SW_DWG_PAPER_DSIZE = 4  # ANSI D
    SW_DWG_PAPER_ESIZE = 5  # ANSI E
    SW_DWG_PAPER_A4SIZE = 6  # ISO A4 (landscape)
    SW_DWG_PAPER_A4SIZE_VERTICAL = 7  # ISO A4 (portrait)
    SW_DWG_PAPER_A3SIZE = 8  # ISO A3
    SW_DWG_PAPER_A2SIZE = 9  # ISO A2
    SW_DWG_PAPER_A1SIZE = 10  # ISO A1
    SW_DWG_PAPER_A0SIZE = 11  # ISO A0
    SW_DWG_PAPERS_USER_DEFINED = 12  # User-defined paper size
