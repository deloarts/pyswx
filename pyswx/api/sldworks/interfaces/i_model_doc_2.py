"""
IModelDoc2 Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html

Status: 🟠
"""

from pathlib import Path
from typing import List

from pythoncom import VT_ARRAY
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_I4
from pythoncom import VT_R8
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_configuration import IConfiguration
from pyswx.api.sldworks.interfaces.i_configuration_manager import IConfigurationManager
from pyswx.api.sldworks.interfaces.i_display_dimension import IDisplayDimension
from pyswx.api.sldworks.interfaces.i_model_doc_extension import IModelDocExtension
from pyswx.api.swconst.enumerations import SWConfigurationOptions2E
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWFeatMgrPaneE
from pyswx.api.swconst.enumerations import SWFileSaveErrorE
from pyswx.api.swconst.enumerations import SWFileSaveWarningE
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.exceptions import DocumentError


class IModelDoc2(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IModelDoc2({self.com_object})"

    @property
    def configuration_manager(self) -> IConfigurationManager:
        """
        Gets the IConfigurationManager object, which allows access to a configuration in a model.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.imodeldoc2~configurationmanager.html
        """
        return IConfigurationManager(self.com_object.ConfigurationManager)

    @property
    def extension(self) -> IModelDocExtension:
        """
        Gets the IModelDocExtension object, which also allows access to the model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.imodeldoc2~extension.html
        """
        return IModelDocExtension(self.com_object.Extension)

    @property
    def i_material_property_values(self) -> List[float]:
        """
        Gets the material property values for this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMaterialPropertyValues.html
        """
        com_object = self.com_object.IMaterialPropertyValues
        return [float(i) for i in com_object]

    @i_material_property_values.setter
    def i_material_property_values(self, values: List[float]) -> None:
        in_values = VARIANT(VT_ARRAY | VT_R8, values)
        self.com_object.IMaterialPropertyValues = in_values

    @property
    def material_property_values(self) -> List[float]:
        """
        Gets the material property values for this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialPropertyValues.html
        """
        com_object = self.com_object.MaterialPropertyValues
        return [float(i) for i in com_object]

    @material_property_values.setter
    def material_property_values(self, values: List[float]) -> None:
        in_values = VARIANT(VT_ARRAY | VT_R8, values)
        self.com_object.MaterialPropertyValues = in_values

    def activate_feature_mgr_view(self):
        """Obsolete. Superseded by IFeatureMgrView::ActivateView."""
        raise NotImplementedError

    def activate_selected_feature(self) -> None:
        """Activates the selected feature for editing."""
        self.com_object.ActivateSelectedFeature

    def add_configuration(self):
        """Obsolete. Superseded by IModelDoc2::AddConfiguration3."""
        raise NotImplementedError

    def add_configuration_2(self):
        """Obsolete. Superseded by IModelDoc2::AddConfiguration3."""
        raise NotImplementedError

    def add_configuration_3(
        self, name: str, comment: str, alternate_name: str, options: SWConfigurationOptions2E
    ) -> IConfiguration:
        """
        Adds a new configuration to this model document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html
        """
        in_name = VARIANT(VT_BSTR, name)
        in_comment = VARIANT(VT_BSTR, comment)
        in_alternate_name = VARIANT(VT_BSTR, alternate_name)
        in_options = VARIANT(VT_I4, options.value)

        com_object = self.com_object.AddConfiguration3(in_name, in_comment, in_alternate_name, in_options)
        return IConfiguration(com_object)

    def add_custom_info(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_custom_info_2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_custom_info_3(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_diameter_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddDiameterDimension2."""
        raise NotImplementedError

    def add_diameter_dimension_2(self, x: float, y: float, z: float) -> IDisplayDimension:
        """
        Adds a diameter dimension at the specified location for the selected item.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html
        """
        in_x = VARIANT(VT_R8, x)
        in_y = VARIANT(VT_R8, y)
        in_z = VARIANT(VT_R8, z)

        com_object = self.com_object.AddDiameterDimension2(in_x, in_y, in_z)
        return IDisplayDimension(com_object)

    def add_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddDimension2."""
        raise NotImplementedError

    def add_dimension_2(self, x: float, y: float, z: float) -> IDisplayDimension:
        """
        Creates a display dimension at the specified location for selected entities.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html
        """
        in_x = VARIANT(VT_R8, x)
        in_y = VARIANT(VT_R8, y)
        in_z = VARIANT(VT_R8, z)

        com_object = self.com_object.AddDimension2(in_x, in_y, in_z)
        return IDisplayDimension(com_object)

    def add_feature_mgr_view(self):
        """Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3."""
        raise NotImplementedError

    def add_feature_mgr_view_2(self):
        """Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3."""
        raise NotImplementedError

    def add_feature_mgr_view_3(self, bitmap: int, app_view: int, tooltip: str, which_pane: SWFeatMgrPaneE) -> bool:
        """
        Adds the specified tab to the FeatureManager design tree view.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html
        """
        in_bitmap = VARIANT(VT_I4, bitmap)
        in_app_view = VARIANT(VT_I4, app_view)
        in_tooltip = VARIANT(VT_BSTR, tooltip)
        in_which_pane = VARIANT(VT_I4, which_pane.value)

        com_object = self.com_object.AddFeatureMgrView3(in_bitmap, in_app_view, in_tooltip, in_which_pane)
        return bool(com_object)

    def add_horizontal_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddHorizontalDimension2."""
        raise NotImplementedError

    def add_horizontal_dimension2(self):
        """Creates a horizontal dimension for the currently selected entities at the specified location."""
        raise NotImplementedError

    def add_ins(self):
        """Displays the Add-In Manager dialog box."""
        raise NotImplementedError

    def add_light_source(self):
        """Adds a type of light source to a scene with the specified names."""
        raise NotImplementedError

    def add_light_source_ext_property(self):
        """Stores a float, string, or integer value for the light source."""
        raise NotImplementedError

    def add_light_to_scene(self):
        """Adds a light source to a scene."""
        raise NotImplementedError

    def add_loft_section(self):
        """Adds a loft section to a blend feature."""
        raise NotImplementedError

    def add_or_edit_configuration(self):
        """Obsolete. Superseded by IConfiguration::GetParameters, IGetParameters, ISetParameters, and SetParameters."""
        raise NotImplementedError

    def add_property_extension(self):
        """Adds a property extension to this model."""
        raise NotImplementedError

    def add_radial_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddRadialDimension2."""
        raise NotImplementedError

    def add_radial_dimension2(self):
        """Adds a radial dimension at the specified location for the selected item."""
        raise NotImplementedError

    def add_relation(self):
        """Obsolete. Superseded by IEquationMgr::Add."""
        raise NotImplementedError

    def add_scene_ext_property(self):
        """Stores a float, string, or integer value for a scene."""
        raise NotImplementedError

    def add_vertical_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddVerticalDimension2."""
        raise NotImplementedError

    def add_vertical_dimension2(self):
        """Creates a vertical dimension for the currently selected entities at the specified location."""
        raise NotImplementedError

    def align_dimensions(self):
        """Obsolete. Superseded by IModelDocExtension::AlignDimensions."""
        raise NotImplementedError

    def align_ordinate(self):
        """Aligns the selected group of ordinate dimensions."""
        raise NotImplementedError

    def align_parallel_dimensions(self):
        """Aligns the selected linear dimensions in a parallel fashion."""
        raise NotImplementedError

    def and_select(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def and_select_by_id(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def and_select_by_mark(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def auto_infer_toggle(self):
        """Obsolete. Superseded by ISketchManager::AutoInference."""
        raise NotImplementedError

    def auto_solve_toggle(self):
        """Obsolete. Superseded by ISketchManager::AutoSolve."""
        raise NotImplementedError

    def blank_ref_geom(self):
        """Hides the selected reference geometry in the graphics window."""
        raise NotImplementedError

    def blank_sketch(self):
        """Hides the selected sketches."""
        raise NotImplementedError

    def break_all_external_references(self):
        """Obsolete. Superseded by IModelDocExtension::BreakAllExternalReferences2."""
        raise NotImplementedError

    def break_dimension_alignment(self):
        """Breaks the association of any selected dimensions belonging to an alignment group (parallel or collinear)."""
        raise NotImplementedError

    def change_sketch_plane(self):
        """Obsolete. Superseded by IModelDocExtension::ChangeSketchPlane."""
        raise NotImplementedError

    def clear_selection(self):
        """Obsolete. Superseded by IModelDoc2::ClearSelection2."""
        raise NotImplementedError

    def clear_selection2(self):
        """Clears the selection list."""
        raise NotImplementedError

    def clear_undo_list(self):
        """Clears the undo list for this model document."""
        raise NotImplementedError

    def close(self):
        """Not implemented. Use ISldWorks::CloseDoc."""
        raise NotImplementedError

    def close_family_table(self):
        """Closes the design table currently being edited."""
        raise NotImplementedError

    def close_print_preview(self):
        """Closes the currently displayed Print Preview page for this document."""
        raise NotImplementedError

    def closest_distance(self):
        """Calculates the minimum distance between the specified geometric objects."""
        raise NotImplementedError

    def create_3_point_arc(self):
        """Obsolete. Superseded by ISketchManager::Create3PointArc."""
        raise NotImplementedError

    def create_arc(self):
        """Obsolete. Superseded by IModelDoc2::CreateArc2."""
        raise NotImplementedError

    def create_arc2(self):
        """Obsolete. Superseded by ISketchManager::CreateArc."""
        raise NotImplementedError

    def create_arc_by_center(self):
        """Creates an arc by center in this model document."""
        raise NotImplementedError

    def create_arc_db(self):
        """Obsolete. Superseded by IModelDoc2::CreateArc2."""
        raise NotImplementedError

    def create_arc_vb(self):
        """Obsolete. Superseded by IModelDoc2::CreateArc2."""
        raise NotImplementedError

    def create_center_line(self):
        """Obsolete. Superseded by ISketchManager::CreateCenterLine."""
        raise NotImplementedError

    def create_center_line_vb(self):
        """Creates a center line from P1 to P2 for VBA and other Basic without SafeArrays."""
        raise NotImplementedError

    def create_circle(self):
        """Obsolete. Superseded by IModelDoc2::CreateCircle2."""
        raise NotImplementedError

    def create_circle2(self):
        """Obsolete. Superseded by SketchManager::CreateCircle."""
        raise NotImplementedError

    def create_circle_by_radius(self):
        """Obsolete. Superseded by IModelDoc2::CreateCircleByRadius2."""
        raise NotImplementedError

    def create_circle_by_radius2(self):
        """Obsolete. Superseded by SketchManager::CreateCircleByRadius."""
        raise NotImplementedError

    def create_circle_db(self):
        """Obsolete. Superseded by IModelDoc2::CreateCircle2."""
        raise NotImplementedError

    def create_circle_vb(self):
        """Obsolete. Superseded by IModelDoc2::CreateCircle2."""
        raise NotImplementedError

    def create_circular_sketch_step_and_repeat(self):
        """Obsolete. Superseded by ISketchManager::CreateCircularSketchStepAndRepeat."""
        raise NotImplementedError

    def create_clipped_splines(self):
        """Creates one or more sketch spline segments clipped against a given rectangle in active 2D sketch."""
        raise NotImplementedError

    def create_ellipse(self):
        """Obsolete. Superseded by IModelDoc2::CreateEllipse2."""
        raise NotImplementedError

    def create_ellipse2(self):
        """Obsolete. Superseded by ISketchManager::CreateEllipse."""
        raise NotImplementedError

    def create_ellipse_vb(self):
        """Obsolete. Superseded by IModelDoc2::CreateEllipse2."""
        raise NotImplementedError

    def create_elliptical_arc2(self):
        """Obsolete. Superseded by SketchManager::CreateEllipticalArc."""
        raise NotImplementedError

    def create_elliptical_arc_by_center(self):
        """Obsolete. Superseded by SketchManager::CreateEllipticalArc."""
        raise NotImplementedError

    def create_elliptical_arc_by_center_vb(self):
        """Obsolete. Superseded by SketchManager::CreateEllipticalArc."""
        raise NotImplementedError

    def create_feature_mgr_view(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def create_feature_mgr_view2(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def create_feature_mgr_view3(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def create_group(self):
        """Creates an annotation group from the currently selected annotations."""
        raise NotImplementedError

    def create_line(self):
        """Obsolete. Superseded by IModelDoc2::CreateLine2."""
        raise NotImplementedError

    def create_line2(self):
        """Obsolete. Superseded by SketchManager::CreateLine."""
        raise NotImplementedError

    def create_linear_sketch_step_and_repeat(self):
        """Obsolete. Superseded by ISketchManager::CreateLinearSketchStepAndRepeat."""
        raise NotImplementedError

    def create_line_db(self):
        """Obsolete. Superseded by IModelDoc2::CreateLine2."""
        raise NotImplementedError

    def create_line_vb(self):
        """Obsolete. Superseded by IModelDoc2::CreateLine2."""
        raise NotImplementedError

    def create_plane_at_angle(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtAngle3."""
        raise NotImplementedError

    def create_plane_at_angle2(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtAngle3."""
        raise NotImplementedError

    def create_plane_at_angle3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_at_offset(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtOffset3."""
        raise NotImplementedError

    def create_plane_at_offset2(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtOffset3."""
        raise NotImplementedError

    def create_plane_at_offset3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_at_surface(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface3."""
        raise NotImplementedError

    def create_plane_at_surface2(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface3."""
        raise NotImplementedError

    def create_plane_at_surface3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_fixed(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneFixed2."""
        raise NotImplementedError

    def create_plane_fixed2(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_per_curve_and_pass_point(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlanePerCurveAndPassPoint3."""
        raise NotImplementedError

    def create_plane_per_curve_and_pass_point2(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlanePerCurveAndPassPoint3."""
        raise NotImplementedError

    def create_plane_per_curve_and_pass_point3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_thru_3_points(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneThru3Points3."""
        raise NotImplementedError

    def create_plane_thru_3_points2(self):
        """Obsolete. Superseded by IModelDoc2::CreatePlaneThru3Points3."""
        raise NotImplementedError

    def create_plane_thru_3_points3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_thru_line_and_pt(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_plane_thru_pt_parallel_to_plane(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def create_point(self):
        """Obsolete. Superseded by IModelDoc2::CreatePoint2."""
        raise NotImplementedError

    def create_point2(self):
        """Obsolete. Superseded by ISketchManager::CreatePoint."""
        raise NotImplementedError

    def create_point_db(self):
        """Obsolete. Superseded by IModelDoc2::CreatePoint2 and IModelDoc2::ICreatePoint2."""
        raise NotImplementedError

    def create_spline(self):
        """Obsolete. Superseded by ISketchManager::CreateSpline."""
        raise NotImplementedError

    def create_spline_by_eqn_params(self):
        """Obsolete. Superseded by ISketchManager::CreateSplineByEqnParams."""
        raise NotImplementedError

    def create_splines_by_eqn_params(self):
        """Obsolete. Superseded by ISketchManager::CreateSplinesByEqnParams."""
        raise NotImplementedError

    def create_tangent_arc(self):
        """Obsolete. Superseded by IModelDoc2::CreateTangentArc2."""
        raise NotImplementedError

    def create_tangent_arc2(self):
        """Obsolete. Superseded by ISketchManager::CreateTangentArc."""
        raise NotImplementedError

    def deactivate_feature_mgr_view(self):
        """Deactivates a tab in the FeatureManager design tree view."""
        raise NotImplementedError

    def debug_check_iges_geom(self):
        """Dumps an IGES geometry check."""
        raise NotImplementedError

    def delete_all_relations(self):
        """Deletes all existing relations."""
        raise NotImplementedError

    def delete_bend_table(self):
        """Deletes a bend table."""
        raise NotImplementedError

    def delete_bkg_image(self):
        """Deletes any background image."""
        raise NotImplementedError

    def delete_configuration(self):
        """Obsolete. Superseded by IModelDoc2::DeleteConfiguration2."""
        raise NotImplementedError

    def delete_configuration2(self):
        """Deletes a configuration."""
        raise NotImplementedError

    def delete_custom_info(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def delete_custom_info2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def delete_design_table(self):
        """Deletes the design table for this document, if one exists."""
        raise NotImplementedError

    def delete_feature_mgr_view(self):
        """Removes the specified tab in the FeatureManager design tree."""
        raise NotImplementedError

    def delete_light_source(self):
        """Deletes a light source."""
        raise NotImplementedError

    def delete_named_view(self):
        """Deletes the specified model view."""
        raise NotImplementedError

    def delete_selection(self):
        """Obsolete. Superseded by IModelDocExtension::DeleteSelection2."""
        raise NotImplementedError

    def derive_sketch(self):
        """Creates a derived sketch."""
        raise NotImplementedError

    def deselect_by_id(self):
        """Removes the selected object from the selection list."""
        raise NotImplementedError

    def dim_preferences(self):
        """Sets dimension preferences."""
        raise NotImplementedError

    def dissolve_library_feature(self):
        """Dissolves the selected library features."""
        raise NotImplementedError

    def dissolve_sketch_text(self):
        """Dissolves sketch text."""
        raise NotImplementedError

    def drag_to(self):
        """Drags the specified end point."""
        raise NotImplementedError

    def draw_light_icons(self):
        """Draws any visible light icons."""
        raise NotImplementedError

    def edit_balloon_properties(self):
        """Obsolete. Superseded by INote::SetBalloon and INote::SetBomBalloonText."""
        raise NotImplementedError

    def edit_clear_all(self):
        """Obsolete. Superseded by IModelDoc2::ClearSelection2."""
        raise NotImplementedError

    def edit_configuration(self):
        """Obsolete. Superseded by IModelDoc2::EditConfiguration3."""
        raise NotImplementedError

    def edit_configuration2(self):
        """Obsolete. Superseded by IModelDoc2::EditConfiguration3."""
        raise NotImplementedError

    def edit_configuration3(self):
        """Edits the specified configuration."""
        raise NotImplementedError

    def edit_copy(self):
        """Copies the currently selected items and places them in the clipboard."""
        raise NotImplementedError

    def edit_cut(self):
        """Cuts the currently selected items and places them on the Microsoft Windows Clipboard."""
        raise NotImplementedError

    def edit_datum_target_symbol(self):
        """Edits a datum target symbol."""
        raise NotImplementedError

    def edit_delete(self):
        """Deletes the selected items."""
        raise NotImplementedError

    def edit_dimension_properties(self):
        """Obsolete. Superseded by IModelDoc2::EditDimensionProperties3."""
        raise NotImplementedError

    def edit_dimension_properties2(self):
        """Obsolete. Superseded by IModelDoc2::EditDimensionProperties3."""
        raise NotImplementedError

    def edit_dimension_properties3(self):
        """Obsolete. Superseded by IModelDocExtension::EditDimensionProperties."""
        raise NotImplementedError

    def edit_ordinate(self):
        """Puts the currently selected ordinate dimension into edit mode to add more ordinate dimensions to this group."""
        raise NotImplementedError

    def edit_rebuild3(self):
        """Rebuilds only those features that need to be rebuilt in the active configuration."""
        raise NotImplementedError

    def edit_redo(self):
        """Obsolete. Superseded by IModelDoc2::EditRedo2."""
        raise NotImplementedError

    def edit_redo2(self):
        """Repeats the specified number of actions in this SOLIDWORKS session."""
        raise NotImplementedError

    def edit_rollback(self):
        """Obsolete. Superseded by IFeatureManager::EditRollback."""
        raise NotImplementedError

    def edit_rollback2(self):
        """Obsolete. Superseded by IFeatureManager::EditRollback."""
        raise NotImplementedError

    def edit_route(self):
        """Makes the last selected route the active route."""
        raise NotImplementedError

    def edit_seed_feat(self):
        """Gets the pattern seed feature, based on the selected face, and displays the Edit Definition dialog."""
        raise NotImplementedError

    def edit_sketch(self):
        """Allows the currently selected sketch to be edited."""
        raise NotImplementedError

    def edit_sketch_or_single_sketch_feature(self):
        """Edits a selected sketch or feature sketch."""
        raise NotImplementedError

    def edit_suppress(self):
        """Obsolete. Superseded by IModelDoc2::EditSuppress2."""
        raise NotImplementedError

    def edit_suppress2(self):
        """Suppresses the selected feature, component, or owning feature of the selected face."""
        raise NotImplementedError

    def edit_undo(self):
        """Obsolete. Superseded by IModelDoc2::EditUndo2."""
        raise NotImplementedError

    def edit_undo2(self):
        """Undoes the specified number of actions in the active SOLIDWORKS session."""
        raise NotImplementedError

    def edit_unsuppress(self):
        """Obsolete. Superseded by IModelDoc2::EditUnsuppress2."""
        raise NotImplementedError

    def edit_unsuppress2(self):
        """Unsuppresses the selected feature or component."""
        raise NotImplementedError

    def edit_unsuppress_dependent(self):
        """Obsolete. Superseded by IModelDoc2::EditUnsuppressDependent2."""
        raise NotImplementedError

    def edit_unsuppress_dependent2(self):
        """Unsuppresses the selected feature/component and their dependents."""
        raise NotImplementedError

    def entity_properties(self):
        """Displays the Properties dialog for the selected edge or face."""
        raise NotImplementedError

    def enum_model_views(self):
        """Gets the model views enumeration in this document."""
        raise NotImplementedError

    def feat_edit(self):
        """Puts the current feature into edit mode."""
        raise NotImplementedError

    def feat_edit_def(self):
        """Displays the Feature Definition dialog and lets the user edit the values."""
        raise NotImplementedError

    def feature_boss(self):
        """Obsolete. Superseded by IFeatureManager::FeatureExtrusion2."""
        raise NotImplementedError

    def feature_boss2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureExtrusion2."""
        raise NotImplementedError

    def feature_boss_thicken(self):
        """Obsolete. Superseded by IFeatureManager::FeatureBossThicken."""
        raise NotImplementedError

    def feature_boss_thicken2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureBossThicken."""
        raise NotImplementedError

    def feature_boss_thin(self):
        """Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2."""
        raise NotImplementedError

    def feature_boss_thin2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2."""
        raise NotImplementedError

    def feature_by_position_reverse(self):
        """Gets the nth from last feature in the document."""
        raise NotImplementedError

    def feature_chamfer(self):
        """Creates a chamfer feature."""
        raise NotImplementedError

    def feature_chamfer_type(self):
        """Obsolete. Superseded by IFeatureManager::InsertFeatureChamfer."""
        raise NotImplementedError

    def feature_cir_pattern(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCircularPattern2."""
        raise NotImplementedError

    def feature_curve_pattern(self):
        """Obsolete. See IFeatureManager::CreateFeature and Remarks of ICurveDrivenPatternFeatureData."""
        raise NotImplementedError

    def feature_cut(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def feature_cut2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def feature_cut3(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def feature_cut4(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def feature_cut5(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def feature_cut_thicken(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCutThicken."""
        raise NotImplementedError

    def feature_cut_thicken2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCutThicken."""
        raise NotImplementedError

    def feature_cut_thin(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCutThin."""
        raise NotImplementedError

    def feature_cut_thin2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCutThin."""
        raise NotImplementedError

    def feature_extru_ref_surface(self):
        """Obsolete. Superseded by IModelDoc2::FeatureExtruRefSurface2."""
        raise NotImplementedError

    def feature_extru_ref_surface2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureExtruRefSurface."""
        raise NotImplementedError

    def feature_fillet(self):
        """Obsolete. Superseded by IFeatureManager::FeatureFillet."""
        raise NotImplementedError

    def feature_fillet2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureFillet."""
        raise NotImplementedError

    def feature_fillet3(self):
        """Obsolete. Superseded by IFeatureManager::FeatureFillet."""
        raise NotImplementedError

    def feature_fillet4(self):
        """Obsolete. Superseded by IFeatureManager::FeatureFillet."""
        raise NotImplementedError

    def feature_fillet5(self):
        """Obsolete. Superseded by IFeatureManager::FeatureFillet."""
        raise NotImplementedError

    def feature_linear_pattern(self):
        """Obsolete. Superseded by IFeatureManager::FeatureLinearPattern2."""
        raise NotImplementedError

    def feature_reference_curve(self):
        """Creates a reference curve feature from an array of curves."""
        raise NotImplementedError

    def feature_revolve2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureRevolve."""
        raise NotImplementedError

    def feature_revolve_cut2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureRevolveCut."""
        raise NotImplementedError

    def feature_sketch_driven_pattern(self):
        """Obsolete. Superseded by IFeatureManager::FeatureSketchDrivenPattern."""
        raise NotImplementedError

    def file_reload(self):
        """Obsolete. Superseded by IModelDoc2::ReloadOrReplace."""
        raise NotImplementedError

    def file_summary_info(self):
        """Displays the File Summary Information dialog box for this file."""
        raise NotImplementedError

    def first_feature(self):
        """Gets the first feature in the document."""
        raise NotImplementedError

    def font_bold(self):
        """Enables or disables bold font style in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def font_face(self):
        """Changes the font face in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def font_italic(self):
        """Enables or disables italic font style in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def font_points(self):
        """Changes font height (points) in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def font_underline(self):
        """Enables or disables underlining in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def font_units(self):
        """Changes font height (system units) in selected notes, dimensions, GTols."""
        raise NotImplementedError

    def force_rebuild3(self, top_only: bool) -> bool:
        """
        Forces rebuild of all features in active configuration.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html
        """
        return self.com_object.ForceRebuild3(top_only)

    def force_release_locks(self):
        """Releases file system locks on a file and detaches the file."""
        raise NotImplementedError

    def get_active_configuration(self):
        """Obsolete. Superseded by IConfigurationManager::ActiveConfiguration."""
        raise NotImplementedError

    def get_active_sketch(self):
        """Obsolete. Superseded by IModelDoc2::GetActiveSketch2."""
        raise NotImplementedError

    def get_active_sketch2(self):
        """Obsolete. Superseded by SketchManager::ActiveSketch."""
        raise NotImplementedError

    def get_add_to_db(self):
        """Gets whether entities are added directly to the SOLIDWORKS database."""
        raise NotImplementedError

    def get_ambient_light_properties(self):
        """Gets the ambient light properties for this model document."""
        raise NotImplementedError

    def get_angular_units(self):
        """Gets the current angular unit settings."""
        raise NotImplementedError

    def get_arc_centers_displayed(self):
        """Gets whether the arc centers are displayed."""
        raise NotImplementedError

    def get_bend_state(self):
        """Gets the current bend state of a sheet metal part."""
        raise NotImplementedError

    def get_blocking_state(self):
        """Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState."""
        raise NotImplementedError

    def get_color_table(self):
        """Obsolete. Superseded by ISldWorks::GetColorTable."""
        raise NotImplementedError

    def get_configuration_by_name(self):
        """Gets the specified configuration."""
        raise NotImplementedError

    def get_configuration_count(self):
        """Gets the number of configurations."""
        raise NotImplementedError

    def get_configuration_names(self) -> List[str]:
        """
        Gets the names of the configurations in this document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationNames.html
        """
        com_object = self.com_object.GetConfigurationNames
        return [str(name) for name in com_object] if com_object else []

    def get_consider_leaders_as_lines(self):
        """Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document."""
        raise NotImplementedError

    def get_coordinate_system_xform_by_name(self):
        """Obsolete. Superseded by IModelDocExtension::GetCoordinateSystemTransformByName."""
        raise NotImplementedError

    def get_current_coordinate_system_name(self):
        """Gets the name of the current coordinate system or an empty string for the default coordinate system."""
        raise NotImplementedError

    def get_custom_info_count(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_count2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_names(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_names2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_type(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_type2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_type3(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_custom_info_value(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def get_default_text_height(self):
        """Gets the default text height in use for this document."""
        raise NotImplementedError

    def get_dependencies(self):
        """Obsolete. Superseded by IModelDoc2::GetDependencies2."""
        raise NotImplementedError

    def get_dependencies2(self):
        """Obsolete. Superseded by IModelDocExtension::GetDependencies."""
        raise NotImplementedError

    def get_design_table(self):
        """Gets the design table associated with this part or assembly document."""
        raise NotImplementedError

    def get_detailing_defaults(self):
        """Obsolete. Superseded by IModelDoc2::GetUserPreferenceTextFormat and IModelDoc2::SetUserPreferenceTextFormat."""
        raise NotImplementedError

    def get_direction_light_properties(self):
        """Gets the directional light properties."""
        raise NotImplementedError

    def get_display_when_added(self):
        """Gets whether new sketch entities are displayed when created."""
        raise NotImplementedError

    def get_entity_name(self):
        """Gets the name of the specified face, edge, or vertex."""
        raise NotImplementedError

    def get_equation_mgr(self):
        """Gets the equation manager."""
        raise NotImplementedError

    def get_external_reference_name(self):
        """Gets the name of the externally referenced document (in the case of a join or mirrored part)."""
        raise NotImplementedError

    def get_feature_count(self):
        """Gets the number of features in this document."""
        raise NotImplementedError

    def get_feature_manager_width(self):
        """Gets the width of the FeatureManager design tree."""
        raise NotImplementedError

    def get_first_annotation(self):
        """Obsolete. Superseded by IModelDoc2::GetFirstAnnotation2."""
        raise NotImplementedError

    def get_first_annotation2(self):
        """Gets the first annotation in the model."""
        raise NotImplementedError

    def get_first_model_view(self):
        """Gets the first view in a model document."""
        raise NotImplementedError

    def get_grid_settings(self):
        """Gets the current grid settings."""
        raise NotImplementedError

    def get_inference_mode(self):
        """Obsolete. Superseded by SketchManager::InferenceMode."""
        raise NotImplementedError

    def get_layer_manager(self):
        """Gets the layer manager for the current drawing document."""
        raise NotImplementedError

    def get_light_source_count(self):
        """Gets the number of light sources."""
        raise NotImplementedError

    def get_light_source_ext_property(self):
        """Gets a float, string, or integer value stored for the light source."""
        raise NotImplementedError

    def get_light_source_id_from_name(self):
        """Gets the ID of the specified light source."""
        raise NotImplementedError

    def get_light_source_name(self):
        """Gets the name of a light source used internally by the SOLIDWORKS application."""
        raise NotImplementedError

    def get_line_count(self):
        """Gets the number of lines in the current sketch."""
        raise NotImplementedError

    def get_lines(self):
        """Gets all of the lines in the current sketch."""
        raise NotImplementedError

    def get_mass_properties(self):
        """Obsolete. Superseded by IModelDocExtension::GetMassProperties and IModelDocExtension::IGetMassProperties."""
        raise NotImplementedError

    def get_mass_properties2(self):
        """Obsolete. Superseded by IModelDocExtension::GetMassProperties and IModelDocExtension::IGetMassProperties."""
        raise NotImplementedError

    def get_model_view_count(self):
        """Obsolete. Superseded by IModelDocExtension::GetModelViewCount."""
        raise NotImplementedError

    def get_model_view_names(self):
        """Gets a list containing the names of each model view in this document."""
        raise NotImplementedError

    def get_next(self):
        """Gets the next document in the current SOLIDWORKS session."""
        raise NotImplementedError

    def get_num_dependencies(self):
        """Gets the number of strings returned by IModelDoc2::GetDependencies2."""
        raise NotImplementedError

    def get_path_name(self) -> Path:
        """
        Gets the full path name for this document, including the file name.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html
        """
        com_object = self.com_object.GetPathName
        return Path(com_object)

    def get_point_light_properties(self):
        """Gets point light properties."""
        raise NotImplementedError

    def get_popup_menu_mode(self):
        """Gets the current pop-up menu mode."""
        raise NotImplementedError

    def get_property_extension(self):
        """Gets the specified property extension on this model."""
        raise NotImplementedError

    def get_property_manager_page(self):
        """Obsolete. Superseded by ISldWorks::CreatePropertyManagerPage and ISldWorks::ICreatePropertyManagerPage."""
        raise NotImplementedError

    def get_ray_intersections_points(self):
        """Gets the intersection point information generated by IModelDoc2::RayIntersections."""
        raise NotImplementedError

    def get_ray_intersections_topology(self):
        """Gets the topology intersections generated by IModelDoc2::RayIntersections."""
        raise NotImplementedError

    def get_save_flag(self):
        """Gets whether the document is currently dirty and needs to be saved."""
        raise NotImplementedError

    def get_scene_bkg_dib(self):
        """Gets background image as a LPDIBSECTION."""
        raise NotImplementedError

    def get_scene_ext_property(self):
        """Gets a float, string, or integer value stored for the scene."""
        raise NotImplementedError

    def get_spotlight_properties(self):
        """Gets the spotlight properties."""
        raise NotImplementedError

    def get_standard_view_rotation(self):
        """Gets the specified view orientation matrix with respect to the Front view."""
        raise NotImplementedError

    def get_tessellation_quality(self):
        """Gets the shaded-display image quality number for the current document."""
        raise NotImplementedError

    def get_title(self) -> str:
        """
        Gets the title of the document that appears in the active window's title bar.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.imodeldoc2~gettitle.html
        """
        com_object = self.com_object.GetTitle
        return str(com_object)

    def get_toolbar_visibility(self):
        """Gets the visibility of a toolbar."""
        raise NotImplementedError

    def get_type(self) -> SWDocumentTypesE:
        """Gets the type of the document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html
        """
        com_object = self.com_object.GetType
        return SWDocumentTypesE(com_object)

    def get_units(self):
        """Gets the current unit settings, fraction base, fraction value, and significant digits."""
        raise NotImplementedError

    def get_update_stamp(self):
        """Gets the current update stamp for this document."""
        raise NotImplementedError

    def get_user_preference_double_value(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceDouble."""
        raise NotImplementedError

    def get_user_preference_integer_value(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceInteger."""
        raise NotImplementedError

    def get_user_preference_string_value(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceString."""
        raise NotImplementedError

    def get_user_preference_text_format(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceTextFormat."""
        raise NotImplementedError

    def get_user_preference_toggle(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceToggle."""
        raise NotImplementedError

    def get_user_unit(self):
        """Gets this document's units settings."""
        raise NotImplementedError

    def get_visibility_of_construct_planes(self):
        """Gets whether construction (reference) planes are currently visible."""
        raise NotImplementedError

    def get_zebra_stripe_data(self):
        """Gets zebra line data."""
        raise NotImplementedError

    def graphics_redraw(self):
        """Obsolete. Superseded by IModelDoc2::GraphicsRedraw2."""
        raise NotImplementedError

    def graphics_redraw2(self):
        """Obsolete. Superseded by IModelView::GraphicsRedraw and IModelView::IGraphicsRedraw."""
        raise NotImplementedError

    def grid_options(self):
        """Obsolete. Superseded by ISketchManager::SetGridOptions."""
        raise NotImplementedError

    def hide_component2(self):
        """Hides the selected component."""
        raise NotImplementedError

    def hide_cosmetic_thread(self):
        """Hides the selected cosmetic thread."""
        raise NotImplementedError

    def hide_dimension(self):
        """Hides the selected dimension in this document."""
        raise NotImplementedError

    def hide_feature_dimensions(self):
        """Obsolete. Superseded by IModelDoc2::GetUserPreferenceToggle or IModelDoc2::SetUserPreferenceToggle and swDisplayFeatureDimensions."""
        raise NotImplementedError

    def hide_show_bodies(self):
        """Sets whether to hide or show the bodies in the model."""
        raise NotImplementedError

    def hide_solid_body(self):
        """Hides the currently selected solid body."""
        raise NotImplementedError

    def hole_wizard(self):
        """Obsolete. Superseded by IFeatureManager::HoleWizard2."""
        raise NotImplementedError

    def i_add_configuration3(self):
        """Adds a new configuration to this model document."""
        raise NotImplementedError

    def i_add_diameter_dimension2(self):
        """Adds a diameter dimension at the specified location for the selected item."""
        raise NotImplementedError

    def i_add_dimension2(self):
        """Obsolete. Superseded by IModelDocExtension::AddDimension."""
        raise NotImplementedError

    def i_add_horizontal_dimension2(self):
        """Creates a horizontal dimension for the current selected entities at the specified location."""
        raise NotImplementedError

    def i_add_or_edit_configuration(self):
        """Obsolete. Superseded by IConfiguraiton::GetParameters, IConfiguration::IGetParameters, IConfiguration::ISetParameters, and IConfiguration::SetParameters."""
        raise NotImplementedError

    def i_add_radial_dimension2(self):
        """Adds a radial dimension at the specified location for the selected item."""
        raise NotImplementedError

    def i_add_vertical_dimension2(self):
        """Creates a vertical dimension for the currently selected entities at the specified location."""
        raise NotImplementedError

    def i_closest_distance(self):
        """Calculates the distance and closest points between two geometric objects."""
        raise NotImplementedError

    def i_create_arc(self):
        """Obsolete. Superseded by IModelDoc2::ICreateArc2."""
        raise NotImplementedError

    def i_create_arc2(self):
        """Creates an arc based on a center point, a start, an end point, and a direction."""
        raise NotImplementedError

    def i_create_center_line(self):
        """Creates a center line from P1 to P2."""
        raise NotImplementedError

    def i_create_circle2(self):
        """Creates a circle based on a center point and a point on the circle."""
        raise NotImplementedError

    def i_create_circle_by_radius(self):
        """Obsolete. Superseded by IModelDoc2::ICreateCircleByRadius2."""
        raise NotImplementedError

    def i_create_circle_by_radius2(self):
        """Creates a circle based on a center point and a specified radius."""
        raise NotImplementedError

    def i_create_clipped_splines(self):
        """Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
        raise NotImplementedError

    def i_create_ellipse(self):
        """Obsolete. Superseded by IModelDoc2::ICreateEllipse2."""
        raise NotImplementedError

    def i_create_ellipse2(self):
        """Creates an ellipse using the specified center point and points."""
        raise NotImplementedError

    def i_create_elliptical_arc2(self):
        """Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points."""
        raise NotImplementedError

    def i_create_elliptical_arc_by_center(self):
        """Creates an elliptical arc trimmed between two points."""
        raise NotImplementedError

    def i_create_feature_mgr_view(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def i_create_feature_mgr_view2(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def i_create_feature_mgr_view3(self):
        """Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2."""
        raise NotImplementedError

    def i_create_line(self):
        """Obsolete. Superseded by IModelDoc2::ICreateLine2."""
        raise NotImplementedError

    def i_create_line2(self):
        """Creates a sketch line in the currently active 2D or 3D sketch."""
        raise NotImplementedError

    def i_create_plane_at_angle2(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlaneAtAngle3."""
        raise NotImplementedError

    def i_create_plane_at_angle3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_at_offset2(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlaneAtOffset3."""
        raise NotImplementedError

    def i_create_plane_at_offset3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_at_surface2(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlaneAtSurface3."""
        raise NotImplementedError

    def i_create_plane_at_surface3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_fixed(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlaneFixed2."""
        raise NotImplementedError

    def i_create_plane_fixed2(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_per_curve_and_pass_point2(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlanePerCurveAndPassPoint3."""
        raise NotImplementedError

    def i_create_plane_per_curve_and_pass_point3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_thru3_points2(self):
        """Obsolete. Superseded by IModelDoc2::ICreatePlaneThru3Points3."""
        raise NotImplementedError

    def i_create_plane_thru3_points3(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_thru_line_and_pt(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_plane_thru_pt_parallel_to_plane(self):
        """Obsolete. Superseded by IFeatureManager::InsertRefPlane."""
        raise NotImplementedError

    def i_create_point2(self):
        """Obsolete. Superseded by ISketchManager::CreatePoint."""
        raise NotImplementedError

    def i_create_spline(self):
        """Obsolete. Superseded by ISketchManager::ICreateSpline."""
        raise NotImplementedError

    def i_create_spline_by_eqn_params(self):
        """Obsolete. Superseded by ISketchManager::ICreateSplineByEqnParams."""
        raise NotImplementedError

    def i_create_splines_by_eqn_params(self):
        """Obsolete. Superseded by ISketchManager::ICreateSplinesByEqnParams."""
        raise NotImplementedError

    def i_edit_dimension_properties3(self):
        """Obsolete. Superseded by IModelDocExtension::IEditDimensionProperties."""
        raise NotImplementedError

    def i_feature_by_position_reverse(self):
        """Gets the nth from last feature in the document."""
        raise NotImplementedError

    def i_feature_fillet2(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def i_feature_fillet3(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def i_feature_fillet4(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def i_feature_fillet5(self):
        """Obsolete. Superseded by IFeatureManager::FeatureCut."""
        raise NotImplementedError

    def i_feature_reference_curve(self):
        """Creates a reference curve feature from an array of curves."""
        raise NotImplementedError

    def i_first_feature(self):
        """Gets the first feature in the document."""
        raise NotImplementedError

    def i_get_3rd_party_storage(self):
        """Gets the IStream interface to the specified third-party stream inside this SOLIDWORKS document."""
        raise NotImplementedError

    def i_get_active_configuration(self):
        """Obsolete. Superseded by IConfigurationManager::ActiveConfiguration."""
        raise NotImplementedError

    def i_get_active_sketch(self):
        """Obsolete. Superseded by IModelDoc2::IGetActiveSketch2."""
        raise NotImplementedError

    def i_get_active_sketch2(self):
        """Gets the active sketch."""
        raise NotImplementedError

    def i_get_angular_units(self):
        """Gets the current angular unit settings."""
        raise NotImplementedError

    def i_get_color_table(self):
        """Obsolete. Superseded by ISldWorks::IGetColorTable."""
        raise NotImplementedError

    def i_get_configuration_by_name(self):
        """Gets the specified configuration."""
        raise NotImplementedError

    def i_get_configuration_names(self):
        """Gets the names of the configurations in this document."""
        raise NotImplementedError

    def i_get_coordinate_system_xform_by_name(self):
        """Obsolete. Superseded by IModelDocExtension::GetCoordinateSystemTransformByName."""
        raise NotImplementedError

    def i_get_custom_info_names(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def i_get_custom_info_names2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def i_get_dependencies(self):
        """Obsolete. Superseded by IModelDoc2::GetDependencies2."""
        raise NotImplementedError

    def i_get_dependencies2(self):
        """Gets all of the model's dependencies."""
        raise NotImplementedError

    def i_get_design_table(self):
        """Gets the design table associated with this part or assembly document."""
        raise NotImplementedError

    def i_get_detailing_defaults(self):
        """Obsolete. Superseded by IModelDoc2::GetUserPreferenceTextFormat and IModelDoc2::SetUserPreferenceTextFormat."""
        raise NotImplementedError

    def i_get_entity_name(self):
        """Gets the name of the specified face, edge, or vertex."""
        raise NotImplementedError

    def i_get_first_annotation(self):
        """Obsolete. Superseded by IModelDoc2::IGetFirstAnnotation2."""
        raise NotImplementedError

    def i_get_first_annotation2(self):
        """Gets the first annotation in the model."""
        raise NotImplementedError

    def i_get_first_model_view(self):
        """Gets the first view in a model document."""
        raise NotImplementedError

    def i_get_layer_manager(self):
        """Gets the layer manager ofr the current drawing document."""
        raise NotImplementedError

    def i_get_lines(self):
        """Gets all of the lines in the current sketch."""
        raise NotImplementedError

    def i_get_mass_properties(self):
        """Obsolete. Superseded by IModelDocExtension::IGetMassProperties."""
        raise NotImplementedError

    def i_get_mass_properties2(self):
        """Obsolete. Superseded by IModelDocExtension::IGetMassProperties."""
        raise NotImplementedError

    def i_get_model_view_names(self):
        """Gets a list containing the names of each model view in this document."""
        raise NotImplementedError

    def i_get_next(self):
        """Gets the next document in the current SOLIDWORKS session."""
        raise NotImplementedError

    def i_get_num_dependencies(self):
        """Obsolete. Superseded by IModelDoc2::IGetNumDependencies2."""
        raise NotImplementedError

    def i_get_num_dependencies2(self):
        """Gets the number of strings returned by IModelDoc2::IGetDependencies2."""
        raise NotImplementedError

    def i_get_ray_intersections_points(self):
        """Gets the intersection point information generated by IModelDoc2::IRayIntersections."""
        raise NotImplementedError

    def i_get_ray_intersections_topology(self):
        """Gets the topology intersections generated by IModelDoc2::IRayIntersections."""
        raise NotImplementedError

    def i_get_standard_view_rotation(self):
        """Gets the specified view orientation matrix with respect to the Front view."""
        raise NotImplementedError

    def i_get_units(self):
        """Gets the current unit settings, fraction base, fraction value, and significant digits."""
        raise NotImplementedError

    def i_get_user_preference_text_format(self):
        """Obsolete. Superseded by IModelDocExtension::GetUserPreferenceTextFormat."""
        raise NotImplementedError

    def i_get_user_unit(self):
        """Gets this document's units settings."""
        raise NotImplementedError

    def i_get_version_history_count(self):
        """Gets the size of the array required to hold data returend by IModleDoc2::IVersionHistory."""
        raise NotImplementedError

    def i_insert_bom_balloon2(self):
        """Obsolete. Superseded by IModelDocExtension::InsertBOMBalloon."""
        raise NotImplementedError

    def i_insert_datum_tag2(self):
        """Inserts a datum tag symbol at the selected location."""
        raise NotImplementedError

    def i_insert_gtol(self):
        """Creates a new geometric tolerance symbol (GTol) in this document."""
        raise NotImplementedError

    def i_insert_macro_feature(self):
        """Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3."""
        raise NotImplementedError

    def i_insert_mid_surface_ext(self):
        """Obsolete. Superseded by IFeatureManager::IInsertMidSurface."""
        raise NotImplementedError

    def i_insert_note(self):
        """Inserts a note in this document."""
        raise NotImplementedError

    def i_insert_projected_sketch2(self):
        """Projects the selected sketch items from the current sketch onto a selected surface."""
        raise NotImplementedError

    def i_insert_sheet_metal_edge_flange(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2."""
        raise NotImplementedError

    def i_insert_sketch_for_edge_flange(self):
        """Inserts a sketch for IFeatureManager::InsertSheetMetalEdgeFlange2 in this sheet metal part."""
        raise NotImplementedError

    def i_insert_sketch_text(self):
        """Obsolete. Superseded by IModelDoc2::InsertSketchText."""
        raise NotImplementedError

    def i_insert_weld_symbol3(self):
        """Inserts a weld symbol into the model."""
        raise NotImplementedError

    def i_list_auxiliary_external_file_references(self):
        """Gets the names of auxiliary external file references for this model."""
        raise NotImplementedError

    def i_list_external_file_references(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalReferences."""
        raise NotImplementedError

    def i_list_external_file_references2(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalReferences."""
        raise NotImplementedError

    def i_multi_select_by_ray(self):
        """Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
        raise NotImplementedError

    def insert_3d_sketch(self):
        """Obsolete. Superseded by IModelDoc2::Insert3DSketch2."""
        raise NotImplementedError

    def insert_3d_sketch2(self):
        """Obsolete. Superseded by ISketchManager::Insert3DSketch."""
        raise NotImplementedError

    def insert_3d_spline_curve(self):
        """Inserts a 3D-spline curve through the selected reference points."""
        raise NotImplementedError

    def insert_axis(self):
        """Obsolete. Superseded by IModelDoc2::InsertAxis2."""
        raise NotImplementedError

    def insert_axis2(self):
        """Inserts a reference axis based on the currently selected items with an option to automatically size the axis."""
        raise NotImplementedError

    def insert_bend_table_edit(self):
        """Inserts a bend table and puts the bend table into its edit state."""
        raise NotImplementedError

    def insert_bend_table_new(self):
        """Inserts a new bend table into the model document."""
        raise NotImplementedError

    def insert_bend_table_open(self):
        """Inserts an existing bend table from a file into this model document."""
        raise NotImplementedError

    def insert_bkg_image(self):
        """Inserts the scene background image."""
        raise NotImplementedError

    def insert_bom_balloon(self):
        """Obsolete. Superseded by IModelDoc2::InsertBOMBalloon2."""
        raise NotImplementedError

    def insert_bom_balloon2(self):
        """Obsolete. Superseded by IModelDocExtension::InsertBOMBalloon."""
        raise NotImplementedError

    def insert_composite_curve(self):
        """Inserts a composite curve based on selections."""
        raise NotImplementedError

    def insert_connection_point(self):
        """Adds a connection point based on the selected point and selected planar item."""
        raise NotImplementedError

    def insert_coordinate_system(self):
        """Obsolete. Superseded by IFeatureManager::InsertCoordinateSystem."""
        raise NotImplementedError

    def insert_cosmetic_thread(self):
        """Obsolete. Superseded by IFeatureManager::InsertCosmeticThread2."""
        raise NotImplementedError

    def insert_curve_file(self):
        """Creates a curve."""
        raise NotImplementedError

    def insert_curve_file_begin(self):
        """Creates a curve."""
        raise NotImplementedError

    def insert_curve_file_end(self):
        """Creates a curve."""
        raise NotImplementedError

    def insert_curve_file_point(self):
        """Creates a point for a curve."""
        raise NotImplementedError

    def insert_cut_blend(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutBlend."""
        raise NotImplementedError

    def insert_cut_blend2(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutBlend."""
        raise NotImplementedError

    def insert_cut_blend3(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutBlend."""
        raise NotImplementedError

    def insert_cut_blend4(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutBlend."""
        raise NotImplementedError

    def insert_cut_surface(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutSurface."""
        raise NotImplementedError

    def insert_cut_swept(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutSwept3."""
        raise NotImplementedError

    def insert_cut_swept2(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutSwept3."""
        raise NotImplementedError

    def insert_cut_swept3(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutSwept3."""
        raise NotImplementedError

    def insert_cut_swept4(self):
        """Obsolete. Superseded by IFeatureManager::InsertCutSwept3."""
        raise NotImplementedError

    def insert_datum_tag2(self):
        """Inserts a datum tag symbol at a selected location."""
        raise NotImplementedError

    def insert_datum_target_symbol(self):
        """Obsolete. Superseded by IModelDocExtension::InsertDatumTargetSymbol2."""
        raise NotImplementedError

    def insert_delete_face(self):
        """Obsolete. Supserseded by IModelDoc2::InsertDeleteFace2."""
        raise NotImplementedError

    def insert_delete_face2(self):
        """Obsolete. Superseded by IModelDocExtension::InsertDeleteFace."""
        raise NotImplementedError

    def insert_delete_hole(self):
        """Obsolete. Supserseded by IFeatureManager::InsertDeleteHoleForSurface."""
        raise NotImplementedError

    def insert_dome(self):
        """Inserts a dome."""
        raise NotImplementedError

    def insert_extend_surface(self):
        """Extends a surface along the selected faces or edges."""
        raise NotImplementedError

    def insert_family_table_edit(self):
        """Edits an open design table from Microsoft Excel."""
        raise NotImplementedError

    def insert_family_table_new(self):
        """Inserts an existing design table from the model into the selected drawing view."""
        raise NotImplementedError

    def insert_family_table_open(self):
        """Inserts the specified Microsoft Excel design table."""
        raise NotImplementedError

    def insert_feature_replace_face(self):
        """Creates a Replace Face feature."""
        raise NotImplementedError

    def insert_feature_shell(self):
        """Creates a shell feature."""
        raise NotImplementedError

    def insert_feature_shell_add_thickness(self):
        """Adds thickness to a face in a multi-thickness shell feature."""
        raise NotImplementedError

    def insert_frame_point(self):
        """Obsolete. Not superseded."""
        raise NotImplementedError

    def insert_gtol(self):
        """Creates a new geometric tolerance symbol (GTol) in this document."""
        raise NotImplementedError

    def insert_hatched_face(self):
        """Hatches the selected faces or closed sketch segments in a drawing."""
        raise NotImplementedError

    def insert_helix(self):
        """Creates a constant-pitch helix or spiral."""
        raise NotImplementedError

    def insert_library_feature(self):
        """Obsolete. See Remarks."""
        raise NotImplementedError

    def insert_loft_ref_surface(self):
        """Obsolete. Superseded by IModelDoc2::InsertLoftRefSurface2."""
        raise NotImplementedError

    def insert_loft_ref_surface2(self):
        """Creates a loft surface from the selected profiles, centerline, and guide curves."""
        raise NotImplementedError

    def insert_macro_feature(self):
        """Obsolete. Superseded by IFeatureManager::InsertMacroFeature3."""
        raise NotImplementedError

    def insert_mf_draft(self):
        """Obsolete. Superseded by IFeatureManager::InsertMultifaceDraft."""
        raise NotImplementedError

    def insert_mf_draft2(self):
        """Obsolete. Superseded by IFeatureManager::InsertMultifaceDraft."""
        raise NotImplementedError

    def insert_mid_surface_ext(self):
        """Obsolete. Superseded by IFeatureManager::InsertMidSurface."""
        raise NotImplementedError

    def insert_new_note3(self):
        """Creates a new note."""
        raise NotImplementedError

    def insert_note(self):
        """Inserts a note in this document."""
        raise NotImplementedError

    def insert_object(self) -> None:
        """
        Activates the Microsoft Insert Object dialog.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertObject.html
        """
        self.com_object.InsertObject()

    def insert_object_from_file(self):
        """Obsolete. Superseded by IModelDocExtension::InsertObjectFromFile."""
        raise NotImplementedError

    def insert_offset_surface(self):
        """Inserts an offset surface."""
        raise NotImplementedError

    def insert_planar_ref_surface(self):
        """Inserts a planar reference surface."""
        raise NotImplementedError

    def insert_point(self):
        """Inserts a point in this model document."""
        raise NotImplementedError

    def insert_projected_sketch(self):
        """Obsolete. Superseded by IModelDoc2::InsertProjectedSketch2."""
        raise NotImplementedError

    def insert_projected_sketch2(self):
        """Obsolete. See IProjectionCurveFeatureData and IFeatureManager::CreateDefinition."""
        raise NotImplementedError

    def insert_protrusion_blend(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend."""
        raise NotImplementedError

    def insert_protrusion_blend2(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend."""
        raise NotImplementedError

    def insert_protrusion_blend3(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend."""
        raise NotImplementedError

    def insert_protrusion_blend4(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend."""
        raise NotImplementedError

    def insert_protrusion_swept(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_protrusion_swept2(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_protrusion_swept3(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_protrusion_swept4(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_radiate_surface(self):
        """Creates a radiate surface based on the selections."""
        raise NotImplementedError

    def insert_ref_point(self):
        """Inserts a reference point based on the current selections."""
        raise NotImplementedError

    def insert_revolved_ref_surface(self):
        """Obsolete. Superseded by IFeatureManager::InsertRevolvedRefSurface."""
        raise NotImplementedError

    def insert_rib(self):
        """Obsolete. Superseded by IModelDoc2::InsertRib2."""
        raise NotImplementedError

    def insert_rib2(self):
        """Obsolete. Superseded by IFeatureManager::InsertRib."""
        raise NotImplementedError

    def insert_rip(self):
        """Creates a rip feature."""
        raise NotImplementedError

    def insert_route_point(self):
        """Adds a route point based on the selected point."""
        raise NotImplementedError

    def insert_scale(self):
        """Obsolete. Superseded by IFeatureManager::InsertScale."""
        raise NotImplementedError

    def insert_sew_ref_surface(self):
        """Obsolete. Superseded by IFeatureManager::InsertSewRefSurface."""
        raise NotImplementedError

    def insert_sheet_metal_3d_bend(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetal3dBend."""
        raise NotImplementedError

    def insert_sheet_metal_base_flange(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetalBaseFlange."""
        raise NotImplementedError

    def insert_sheet_metal_break_corner(self):
        """Inserts a break corner into a sheet metal part."""
        raise NotImplementedError

    def insert_sheet_metal_closed_corner(self):
        """Inserts a sheet metal closed corner into this model document."""
        raise NotImplementedError

    def insert_sheet_metal_edge_flange(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2."""
        raise NotImplementedError

    def insert_sheet_metal_fold(self):
        """Inserts a fold feature at the selected objects."""
        raise NotImplementedError

    def insert_sheet_metal_hem(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetalHem."""
        raise NotImplementedError

    def insert_sheet_metal_jog(self):
        """Inserts a sheet metal jog in the current model document."""
        raise NotImplementedError

    def insert_sheet_metal_miter_flange(self):
        """Obsolete. Superseded by IFeatureManager::InsertSheetMetalMiterFlange."""
        raise NotImplementedError

    def insert_sheet_metal_unfold(self):
        """Inserts an unfold feature at the selected objects."""
        raise NotImplementedError

    def insert_sketch(self):
        """Obsolete. Superseded by ISketchManager::InsertSketch."""
        raise NotImplementedError

    def insert_sketch2(self):
        """Obsolete. Superseded by ISketchManager::InsertSketch."""
        raise NotImplementedError

    def insert_sketch_for_edge_flange(self):
        """Inserts a profile sketch of an edge flange in this sheet metal part."""
        raise NotImplementedError

    def insert_sketch_picture(self):
        """Inserts a picture into the current sketch."""
        raise NotImplementedError

    def insert_sketch_picture_data(self):
        """Inserts a picture into the current sketch."""
        raise NotImplementedError

    def insert_sketch_picture_data_x64(self):
        """Inserts a picture into the current sketch in 64-bit applications."""
        raise NotImplementedError

    def insert_sketch_text(self):
        """Inserts sketch text."""
        raise NotImplementedError

    def insert_spline_point(self):
        """Inserts a spline point."""
        raise NotImplementedError

    def insert_split_line_project(self):
        """Splits a face by projecting sketch lines onto the face."""
        raise NotImplementedError

    def insert_split_line_sil(self):
        """Splits a face by creating split lines along the silhouette of the selected faces."""
        raise NotImplementedError

    def insert_stacked_balloon(self):
        """Obsolete. Superseded by IModelDocExtension::InsertStackedBalloon."""
        raise NotImplementedError

    def insert_surface_finish_symbol2(self):
        """Obsolete. Superseded by IModelDocExtension::InsertSurfaceFinishSymbol3."""
        raise NotImplementedError

    def insert_sweep_ref_surface(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_sweep_ref_surface2(self):
        """Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3."""
        raise NotImplementedError

    def insert_weld_symbol2(self):
        """Obsolete. Superseded by IModelDoc2::InsertWeldSymbol3."""
        raise NotImplementedError

    def insert_weld_symbol3(self):
        """Inserts a weld symbol into the model."""
        raise NotImplementedError

    def inspect_curvature(self):
        """Adds curvature combs to the selected sketch segment."""
        raise NotImplementedError

    def i_parameter(self):
        """Gets the specified parameter."""
        raise NotImplementedError

    def i_ray_intersections(self):
        """Obsolete. Superseded by IModelDocExtension::RayIntersections."""
        raise NotImplementedError

    def i_release_3rd_party_storage(self):
        """Releases the specified third-party stream."""
        raise NotImplementedError

    def is_active(self):
        """Gets whether the specified assembly component is shown or hidden in this model document."""
        raise NotImplementedError

    def is_editing_self(self):
        """Gets whether this model is being edited in the context of another document."""
        raise NotImplementedError

    def i_select_by_ray(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByRay."""
        raise NotImplementedError

    def i_set_angular_units(self):
        """Sets the current angular units."""
        raise NotImplementedError

    def i_set_next_selection_group_id(self):
        """Sets the group ID for all remaining selections."""
        raise NotImplementedError

    def i_sketch_spline_by_eqn_params(self):
        """Creates a spline on the active 2D sketch using the specified b-curve parameters."""
        raise NotImplementedError

    def is_light_locked_to_model(self):
        """Gets whether the specified light is fixed."""
        raise NotImplementedError

    def is_opened_read_only(self):
        """Gets whether a SOLIDWORKS document is open in read-only mode."""
        raise NotImplementedError

    def is_opened_view_only(self):
        """Gets whether a SOLIDWORKS document is open in view-only mode."""
        raise NotImplementedError

    def is_tessellation_valid(self):
        """Gets whether the current set of facets is valid."""
        raise NotImplementedError

    def i_version_history(self):
        """Gets an array of strings indicating the versions in which this model document was saved."""
        raise NotImplementedError

    def lb_down_at(self):
        """Generates a left mouse button press (down) event."""
        raise NotImplementedError

    def lb_up_at(self):
        """Generates a left-mouse button release (up) event."""
        raise NotImplementedError

    def lights(self):
        """Obsolete. Not superseded."""
        raise NotImplementedError

    def list_auxiliary_external_file_references(self):
        """Gets the names of auxiliary external file references for this model."""
        raise NotImplementedError

    def list_auxiliary_external_file_references_count(self):
        """Gets the number of auxiliary external file references for this model."""
        raise NotImplementedError

    def list_external_file_references(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalReferences."""
        raise NotImplementedError

    def list_external_file_references2(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalReferences."""
        raise NotImplementedError

    def list_external_file_references_count(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalFileReferenceCount."""
        raise NotImplementedError

    def list_external_file_references_count2(self):
        """Obsolete. Superseded by IModelDocExtension::ListExternalFileReferenceCount."""
        raise NotImplementedError

    def lock(self):
        """Blocks the modifying commands in the user interface, effectively locking the application."""
        raise NotImplementedError

    def lock_all_external_references(self):
        """Locks all external references."""
        raise NotImplementedError

    def lock_frame_point(self):
        """Obsolete. Not superseded."""
        raise NotImplementedError

    def lock_light_to_model(self):
        """Locks or unlocks the specified light."""
        raise NotImplementedError

    def mold_draft_analysis(self):
        """Performs a mold draft analysis."""
        raise NotImplementedError

    def multi_select_by_ray(self):
        """Selects multiple objects intersected by a ray from point (x,y,z) in direction vector (x,y,z) within a distance radius."""
        raise NotImplementedError

    def name_view(self):
        """Creates a named view using the current view."""
        raise NotImplementedError

    def object_display_as_icon(self):
        """Shows the current OLE object as an icon."""
        raise NotImplementedError

    def object_display_content(self):
        """Shows the current OLE object's content."""
        raise NotImplementedError

    def object_resetsize(self):
        """Sets the size of the current OLE object to the default."""
        raise NotImplementedError

    def parameter(self):
        """Gets the specified parameter."""
        raise NotImplementedError

    def parent_child_relationship(self):
        """Shows the Parent/Child Relationships dialog for the selected feature."""
        raise NotImplementedError

    def paste(self):
        """Pastes the contents of the Microsoft Windows Clipboard at the current insertion point."""
        raise NotImplementedError

    def post_trim_surface(self):
        """Obsolete. Superseded by IFeatureManager::PostTrimSurface."""
        raise NotImplementedError

    def pre_trim_surface(self):
        """Obsolete. Superseded by IFeatureManager::PreTrimSurface."""
        raise NotImplementedError

    def print_direct(self):
        """Prints the current document to the default printer."""
        raise NotImplementedError

    def print_out(self):
        """Obsolete. Superseded by IModelDocExtension::PrintOut2 and IPrintOut2."""
        raise NotImplementedError

    def print_out2(self):
        """Obsolete. Superseded by IModelDocExtension::PrintOut2 and IPrintOut2."""
        raise NotImplementedError

    def print_preview(self):
        """Displays the Print Preview page for the current document."""
        raise NotImplementedError

    def property_sheet(self):
        """Displays the selected object's property sheet."""
        raise NotImplementedError

    def quit(self):
        """Closes the active document without saving changes."""
        raise NotImplementedError

    def ray_intersections(self):
        """Obsolete. Superseded by IModelDocExtension::RayIntersections."""
        raise NotImplementedError

    def reattach_ordinate(self):
        """Reattaches an ordinate dimension to a different entity."""
        raise NotImplementedError

    def rebuild(self):
        """Obsolete. Superseded by IModelDocExtension::Rebuild."""
        raise NotImplementedError

    def reload_or_replace(self):
        """Obsolete. Superseded by IModelDocExtension::ReloadOrReplace."""
        raise NotImplementedError

    def remove_groups(self):
        """Removes any annotation groups in the current selection."""
        raise NotImplementedError

    def remove_inspect_curvature(self):
        """Removes curvature combs from the selected curved sketch segment."""
        raise NotImplementedError

    def remove_items_from_group(self):
        """Removes the selected annotations from their annotation groups."""
        raise NotImplementedError

    def reset_blocking_state(self):
        """Resets the blocking state for the SOLIDWORKS menus."""
        raise NotImplementedError

    def reset_light_source_ext_property(self):
        """Resets the properties for a light source."""
        raise NotImplementedError

    def reset_property_extension(self):
        """Clears all values stored in the property extension."""
        raise NotImplementedError

    def reset_scene_ext_property(self):
        """Resets the extension property for a scene."""
        raise NotImplementedError

    def save(self):
        """Obsolete. Superseded by IModelDoc2::Save3."""
        raise NotImplementedError

    def save2(self):
        """Obsolete. Superseded by IModelDoc2::Save3."""
        raise NotImplementedError

    def save_3(self, options: SWSaveAsOptionsE | None) -> bool:
        """
        Saves the current document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.html

        Raises:
            DocumentError: Raised if there is an error saving the document.
        """
        in_options = VARIANT(VT_I4, options.value) if options else VARIANT(VT_I4, 0)

        out_errors = VARIANT(VT_BYREF | VT_I4, None)
        out_warnings = VARIANT(VT_BYREF | VT_I4, None)

        com_object = self.com_object.Save3(in_options, out_errors, out_warnings)

        if out_warnings.value != 0:
            out_warnings = SWFileSaveWarningE(value=out_warnings.value)
            self.logger.warning(out_warnings.name)

        if out_errors.value != 0:
            out_errors = SWFileSaveErrorE(value=out_errors.value)
            raise DocumentError(str(out_errors))

        return com_object

    def save_as(self):
        """Obsolete. Superseded by IModelDocExtension::SaveAs."""
        raise NotImplementedError

    def save_as2(self):
        """Obsolete. Superseded by IModelDocExtension::SaveAs."""
        raise NotImplementedError

    def save_as3(self):
        """Obsolete. Superseded by IModelDocExtension::SaveAs."""
        raise NotImplementedError

    def save_as4(self):
        """Obsolete. Superseded by IModelDocExtension::SaveAs."""
        raise NotImplementedError

    def save_as_silent(self):
        """Obsolete. Superseded by IModelDocExtension::SaveAs."""
        raise NotImplementedError

    def save_bmp(self):
        """Saves the current view as a bitmap (BMP) file."""
        raise NotImplementedError

    def save_silent(self):
        """Obsolete. Superseded by IModelDoc2::Save3."""
        raise NotImplementedError

    def scale(self):
        """Scales the part."""
        raise NotImplementedError

    def screen_rotate(self):
        """Switches between model and screen center rotation."""
        raise NotImplementedError

    def select(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_at(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_by_id(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_by_mark(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_by_name(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_by_ray(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByRay."""
        raise NotImplementedError

    def selected_edge_properties(self):
        """Sets the property values of the selected edge."""
        raise NotImplementedError

    def selected_face_properties(self):
        """Sets the material property values of the selected face."""
        raise NotImplementedError

    def selected_feature_properties(self):
        """Sets the property values of the selected feature."""
        raise NotImplementedError

    def select_loop(self):
        """Selects the loop that corresponds to the selected edge."""
        raise NotImplementedError

    def select_midpoint(self):
        """Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list."""
        raise NotImplementedError

    def select_sketch_arc(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_sketch_item(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_sketch_line(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_sketch_point(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_sketch_spline(self):
        """Obsolete. Superseded by IModelDocExtension::SelectByID2."""
        raise NotImplementedError

    def select_tangency(self):
        """Selects all faces tangent to the selected face."""
        raise NotImplementedError

    def set_add_to_db(self):
        """Obsolete. Superseded by ISketchManager::AddToDB."""
        raise NotImplementedError

    def set_ambient_light_properties(self):
        """Sets ambient light properties."""
        raise NotImplementedError

    def set_angular_units(self):
        """Sets the current angular units."""
        raise NotImplementedError

    def set_arc_centers_displayed(self):
        """Sets the current arc centers displayed setting."""
        raise NotImplementedError

    def set_bend_state(self):
        """Sets the bend state of a sheet metal part."""
        raise NotImplementedError

    def set_blocking_state(self):
        """Sets the blocking state for the SOLIDWORKS menus."""
        raise NotImplementedError

    def set_consider_leaders_as_lines(self):
        """Sets a flag indicating whether leader display data should be included as lines."""
        raise NotImplementedError

    def set_direction_light_properties(self):
        """Sets direction light properties."""
        raise NotImplementedError

    def set_display_when_added(self):
        """Obsolete. Superseded by ISketchManager::DisplayWhenAdded."""
        raise NotImplementedError

    def set_feature_manager_width(self):
        """Sets the width of the FeatureManager design tree."""
        raise NotImplementedError

    def set_inference_mode(self):
        """Obsolete. Superseded by SketchManager::InferenceMode."""
        raise NotImplementedError

    def set_light_source_name(self):
        """Sets the light source name used internally by SOLIDWORKS."""
        raise NotImplementedError

    def set_light_source_property_values_vb(self):
        """Sets the light source property values."""
        raise NotImplementedError

    def set_param_value(self):
        """Sets the value of selected dimension (or parameter)."""
        raise NotImplementedError

    def set_pick_mode(self):
        """Returns the user to the default selection mode."""
        raise NotImplementedError

    def set_point_light_properties(self):
        """Sets point light properties."""
        raise NotImplementedError

    def set_popup_menu_mode(self):
        """Sets the pop-up menu mode."""
        raise NotImplementedError

    def set_read_only_state(self):
        """Sets whether this document is read-only or read-write."""
        raise NotImplementedError

    def set_save_as_file_name(self):
        """Sets the Save As filename within FileSaveAsNotify2 handlers."""
        raise NotImplementedError

    def set_save_flag(self):
        """Flags the document as dirty."""
        raise NotImplementedError

    def set_scene_bkg_dib(self):
        """Sets background image described by DIBSECTION data."""
        raise NotImplementedError

    def set_spotlight_properties(self):
        """Sets the spotlight properties."""
        raise NotImplementedError

    def set_tessellation_quality(self):
        """Sets the shaded-display image quality number for the current document."""
        raise NotImplementedError

    def set_title2(self):
        """Sets the title of a new document."""
        raise NotImplementedError

    def set_toolbar_visibility(self):
        """Sets the visibility of a toolbar."""
        raise NotImplementedError

    def set_units(self):
        """Sets the units used by the end-user for the model."""
        raise NotImplementedError

    def set_user_preference_double_value(self):
        """Obsolete. Superseded by IModelDocExtension::SetUserPreferenceDouble."""
        raise NotImplementedError

    def set_user_preference_integer_value(self):
        """Obsolete. Superseded by IModelDocExtension::SetUserPreferenceInteger."""
        raise NotImplementedError

    def set_user_preference_string_value(self):
        """Obsolete. Superseded by IModelDocExtension::SetUserPreferenceString."""
        raise NotImplementedError

    def set_user_preference_text_format(self):
        """Obsolete. Superseded by IModelDocExtension::SetUserPreferenceTextFormat."""
        raise NotImplementedError

    def set_user_preference_toggle(self):
        """Obsolete. Superseded by IModelDocExtension::SetUserPreferenceToggle."""
        raise NotImplementedError

    def set_zebra_stripe_data(self):
        """Sets the zebra-line data."""
        raise NotImplementedError

    def show_component2(self):
        """Shows the selected component."""
        raise NotImplementedError

    def show_configuration(self):
        """Obsolete. Superseded by IModelDoc2::ShowConfiguration2."""
        raise NotImplementedError

    def show_cosmetic_thread(self):
        """Shows the selected cosmetic thread."""
        raise NotImplementedError

    def show_feature_dimensions(self):
        """Obsolete. Superseded by IModelDoc2::GetUserPreferenceToggle and IModelDoc2::SetUserPreferenceToggle and swDisplayFeatureDimensions."""
        raise NotImplementedError

    def show_named_view(self):
        """Obsolete. Superseded by IModelDoc2::ShowNameView2."""
        raise NotImplementedError

    def show_named_view2(self):
        """Shows the specified view."""
        raise NotImplementedError

    def show_solid_body(self):
        """Shows the selected solid body."""
        raise NotImplementedError

    def simple_hole(self):
        """Obsolete. Superseded by IFeatureManager::SimpleHole."""
        raise NotImplementedError

    def simple_hole2(self):
        """Obsolete. Superseded by IFeatureManager::SimpleHole."""
        raise NotImplementedError

    def simple_hole3(self):
        """Obsolete. Superseded by IFeatureManager::SimpleHole."""
        raise NotImplementedError

    def simplify_spline(self):
        """Obsolete. Superseded by ISketchSpline::Simplify."""
        raise NotImplementedError

    def sketch_3d_intersections(self):
        """Creates new sketch segments based on the selected surfaces."""
        raise NotImplementedError

    def sketch_add_constraints(self):
        """Adds the specified constraint to the selected entities."""
        raise NotImplementedError

    def sketch_align(self):
        """Aligns the selected sketch entities."""
        raise NotImplementedError

    def sketch_arc(self):
        """Creates an arc in the current model document."""
        raise NotImplementedError

    def sketch_centerline(self):
        """Adds a centerline to the current model document."""
        raise NotImplementedError

    def sketch_chamfer(self):
        """Obsolete. Superseded by ISketchManager::CreateChamfer."""
        raise NotImplementedError

    def sketch_circle(self):
        """Obsolete. Superseded by IModelDoc2::CreateCircle2."""
        raise NotImplementedError

    def sketch_constrain_coincident(self):
        """Makes the selected sketch entities coincident."""
        raise NotImplementedError

    def sketch_constrain_concentric(self):
        """Makes the selected sketch entities concentric."""
        raise NotImplementedError

    def sketch_constrain_parallel(self):
        """Makes the selected sketch entities parallel."""
        raise NotImplementedError

    def sketch_constrain_perp(self):
        """Makes the selected sketch entities perpendicular."""
        raise NotImplementedError

    def sketch_constrain_tangent(self):
        """Makes the selected entities tangent."""
        raise NotImplementedError

    def sketch_constraints_del(self):
        """Deletes the specified relationship (constraint) on the currently selected sketch item."""
        raise NotImplementedError

    def sketch_constraints_del_all(self):
        """Deletes all of the constraints on the currently selected sketch segment."""
        raise NotImplementedError

    def sketch_convert_iso_curves(self):
        """Converts ISO-parametric curves on a selected surface into a sketch entity."""
        raise NotImplementedError

    def sketch_fillet(self):
        """Obsolete. Superseded by IModelDoc2::SketchFillet2."""
        raise NotImplementedError

    def sketch_fillet1(self):
        """Obsolete. Superseded by IModelDoc2::SketchFillet2."""
        raise NotImplementedError

    def sketch_fillet2(self):
        """Obsolete. Superseded by ISketchManager::CreateFillet."""
        raise NotImplementedError

    def sketch_mirror(self):
        """Creates new entities that are mirror images of the selected entities."""
        raise NotImplementedError

    def sketch_modify_flip(self):
        """Flips the active or selected sketch about the specified coordinate system axis."""
        raise NotImplementedError

    def sketch_modify_rotate(self):
        """Rotates the coordinate system of the active or selected sketch."""
        raise NotImplementedError

    def sketch_modify_scale(self):
        """Scales the active or selected sketch."""
        raise NotImplementedError

    def sketch_modify_translate(self):
        """Translates the coordinate system of the active or selected sketch."""
        raise NotImplementedError

    def sketch_offset(self):
        """Obsolete. Superseded by IModelDoc2::SketchOffset2."""
        raise NotImplementedError

    def sketch_offset2(self):
        """Obsolete. Superseded by ISketchManager::SketchOffset."""
        raise NotImplementedError

    def sketch_offset_edges(self):
        """Offsets the edges of the selected entities."""
        raise NotImplementedError

    def sketch_offset_entities(self):
        """Obsolete. Superseded by IModelDoc2::SketchOffsetEntities2."""
        raise NotImplementedError

    def sketch_offset_entities2(self):
        """Generates entities in the active sketch by offsetting the selected geometry by the specified amount."""
        raise NotImplementedError

    def sketch_parabola(self):
        """Obsolete. Superseded by ISketchManager::CreateParabola."""
        raise NotImplementedError

    def sketch_point(self):
        """Obsolete. Superseded by IModelDoc2::CreatePoint2 and IModelDoc2::ICreatePoint2."""
        raise NotImplementedError

    def sketch_polygon(self):
        """Obsolete. Superseded by ISketchManager::CreatePolygon."""
        raise NotImplementedError

    def sketch_rectangle(self):
        """Obsolete. Superseded by ISketchManager::CreateCornerRectangle."""
        raise NotImplementedError

    def sketch_rectangle_at_any_angle(self):
        """Obsolete. Superseded by ISketchManager::Create3PointCornerRectangle."""
        raise NotImplementedError

    def sketch_spline(self):
        """Starts a spline, or continues one, using the specified point."""
        raise NotImplementedError

    def sketch_spline_by_eqn_params(self):
        """Obsolete. Superseded by IModelDoc2::ISketchSplineByEqnParams2."""
        raise NotImplementedError

    def sketch_spline_by_eqn_params2(self):
        """Obsolete. Superseded by ISketchManager::CreateSplineByEqnParams."""
        raise NotImplementedError

    def sketch_tangent_arc(self):
        """Creates a tangent arc in the current model document."""
        raise NotImplementedError

    def sketch_trim(self):
        """Obsolete. Superseded by ISketchManager::SketchExtend and ISketchManager::SketchTrim."""
        raise NotImplementedError

    def sketch_undo(self):
        """Undoes the last sketch command."""
        raise NotImplementedError

    def sketch_use_edge(self):
        """Obsolete. Superseded by ISketchManager::SketchUseEdge."""
        raise NotImplementedError

    def sketch_use_edge2(self):
        """Obsolete. Superseded by ISketchManager::SketchUseEdge."""
        raise NotImplementedError

    def sketch_use_edge_ctrline(self):
        """Uses this centerline in sketch."""
        raise NotImplementedError

    def sk_tools_auto_constr(self):
        """Automatically constrains the active sketch."""
        raise NotImplementedError

    def split_closed_segment(self):
        """Obsolete. Superseded by ISketchManager::SplitClosedSegment."""
        raise NotImplementedError

    def split_open_segment(self):
        """Obsolete. Superseded by ISketchManager::SplitOpenSegment."""
        raise NotImplementedError

    def show_configuration2(self, configuration_name: str) -> bool:
        """
        Shows the named configuration by switching to that configuration and making it the active configuration.

        Reference:
        https://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html
        """
        in_configuration_name = VARIANT(VT_BSTR, configuration_name)

        com_object = self.com_object.ShowConfiguration2(in_configuration_name)
        return bool(com_object)

    def toolbars(self):
        """Turns the specified SOLIDWORKS toolbars on and off."""
        raise NotImplementedError

    def tools_distance(self):
        """Computes distance."""
        raise NotImplementedError

    def tools_grid(self):
        """Shows and hides the grid in this model document."""
        raise NotImplementedError

    def tools_macro(self):
        """Not implemented."""
        raise NotImplementedError

    def tools_mass_props(self):
        """Calculates the mass properties."""
        raise NotImplementedError

    def tools_sketch_scale(self):
        """Scales a sketch."""
        raise NotImplementedError

    def tools_sketch_translate(self):
        """Translates a sketch."""
        raise NotImplementedError

    def unblank_ref_geom(self):
        """Shows the selected, hidden reference geometry in the graphics window."""
        raise NotImplementedError

    def unblank_sketch(self):
        """Shows a hidden sketch."""
        raise NotImplementedError

    def underive_sketch(self):
        """Changes a sketch to underived."""
        raise NotImplementedError

    def unlock(self):
        """Reverses IModelDoc2::Lock and changes the status bar message to Process Complete."""
        raise NotImplementedError

    def unlock_all_external_references(self):
        """Unlocks all external references."""
        raise NotImplementedError

    def unlock_frame_point(self):
        """Obsolete. Not superseded."""
        raise NotImplementedError

    def user_favors(self):
        """Specifies whether geometric relations are automatically created as you add sketch entities."""
        raise NotImplementedError

    def user_preferences(self):
        """Obsolete. Superseded by other methods (see documentation)."""
        raise NotImplementedError

    def version_history(self):
        """Gets an array of strings indicating the versions in which this document was saved."""
        raise NotImplementedError

    def view_constraint(self):
        """Shows the constraints for the current model document."""
        raise NotImplementedError

    def view_disp_coordinate_systems(self):
        """Toggles the display of coordinate systems on and off."""
        raise NotImplementedError

    def view_display_curvature(self):
        """Toggles the display of surface curvature on and off."""
        raise NotImplementedError

    def view_display_faceted(self):
        """Sets the display mode to show the facets that make up a shaded picture of STL output."""
        raise NotImplementedError

    def view_display_hiddengreyed(self):
        """Sets the display mode to Hidden Lines Visible."""
        raise NotImplementedError

    def view_display_hiddenremoved(self):
        """Sets the display mode to Hidden Lines Removed."""
        raise NotImplementedError

    def view_display_shaded(self):
        """Sets the display mode to Shaded."""
        raise NotImplementedError

    def view_display_wireframe(self):
        """Sets the display mode to Wireframe."""
        raise NotImplementedError

    def view_disp_origins(self):
        """Toggles the display of origins on and off."""
        raise NotImplementedError

    def view_disp_refaxes(self):
        """Toggles the display of reference axes on and off."""
        raise NotImplementedError

    def view_disp_refplanes(self):
        """Toggles the display of reference planes on and off."""
        raise NotImplementedError

    def view_disp_refpoints(self):
        """Shows and hides the reference points for the current model document."""
        raise NotImplementedError

    def view_disp_temp_refaxes(self):
        """Toggles the display of temporary reference axes on and off."""
        raise NotImplementedError

    def view_ogl_shading(self):
        """Sets the display subsystem to use OpenGL."""
        raise NotImplementedError

    def view_orientation_undo(self):
        """Undoes previous view orientation changes made interactively by the user."""
        raise NotImplementedError

    def view_rotate(self):
        """Rotates the view of the current model."""
        raise NotImplementedError

    def view_rotate_minus_x(self):
        """Dynamically rotates the view around X in a negative direction with the current increment."""
        raise NotImplementedError

    def view_rotate_minus_y(self):
        """Dynamically rotates the view around Y in a negative direction with the current increment."""
        raise NotImplementedError

    def view_rotate_minus_z(self):
        """Dynamically rotates the view around Z in a negative direction with the current increment."""
        raise NotImplementedError

    def view_rotate_plus_x(self):
        """Rotates the view around X in a positive direction with the current increment."""
        raise NotImplementedError

    def view_rotate_plus_y(self):
        """Rotates the view around Y in a positive direction with the current increment."""
        raise NotImplementedError

    def view_rotate_plus_z(self):
        """Rotates the view around Z in a positive direction with the current increment."""
        raise NotImplementedError

    def view_rot_x_minus_ninety(self):
        """Dynamically rotates the view by negative 90 about X."""
        raise NotImplementedError

    def view_rot_x_plus_ninety(self):
        """Dynamically rotates the view by 90 about X."""
        raise NotImplementedError

    def view_rot_y_minus_ninety(self):
        """Dynamically rotates the view by negative 90 about Y."""
        raise NotImplementedError

    def view_rot_y_plus_ninety(self):
        """Dynamically rotates the view by 90 about Y."""
        raise NotImplementedError

    def view_rw_shading(self):
        """Sets the display subsystem to use RenderWare."""
        raise NotImplementedError

    def view_translate(self):
        """Translates the view."""
        raise NotImplementedError

    def view_translate_minus_x(self):
        """Dynamically shifts the view left."""
        raise NotImplementedError

    def view_translate_minus_y(self):
        """Dynamically shifts the view down."""
        raise NotImplementedError

    def view_translate_plus_x(self):
        """Dynamically shifts the view right."""
        raise NotImplementedError

    def view_translate_plus_y(self):
        """Dynamically shifts the view up."""
        raise NotImplementedError

    def view_zoomin(self):
        """Zooms the current view in by a factor of 20%."""
        raise NotImplementedError

    def view_zoomout(self):
        """Zooms the current view out by a factor of 20%."""
        raise NotImplementedError

    def view_zoomto(self):
        """Zooms the view to the selected box."""
        raise NotImplementedError

    def view_zoomto2(self):
        """Zooms to the specified region."""
        raise NotImplementedError

    def view_zoomtofit(self):
        """Obsolete. Superseded by IModelDoc2::ViewZoomtofit2."""
        raise NotImplementedError

    def view_zoomtofit2(self):
        """Zooms the currently active view to fit the screen."""
        raise NotImplementedError

    def view_zoom_to_selection(self):
        """Zooms the display to the selection."""
        raise NotImplementedError

    def window_redraw(self) -> None:
        """
        Redraws the current window.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html
        """
        self.com_object.WindowRedraw
