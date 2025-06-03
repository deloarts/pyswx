"""
IModelDoc2 Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html

Status: 🔴
"""

from pathlib import Path
from typing import List

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_configuration import IConfiguration
from pyswx.api.sldworks.interfaces.i_configuration_manager import IConfigurationManager
from pyswx.api.sldworks.interfaces.i_model_doc_extension import IModelDocExtension
from pyswx.api.swconst.enumerations import (
    SWDocumentTypesE,
    SWFileSaveErrorE,
    SWFileSaveWarningE,
    SWSaveAsOptionsE,
)
from pythoncom import VT_BYREF, VT_I4
from win32com.client import VARIANT


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
        https://help.solidworks.com/2018/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.imodeldoc2~configurationmanager.html
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

    def insert_object(self) -> None:
        """
        Activates the Microsoft Insert Object dialog.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertObject.html
        """
        self.com_object.InsertObject()

    def get_configuration_names(self) -> List[str]:
        """
        Gets the names of the configurations in this document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationNames.html
        """
        com_object = self.com_object.GetConfigurationNames
        return [str(name) for name in com_object] if com_object else []

    def get_path_name(self) -> Path:
        """
        Gets the full path name for this document, including the file name.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html
        """
        com_object = self.com_object.GetPathName
        return Path(com_object)

    def get_type(self) -> SWDocumentTypesE:
        """Gets the type of the document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html
        """
        com_object = self.com_object.GetType
        return SWDocumentTypesE(com_object)

    def save_3(self, options: SWSaveAsOptionsE | None) -> bool:
        """
        Saves the current document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.html
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
            self.logger.error(out_errors)
            raise Exception(out_errors)

        return com_object

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def activate_feature_mgr_view(self):
        """Obsolete. Superseded by IFeatureMgrView::ActivateView."""
        raise NotImplementedError

    def activate_selected_feature(self):
        """Activates the selected feature for editing."""
        raise NotImplementedError

    def add_configuration(self):
        """Obsolete. Superseded by IModelDoc2::AddConfiguration3."""
        raise NotImplementedError

    def add_configuration2(self):
        """Obsolete. Superseded by IModelDoc2::AddConfiguration3."""
        raise NotImplementedError

    def add_configuration3(self):
        """Adds a new configuration to this model document."""
        raise NotImplementedError

    def add_custom_info(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_custom_info2(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_custom_info3(self):
        """Obsolete. Superseded by IModelDocExtension::CustomPropertyManager."""
        raise NotImplementedError

    def add_diameter_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddDiameterDimension2."""
        raise NotImplementedError

    def add_diameter_dimension2(self):
        """Adds a diameter dimension at the specified location for the selected item."""
        raise NotImplementedError

    def add_dimension(self):
        """Obsolete. Superseded by IModelDoc2::AddDimension2."""
        raise NotImplementedError

    def add_dimension2(self):
        """Creates a display dimension at the specified location for selected entities."""
        raise NotImplementedError

    def add_feature_mgr_view(self):
        """Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3."""
        raise NotImplementedError

    def add_feature_mgr_view2(self):
        """Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3."""
        raise NotImplementedError

    def add_feature_mgr_view3(self):
        """Adds the specified tab to the FeatureManager design tree view."""
        raise NotImplementedError

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
