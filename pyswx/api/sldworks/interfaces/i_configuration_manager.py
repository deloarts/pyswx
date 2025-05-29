"""
IConfigurationManager Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html

Status: 🟢
"""

from typing import TYPE_CHECKING
from typing import List
from typing import Tuple

from pythoncom import VT_ARRAY
from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_DECIMAL
from pythoncom import VT_I4
from pythoncom import VT_VARIANT
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_configuration import IConfiguration
from pyswx.api.swconst.enumerations import SWCADFamilyCfgOptionsE
from pyswx.api.swconst.enumerations import SWChildComponentInBOMOptionE
from pyswx.api.swconst.enumerations import SWConfigTreeSortTypeE
from pyswx.api.swconst.enumerations import SWConfigurationOptions2E
from pyswx.api.swconst.enumerations import SWFeatMgrPaneE
from pyswx.api.swconst.enumerations import SWInConfigurationOptsE

if TYPE_CHECKING:
    from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2

type ParamsRetrieved = bool
type ParamNames = List[str]
type ParamValues = List[str]


class IConfigurationManager(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IConfigurationManager({self.com_object})"

    @property
    def active_configuration(self) -> IConfiguration:
        """
        Gets the active configuration of the document.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html
        """
        return IConfiguration(self.com_object.ActiveConfiguration)

    @property
    def document(self) -> "IModelDoc2":
        """
        Gets the related model document.

        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~Document.html
        """
        from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2

        return IModelDoc2(self.com_object.Document)

    @property
    def enable_configuration_tree(self) -> bool:
        """
        Gets or sets whether to update the ConfigurationManager tree.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~EnableConfigurationTree.html
        """
        return bool(self.com_object.EnableConfigurationTree)

    @enable_configuration_tree.setter
    def enable_configuration_tree(self, value: bool):
        self.com_object.EnableConfigurationTree = value

    @property
    def link_display_states_to_configurations(self) -> bool:
        """
        Gets or sets whether to link or unlink display states to or from the active configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html
        """
        return bool(self.com_object.LinkDisplayStatesToConfigurations)

    @link_display_states_to_configurations.setter
    def link_display_states_to_configurations(self, value: bool):
        self.com_object.LinkDisplayStatesToConfigurations = value

    @property
    def show_configuration_descriptions(self) -> bool:
        """
        Gets or sets whether to display configuration descriptions in ConfigurationManager.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationDescriptions.html
        """
        return bool(self.com_object.ShowConfigurationDescriptions)

    @show_configuration_descriptions.setter
    def show_configuration_descriptions(self, value: bool):
        self.com_object.ShowConfigurationDescriptions = value

    @property
    def show_configuration_names(self) -> bool:
        """
        Gets or sets whether to display configuration names in ConfigurationManager.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowConfigurationNames.html
        """
        return bool(self.com_object.ShowConfigurationNames)

    @show_configuration_names.setter
    def show_configuration_names(self, value: bool):
        self.com_object.ShowConfigurationNames = value

    @property
    def show_preview(self) -> bool:
        """
        Gets or sets whether to display the preview of a selected configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowPreview.html
        """
        return bool(self.com_object.ShowPreview)

    @show_preview.setter
    def show_preview(self, value: bool):
        self.com_object.ShowPreview = value

    def add_cad_family_configuration(
        self,
        name: str,
        description: str,
        is_physical_product: bool,
        representation_parent_name: str,
        config_options: SWCADFamilyCfgOptionsE,
        child_com_display_option: SWChildComponentInBOMOptionE,
        rebuild: bool,
    ) -> IConfiguration:
        """
        Adds the specified configuration to SOLIDWORKS Connected.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.html
        """
        in_name = VARIANT(VT_BSTR, name)
        in_description = VARIANT(VT_BSTR, description)
        in_is_physical_product = VARIANT(VT_BOOL, is_physical_product)
        in_representation_parent_name = VARIANT(VT_BSTR, representation_parent_name)
        in_config_options = VARIANT(VT_I4, config_options.value)
        in_child_com_display_option = VARIANT(VT_I4, child_com_display_option.value)
        in_rebuild = VARIANT(VT_BOOL, rebuild)

        com_object = self.com_object.AddCADFamilyConfiguration(
            in_name,
            in_description,
            in_is_physical_product,
            in_representation_parent_name,
            in_config_options,
            in_child_com_display_option,
            in_rebuild,
        )
        return IConfiguration(com_object)

    def add_configuration2(
        self,
        name: str,
        comment: str,
        alternate_name: str,
        options: SWConfigurationOptions2E,
        parent_config_name: str,
        description: str,
        rebuild: bool,
    ) -> IConfiguration:
        """
        Creates a new configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration2.html
        """
        in_name = VARIANT(VT_BSTR, name)
        in_comment = VARIANT(VT_BSTR, comment)
        in_alternate_name = VARIANT(VT_BSTR, alternate_name)
        in_options = VARIANT(VT_I4, options.value)
        in_parent_config_name = VARIANT(VT_BSTR, parent_config_name)
        in_description = VARIANT(VT_BSTR, description)
        in_rebuild = VARIANT(VT_BOOL, rebuild)

        com_object = self.com_object.AddConfiguration2(
            in_name,
            in_comment,
            in_alternate_name,
            in_options,
            in_parent_config_name,
            in_description,
            in_rebuild,
        )
        return IConfiguration(com_object)

    def add_rebuild_save_mark(
        self, which_configuration: SWInConfigurationOptsE, config_names: List[str]
    ) -> bool:
        """
        Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html
        """
        in_which_configuration = VARIANT(VT_I4, which_configuration.value)
        in_config_names = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in config_names])

        com_object = self.com_object.AddRebuildSaveMark(
            in_which_configuration, in_config_names
        )
        return bool(com_object)

    def add_speed_pak2(self, type: int, part_threshold: float) -> IConfiguration:
        """
        Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.html
        """
        in_type = VARIANT(VT_I4, type)
        in_part_threshold = VARIANT(VT_DECIMAL, part_threshold)

        com_object = self.com_object.AddSpeedPak2(in_type, in_part_threshold)
        return IConfiguration(com_object)

    def get_configuration_params(
        self, config_name: str
    ) -> Tuple[ParamsRetrieved, ParamNames, ParamValues]:
        """
        Gets the configuration parameters for the specified configuration.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html
        """
        in_config_name = VARIANT(VT_BSTR, config_name)

        out_params = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_values = VARIANT(VT_VARIANT | VT_BYREF, [])

        com_object = self.com_object.GetConfigurationParams(
            in_config_name, out_params, out_values
        )
        return (
            bool(com_object),
            [str(name) for name in out_params.value],
            [str(value) for value in out_values.value],
        )

    def get_configuration_params_count(self, config_name: str) -> int:
        """
        Gets the number of parameters for this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html
        """
        in_config_name = VARIANT(VT_BSTR, config_name)

        com_object = self.com_object.GetConfigurationParamsCount(in_config_name)
        return int(com_object)

    def remove_mark_for_all_configurations(self) -> bool:
        """
        Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~RemoveMarkForAllConfigurations.html
        """
        com_object = self.com_object.RemoveMarkForAllConfigurations
        return bool(com_object)

    def set_configuration_params(
        self, config_name: str, param_names: List[str], param_values: List[str]
    ) -> bool:
        """
        Sets the parameters for this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html
        """
        in_config_name = VARIANT(VT_BSTR, config_name)
        in_param_names = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in param_names])
        in_param_values = VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in param_values])

        com_object = self.com_object.SetConfigurationParams(
            in_config_name, in_param_names, in_param_values
        )
        return bool(com_object)

    def set_expanded(self, which_pane: SWFeatMgrPaneE, expand: bool) -> None:
        """
        Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded.html
        """
        in_which_pane = VARIANT(VT_I4, which_pane)
        in_expand = VARIANT(VT_BOOL, expand)

        self.com_object.SetExpanded(in_which_pane, in_expand)

    def sort_configuration_tree(self, in_sel_type: SWConfigTreeSortTypeE) -> None:
        """
        Specifies the order in which to list configurations in the ConfigurationManager.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SortConfigurationTree.html
        """
        in_in_sel_type = VARIANT(VT_I4, in_sel_type.value)

        self.com_object.SortConfigurationTree(in_in_sel_type)
