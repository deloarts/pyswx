"""
swAddToRecentDocumentList_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddToRecentDocumentList_e.html

Status: 🟢
"""

from enum import IntEnum


class SWAddToRecentDocumentListE(IntEnum):
    """Enumeration for actions related to adding documents to the recent documents list in SolidWorks."""

    SW_ADD_TO_RECENT_DOCUMENT_LIST_DEFAULT = 0  #: Default OpenDoc7 action: if a configuration is specified, the document is not added to the Recent Documents list; if a configuration is not specified, the document is added.
    SW_ADD_TO_RECENT_DOCUMENT_LIST_ADD = (
        1  #: Always add the document to the Recent Documents list.
    )
    SW_ADD_TO_RECENT_DOCUMENT_LIST_DONT_ADD = (
        2  #: Never add the document to the Recent Documents list.
    )
