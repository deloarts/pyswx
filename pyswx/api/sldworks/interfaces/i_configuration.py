"""
IConfiguration Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html

Status: 🔴
"""

from pythoncom import VT_BOOL
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_component_2 import IComponent2
from pyswx.api.sldworks.interfaces.i_custom_property_manager import ICustomPropertyManager
from pyswx.api.sldworks.interfaces.i_dim_xpert_manager import IDimXpertManager
from pyswx.api.swconst.enumerations import SWChildComponentInBOMOptionE
from pyswx.api.swconst.enumerations import SWConfigurationTypeE


class IConfiguration(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IConfiguration({self.com_object})"

    @property
    def add_rebuild_save_mark(self) -> bool:
        """
        Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html
        """
        return bool(self.com_object.AddRebuildSaveMark)

    @add_rebuild_save_mark.setter
    def add_rebuild_save_mark(self, value: bool) -> None:
        self.com_object.AddRebuildSaveMark = value

    @property
    def alternate_name(self) -> str:
        """
        Gets or sets the configuration's alternate name (i.e., user-specified name).

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.html
        """
        return str(self.com_object.AlternateName)

    @alternate_name.setter
    def alternate_name(self, value: str) -> None:
        self.com_object.AlternateName = value

    @property
    def bom_part_no_source(self) -> int:
        """
        Gets or sets the source of the part number used in the BOM table.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource.html
        """
        return int(self.com_object.BOMPartNoSource)

    @bom_part_no_source.setter
    def bom_part_no_source(self, value: int) -> None:
        self.com_object.BOMPartNoSource = value

    @property
    def child_component_display_in_bom(self) -> SWChildComponentInBOMOptionE:
        """
        Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an assembly document.

        Reference:
        https://help.solidworks.com/2024/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.html
        """
        return SWChildComponentInBOMOptionE(self.com_object.ChildComponentDisplayInBOM)

    @child_component_display_in_bom.setter
    def child_component_display_in_bom(self, value: SWChildComponentInBOMOptionE) -> None:
        self.com_object.ChildComponentDisplayInBOM = value.value

    @property
    def comment(self) -> str:
        """
        Gets or sets the configuration comment.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Comment.html
        """
        return str(self.com_object.Comment)

    @comment.setter
    def comment(self, value: str) -> None:
        self.com_object.Comment = value

    @property
    def custom_property_manager(self) -> ICustomPropertyManager:
        """
        Gets the custom property information for this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html
        """
        return ICustomPropertyManager(self.com_object.CustomPropertyManager)

    @property
    def description(self) -> str:
        """
        Gets or sets the description of the configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description.html
        """
        return str(self.com_object.Description)

    @description.setter
    def description(self, value: str) -> None:
        self.com_object.Description = value

    def dim_xpert_manager(self, create_schema: bool) -> IDimXpertManager:
        """
        Gets the DimXpert schema for this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DimXpertManager.html

        Note:
        In the api definition this is a property, but in the python implementation it is a method, because python
        does not support properties with parameters. The parameter is the configuration name.
        """
        in_create_schema = VARIANT(VT_BOOL, bool(create_schema))
        return IDimXpertManager(self.com_object.DimXpertManager(in_create_schema))

    @property
    def hide_new_component_models(self) -> bool:
        """
        Gets or sets whether new components are hidden in this inactive configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~HideNewComponentModels.html
        """
        return bool(self.com_object.HideNewComponentModels)

    @hide_new_component_models.setter
    def hide_new_component_models(self, value: bool) -> None:
        self.com_object.HideNewComponentModels = value

    @property
    def large_design_review_mark(self) -> bool:
        """
        Gets or sets whether to add display data to this configuration when the document is saved.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark.html
        """
        return bool(self.com_object.LargeDesignReviewMark)

    @large_design_review_mark.setter
    def large_design_review_mark(self, value: bool) -> None:
        self.com_object.LargeDesignReviewMark = value

    @property
    def lock(self) -> bool:
        """
        Gets or sets whether the configuration is locked.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Lock.html
        """
        return bool(self.com_object.Lock)

    @lock.setter
    def lock(self, value: bool) -> None:
        self.com_object.Lock = value

    @property
    def name(self) -> str:
        """
        Gets or sets the configuration name.

        Reference:
        https://help.solidworks.com/2021/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html
        """
        return str(self.com_object.Name)

    @name.setter
    def name(self, value: str) -> None:
        self.com_object.Name = value

    @property
    def needs_rebuild(self) -> bool:
        """
        Gets whether the configuration needs to be rebuilt.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html
        """
        return bool(self.com_object.NeedsRebuild)

    @needs_rebuild.setter
    def needs_rebuild(self, value: bool) -> None:
        self.com_object.NeedsRebuild = value

    @property
    def representation_shared(self) -> bool:
        """
        Gets or sets whether this SOLIDWORKS Connected Representation configuration is shared.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RepresentationShared.html
        """
        return bool(self.com_object.RepresentationShared)

    @representation_shared.setter
    def representation_shared(self, value: bool) -> None:
        self.com_object.RepresentationShared = value

    @property
    def suppress_new_component_models(self) -> bool:
        """
        Gets or sets whether new components are suppressed in this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewComponentModels.html
        """
        return bool(self.com_object.SuppressNewComponentModels)

    @suppress_new_component_models.setter
    def suppress_new_component_models(self, value: bool) -> None:
        self.com_object.SuppressNewComponentModels = value

    @property
    def suppress_new_features(self) -> bool:
        """
        Gets or sets whether to suppress new features in this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewFeatures.html
        """
        return bool(self.com_object.SuppressNewFeatures)

    @suppress_new_features.setter
    def suppress_new_features(self, value: bool) -> None:
        self.com_object.SuppressNewFeatures = value

    @property
    def type(self) -> SWConfigurationTypeE:
        """
        Gets the type of configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Type.html
        """
        return SWConfigurationTypeE(self.com_object.Type)

    @type.setter
    def type(self, value: SWConfigurationTypeE) -> None:
        self.com_object.Type = value.value

    @property
    def use_alternate_name_in_bom(self) -> bool:
        """
        Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for this configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.html
        """
        return bool(self.com_object.UseAlternateNameInBOM)

    @use_alternate_name_in_bom.setter
    def use_alternate_name_in_bom(self, value: bool) -> None:
        self.com_object.UseAlternateNameInBOM = value

    @property
    def use_description_in_bom(self) -> bool:
        """
        Gets or sets whether the description of the configuration is displayed in the bill of materials.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM.html
        """
        return bool(self.com_object.UseDescriptionInBOM)

    @use_description_in_bom.setter
    def use_description_in_bom(self, value: bool) -> None:
        self.com_object.UseDescriptionInBOM = value

    def get_root_component3(self, resolve: bool) -> IComponent2 | None:
        """
        Gets the root component for this assembly configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html
        """
        com_object = self.com_object.GetRootComponent3(resolve)
        return IComponent2(com_object) if com_object else None
