"""
IFrame Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html

Status: 🔴
"""

from pathlib import Path
from typing import List

from pythoncom import VT_ARRAY
from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_DECIMAL
from pythoncom import VT_I4
from pythoncom import VT_VARIANT
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWSelectTypeE


class IFrame(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IFrame({self.com_object})"

    @property
    def keep_invisible(self) -> bool:
        """
        Gets or sets whether to keep the SOLIDWORKS frame invisible.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.html
        """
        return bool(self.com_object.KeepInvisible)

    @keep_invisible.setter
    def keep_invisible(self, value: bool) -> None:
        self.com_object.KeepInvisible = value

    @property
    def menu_pinned(self) -> bool:
        """
        Gets or sets whether the SOLIDWORKS main menu is pinned.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~MenuPinned.html
        """
        return bool(self.com_object.MenuPinned)

    @menu_pinned.setter
    def menu_pinned(self, value: bool) -> None:
        self.com_object.MenuPinned = value

    @property
    def model_windows(self) -> bool:
        """
        Gets the client model windows for this frame.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html
        """
        return bool(self.com_object.ModelWindows)

    @model_windows.setter
    def model_windows(self, value: bool) -> None:
        self.com_object.ModelWindows = value

    def add_menu(self, menu: str, position: int) -> bool:
        """
        Adds a menu item.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html
        """
        in_menu = VARIANT(VT_BSTR, menu)
        in_position = VARIANT(VT_I4, position)

        com_object = self.com_object.AddMenu(in_menu, in_position)
        return bool(com_object)

    def add_menu_item2(
        self,
        menu: str,
        item: str,
        position: int,
        callback_func_and_module: str,
        bitmap_file_name: Path,
    ) -> bool:
        """
        Adds a menu item and bitmap or a separator to an existing menu.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html
        """
        in_menu = VARIANT(VT_BSTR, menu)
        in_item = VARIANT(VT_BSTR, item)
        in_position = VARIANT(VT_I4, position)
        in_callback_func_and_module = VARIANT(VT_BSTR, callback_func_and_module)
        in_bitmap_file_name = VARIANT(VT_BSTR, str(bitmap_file_name))

        com_object = self.com_object.AddMenuItem2(
            in_menu,
            in_item,
            in_position,
            in_callback_func_and_module,
            in_bitmap_file_name,
        )
        return bool(com_object)

    def add_menu_popup_icon(
        self,
        doc_type: SWDocumentTypesE,
        select_type: SWSelectTypeE,
        hint_string: str,
        callback_func_and_module: str,
        custom_names: str,
        bitmap_file_path: str,
    ) -> bool:
        """
        Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.html
        """
        in_doc_type = VARIANT(VT_I4, doc_type.value)
        in_select_type = VARIANT(VT_I4, select_type.value)
        in_hint_string = VARIANT(VT_BSTR, hint_string)
        in_callback_func_and_module = VARIANT(VT_BSTR, callback_func_and_module)
        in_custom_names = VARIANT(VT_BSTR, custom_names)
        in_bitmap_file_path = VARIANT(VT_BSTR, str(bitmap_file_path))

        com_object = self.com_object.AddMenuPopupIcon(
            in_doc_type,
            in_select_type,
            in_hint_string,
            in_callback_func_and_module,
            in_custom_names,
            in_bitmap_file_path,
        )
        return bool(com_object)

    def add_menu_popup_icon3(
        self,
        doc_type: SWDocumentTypesE,
        select_type: SWSelectTypeE,
        hint_string: str,
        identifier: int,
        callback_function: str,
        callback_update_function: str,
        custom_names: str,
        image_list: List[Path],
    ) -> bool:
        """
        Adds an icon to a context-sensitive menu of a SOLIDWORKS add-in.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon3.html
        """
        in_doc_type = VARIANT(VT_I4, doc_type.value)
        in_select_type = VARIANT(VT_I4, select_type.value)
        in_hint_string = VARIANT(VT_BSTR, hint_string)
        in_identifier = VARIANT(VT_I4, identifier)
        in_callback_function = VARIANT(VT_BSTR, callback_function)
        in_callback_update_function = VARIANT(VT_BSTR, callback_update_function)
        in_custom_names = VARIANT(VT_BSTR, custom_names)
        in_image_list = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in image_list])

        com_object = self.com_object.AddMenuPopupIcon3(
            in_doc_type,
            in_select_type,
            in_hint_string,
            in_identifier,
            in_callback_function,
            in_callback_update_function,
            in_custom_names,
            in_image_list,
        )
        return bool(com_object)
