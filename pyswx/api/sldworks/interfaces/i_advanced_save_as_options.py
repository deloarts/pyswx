"""
IAdvancedSaveAsOptions Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html

Status: 🟢
"""

from pathlib import Path
from typing import List
from typing import Tuple

from pythoncom import VT_ARRAY
from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_I4
from pythoncom import VT_VARIANT
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWGeometryToSaveE
from pyswx.api.swconst.enumerations import SWSaveItemsPathErrorE

type IdsList = List[int]
type NamesList = List[str]
type PathsList = List[Path]


class IAdvancedSaveAsOptions(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IAdvancedSaveAsOptions({self.com_object})"

    @property
    def configuration_to_save(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ConfigurationsToSave.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @configuration_to_save.setter
    def configuration_to_save(self, value: List["IAdvancedSaveAsOptions"]) -> None:
        """
        Array of configurations to save.
        """
        self.com_object.ConfigurationsToSave = VARIANT(
            VT_BSTR | VT_ARRAY, [v.com_object for v in value]
        )

    @property
    def description(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~Description.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @description.setter
    def description(self, value: str) -> None:
        """
        Adds a desciption of the save.
        """
        self.com_object.Description = VARIANT(VT_BSTR, value)

    @property
    def geometry_to_save(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GeometryToSave.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @geometry_to_save.setter
    def geometry_to_save(self, value: SWGeometryToSaveE) -> None:
        self.com_object.GeometryToSave = VARIANT(VT_I4, value.value)

    @property
    def override_defaults(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~OverrideDefaults.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @override_defaults.setter
    def override_defaults(self, value: bool) -> None:
        self.com_object.OverrideDefaults = VARIANT(VT_BOOL, value)

    @property
    def preserve_geometry_references(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~PreserveGeometryReferences.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @preserve_geometry_references.setter
    def preserve_geometry_references(self, value: bool) -> None:
        self.com_object.PreserveGeometryReferences = VARIANT(VT_BOOL, value)

    @property
    def save_all_as_copy(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAllAsCopy.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @save_all_as_copy.setter
    def save_all_as_copy(self, value: bool) -> None:
        self.com_object.SaveAllAsCopy = VARIANT(VT_BOOL, value)

    @property
    def save_as_previous_version(self) -> None:
        """
        Write Only. Getter not implemented.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html
        """
        raise NotImplementedError("Write Only. Getter not implemented.")

    @save_as_previous_version.setter
    def save_as_previous_version(self, value: int) -> None:
        self.com_object.SaveAllAsCopy = VARIANT(VT_I4, value)

    def get_items_name_and_path(self) -> Tuple[IdsList, NamesList, PathsList]:
        """
        Gets all reference components' names and paths.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.html
        """
        out_ids_list = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_names_list = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_paths_list = VARIANT(VT_VARIANT | VT_BYREF, [])

        self.com_object.GetItemsNameAndPath(
            out_ids_list, out_names_list, out_paths_list
        )

        return (
            [int(i) for i in out_ids_list.value],
            [str(i) for i in out_names_list.value],
            [Path(i) for i in out_paths_list.value],
        )

    def modify_items_name_and_path(
        self, ids_list: IdsList, names_list: NamesList, paths_list: PathsList
    ) -> SWSaveItemsPathErrorE:
        """
        Modifies the specified reference components with the specified names and paths.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html
        """

        in_ids_list = VARIANT(VT_I4 | VT_ARRAY, [int(i) for i in ids_list])
        in_names_list = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in names_list])
        in_paths_list = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in paths_list])

        com_object = self.com_object.ModifyItemsNameAndPath(
            in_ids_list, in_names_list, in_paths_list
        )

        return SWSaveItemsPathErrorE(com_object)

    def set_prefix_suffix_to_all(self, prefix_string: str, suffix_string: str) -> None:
        """
        Sets a prefix and/or a suffix on all component reference names.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SetPrefixSuffixToAll.html
        """

        in_prefix_string = VARIANT(VT_BSTR, prefix_string)
        in_suffix_string = VARIANT(VT_BSTR, suffix_string)

        self.com_object.SetPrefixSuffixToAll(in_prefix_string, in_suffix_string)
