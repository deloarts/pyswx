"""
ISwAddin Interface Members

Reference:
https://help.solidworks.com/2024/english/api/swpublishedapi/solidworks.interop.swpublished~solidworks.interop.swpublished.iswaddin_members.html

Status: 🟢
"""

from pythoncom import VT_DISPATCH
from pythoncom import VT_I4
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks


class ISwAddin(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"ISwAddin({self.com_object})"

    def connect_to_sw(self, this_sw: ISldWorks, cookie: int) -> bool:
        """
        Calls this method when the add-in is loaded.

        Reference:
        https://help.solidworks.com/2024/english/api/swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~ConnectToSW.html
        """
        in_this_sw = VARIANT(VT_DISPATCH, this_sw)
        in_cookie = VARIANT(VT_I4, cookie)

        com_object = self.com_object.ConnectToSW(in_this_sw, in_cookie)
        return bool(com_object)

    def disconnect_from_sw(self) -> bool:
        """
        Calls this method when SOLIDWORKS is about to be destroyed.

        Reference:
        https://help.solidworks.com/2024/english/api/swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddin~DisconnectFromSW.html
        """
        com_object = self.com_object.DisconnectFromSW
        return bool(com_object)
