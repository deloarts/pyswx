"""
IDrawingDoc Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html

Status: 🔴
"""

from pathlib import Path

from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_DISPATCH
from pythoncom import VT_I4
from pythoncom import VT_R8
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_view import IView


class IDrawingDoc(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IDrawingDoc({self.com_object})"

    def create_draw_view_from_model_view_3(
        self, model_name: Path, view_name: str, loc_x: float, loc_y: float, loc_z: float
    ) -> IView:
        """
        Creates a drawing view on the current drawing sheet using the specified model view.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.idrawingdoc~createdrawviewfrommodelview3.html
        """
        in_model_name = VARIANT(VT_BSTR, str(model_name))
        in_view_name = VARIANT(VT_BSTR, view_name)
        in_loc_x = VARIANT(VT_R8, loc_x)
        in_loc_y = VARIANT(VT_R8, loc_y)
        in_loc_z = VARIANT(VT_R8, loc_z)

        com_object = self.com_object.CreateDrawViewFromModelView3(
            in_model_name, in_view_name, in_loc_x, in_loc_y, in_loc_z
        )
        return IView(com_object)
