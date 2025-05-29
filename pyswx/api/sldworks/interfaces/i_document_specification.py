"""
IDocumentSpecification Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html

Status: 🔴
"""

from pathlib import Path

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWAddToRecentDocumentListE
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWFileLoadErrorE
from pyswx.api.swconst.enumerations import SWFileLoadWarningE


class IDocumentSpecification(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IDocumentSpecification({self.com_object})"

    @property
    def add_to_recent_document_list(self) -> SWAddToRecentDocumentListE:
        """
        Gets or sets whether to add the opened document to the Recent Documents list.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList.html
        """
        return SWAddToRecentDocumentListE(self.com_object.AddToRecentDocumentList)

    @add_to_recent_document_list.setter
    def add_to_recent_document_list(self, value: SWAddToRecentDocumentListE) -> None:
        self.com_object.AddToRecentDocumentList = value.value

    @property
    def auto_repair(self) -> bool:
        """
        Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.html
        """
        return bool(self.com_object.AutoRepair)

    @auto_repair.setter
    def auto_repair(self, value: bool) -> None:
        self.com_object.AutoRepair = value

    @property
    def component_list(self):
        """Gets or sets the selected components to load when opening an assembly document."""
        raise NotImplementedError

    @component_list.setter
    def component_list(self, value):
        raise NotImplementedError

    @property
    def configuration_name(self):
        """Gets or sets the name of the configuration to load when opening a model document."""
        raise NotImplementedError

    @configuration_name.setter
    def configuration_name(self, value):
        raise NotImplementedError

    @property
    def critical_data_repair(self):
        """Gets or sets whether to automatically repair critical data errors in the file to be opened."""
        raise NotImplementedError

    @critical_data_repair.setter
    def critical_data_repair(self, value):
        raise NotImplementedError

    @property
    def detailing_mode(self):
        """Gets or sets whether this drawing document is in detailing mode."""
        raise NotImplementedError

    @detailing_mode.setter
    def detailing_mode(self, value):
        raise NotImplementedError

    @property
    def display_state(self) -> str:
        """
        Gets or sets the name of the display state to use when opening a model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DisplayState.html
        """
        return str(self.com_object.DisplayState)

    @display_state.setter
    def display_state(self, value: str) -> None:
        self.com_object.DisplayState = value

    @property
    def document_type(self) -> SWDocumentTypesE:
        """
        Gets or sets the type of model document to open.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.html
        """
        return SWDocumentTypesE(self.com_object.DocumentType)

    @document_type.setter
    def document_type(self, value: SWDocumentTypesE) -> None:
        self.com_object.DocumentType = value.value

    @property
    def error(self) -> SWFileLoadErrorE | None:
        """
        Gets or sets the file load errors when opening a model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Error.html
        """
        try:
            return SWFileLoadErrorE(self.com_object.Error)
        except ValueError:
            return None

    @error.setter
    def error(self, value: SWFileLoadErrorE) -> None:
        self.com_object.Error = value.value

    @property
    def file_name(self) -> Path:
        """
        Gets or sets the path and filename of the model document to open.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~FileName.html
        """
        return Path(self.com_object.FileName)

    @file_name.setter
    def file_name(self, value: Path) -> None:
        self.com_object.FileName = str(value)

    @property
    def ignore_hidden_components(self) -> bool:
        """
        Gets or sets whether to load hidden components when opening an assembly or drawing document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~IgnoreHiddenComponents.html
        """
        return bool(self.com_object.IgnoreHiddenComponents)

    @ignore_hidden_components.setter
    def ignore_hidden_components(self, value: bool) -> None:
        self.com_object.IgnoreHiddenComponents = value

    @property
    def interactive_advanced_open(self):
        """Gets whether to display an intermediate dialog for advanced open options."""
        raise NotImplementedError

    @interactive_advanced_open.setter
    def interactive_advanced_open(self, value):
        raise NotImplementedError

    @property
    def interactive_component_selection(self):
        """Gets whether to display the Selective Open dialog."""
        raise NotImplementedError

    @interactive_component_selection.setter
    def interactive_component_selection(self, value):
        raise NotImplementedError

    @property
    def light_weight(self) -> bool:
        """
        Gets or sets whether to open an assembly or drawing document with lightweight parts.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LightWeight.html
        """
        return bool(self.com_object.LightWeight)

    @light_weight.setter
    def light_weight(self, value: bool) -> None:
        self.com_object.LightWeight = value

    @property
    def load_external_references_in_memory(self):
        """Gets or sets whether to load external references in memory when opening a document."""
        raise NotImplementedError

    @load_external_references_in_memory.setter
    def load_external_references_in_memory(self, value):
        raise NotImplementedError

    @property
    def load_model(self):
        """Gets or sets whether to load the model if the document is a detached drawing."""
        raise NotImplementedError

    @load_model.setter
    def load_model(self, value):
        raise NotImplementedError

    @property
    def plm_object_specification(self):
        """Gets the specification of this SOLIDWORKS Connected document."""
        raise NotImplementedError

    @plm_object_specification.setter
    def plm_object_specification(self, value):
        raise NotImplementedError

    @property
    def query(self):
        """Gets or sets whether options can be retrieved by this API during open/load/save."""
        raise NotImplementedError

    @query.setter
    def query(self, value):
        raise NotImplementedError

    @property
    def read_only(self):
        """Gets or sets whether the model document is opened read-only."""
        raise NotImplementedError

    @read_only.setter
    def read_only(self, value):
        raise NotImplementedError

    @property
    def selective(self):
        """Gets or sets whether to open a document in Quick view or Selective mode."""
        raise NotImplementedError

    @selective.setter
    def selective(self, value):
        raise NotImplementedError

    @property
    def sheet_name(self):
        """Gets or sets the name of the sheet in a drawing document to open."""
        raise NotImplementedError

    @sheet_name.setter
    def sheet_name(self, value):
        raise NotImplementedError

    @property
    def silent(self) -> bool:
        """
        Gets or sets whether to open the model document silently.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.html
        """
        return bool(self.com_object.Silent)

    @silent.setter
    def silent(self, value: bool) -> None:
        self.com_object.Silent = value

    @property
    def use_light_weight_default(self) -> bool:
        """
        Gets or sets whether to use the system default lightweight setting.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault.html
        """
        return bool(self.com_object.UseLightWeightDefault)

    @use_light_weight_default.setter
    def use_light_weight_default(self, value: bool):
        self.com_object.UseLightWeightDefault = value

    @property
    def use_speed_pak(self):
        """Gets or sets whether to open an assembly document using the SpeedPak option."""
        raise NotImplementedError

    @use_speed_pak.setter
    def use_speed_pak(self, value):
        raise NotImplementedError

    @property
    def view_only(self):
        """
        Gets or sets whether to open the assembly document in Large Design Review mode.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.html
        """
        return bool(self.com_object.ViewOnly)

    @view_only.setter
    def view_only(self, value):
        self.com_object.ViewOnly = value

    @property
    def warning(self) -> SWFileLoadWarningE | None:
        """
        Gets or sets any file load warnings when opening a model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Warning.html
        """
        try:
            return SWFileLoadWarningE(self.com_object.Warning)
        except ValueError:
            return None

    @warning.setter
    def warning(self, value: SWFileLoadWarningE) -> None:
        self.com_object.Warning = value.value
