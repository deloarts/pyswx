"""
ISldWorks

Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API.

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html

Status: 🟠
"""

from pathlib import Path
from typing import Tuple

from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_DISPATCH
from pythoncom import VT_I4
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_export_pdf_data import IExportPdfData
from pyswx.api.sldworks.interfaces.i_frame import IFrame
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
from pyswx.api.swconst.enumerations import SWApplicationTypeE
from pyswx.api.swconst.enumerations import SWCloseReopenErrorE
from pyswx.api.swconst.enumerations import SWCloseReopenOptionE
from pyswx.api.swconst.enumerations import SWDocActivateErrorE
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWExportDataFileType_e
from pyswx.api.swconst.enumerations import SWFileLoadErrorE
from pyswx.api.swconst.enumerations import SWFileLoadWarningE
from pyswx.api.swconst.enumerations import SWOpenDocOptionsE
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE


class ISldWorks(BaseInterface):
    """
    ISldWorks Interface Members
    """

    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"ISldWorks({self.com_object})"

    @property
    def active_doc(self) -> IModelDoc2 | None:
        """
        Gets the currently active document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html
        """
        com_object = self.com_object.ActiveDoc
        if com_object:
            return IModelDoc2(com_object)
        return None

    @property
    def application_type(self) -> SWApplicationTypeE:
        """
        Gets the type of this SOLIDWORKS application.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ApplicationType.html
        """
        com_object = self.com_object.ApplicationType
        return SWApplicationTypeE(value=com_object)

    @property
    def command_in_progress(self):
        raise NotImplementedError

    @command_in_progress.setter
    def command_in_progress(self, value):
        raise NotImplementedError

    @property
    def enable_background_processing(self):
        raise NotImplementedError

    @enable_background_processing.setter
    def enable_background_processing(self, value):
        raise NotImplementedError

    @property
    def enable_file_menu(self):
        raise NotImplementedError

    @enable_file_menu.setter
    def enable_file_menu(self, value):
        raise NotImplementedError

    @property
    def frame_height(self):
        raise NotImplementedError

    @frame_height.setter
    def frame_height(self, value):
        raise NotImplementedError

    @property
    def frame_left(self):
        raise NotImplementedError

    @frame_left.setter
    def frame_left(self, value):
        raise NotImplementedError

    @property
    def frame_state(self):
        raise NotImplementedError

    @frame_state.setter
    def frame_state(self, value):
        raise NotImplementedError

    @property
    def frame_top(self):
        raise NotImplementedError

    @frame_top.setter
    def frame_top(self, value):
        raise NotImplementedError

    @property
    def frame_width(self):
        raise NotImplementedError

    @frame_width.setter
    def frame_width(self, value):
        raise NotImplementedError

    @property
    def i_active_doc2(self):
        raise NotImplementedError

    @i_active_doc2.setter
    def i_active_doc2(self, value):
        raise NotImplementedError

    @property
    def startup_process_completed(self) -> bool:
        """
        Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~startupprocesscompleted.html
        """
        com_object = self.com_object.StartupProcessCompleted
        return bool(com_object)

    @property
    def task_pane_is_pinned(self):
        raise NotImplementedError

    @task_pane_is_pinned.setter
    def task_pane_is_pinned(self, value):
        raise NotImplementedError

    @property
    def user_control(self) -> bool:
        """
        Gets and sets whether the user has control over the application.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~usercontrol.html
        """
        com_object = self.com_object.UserControl
        return bool(com_object)

    @user_control.setter
    def user_control(self, value: bool):
        self.com_object.UserControl = value

    @property
    def user_control_background(self):
        raise NotImplementedError

    @user_control_background.setter
    def user_control_background(self, value):
        raise NotImplementedError

    @property
    def user_type_lib_references(self):
        raise NotImplementedError

    @user_type_lib_references.setter
    def user_type_lib_references(self, value):
        raise NotImplementedError

    @property
    def visible(self) -> bool:
        """
        Gets whether the SOLIDWORKS application is visible.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html
        """
        return self.com_object.Visible

    @visible.setter
    def visible(self, value: bool):
        self.com_object.Visible = VARIANT(VT_BOOL, value)

    def activate_doc_3(
        self,
        name: Path,
        use_user_preferences: bool,
        option: SWRebuildOnActivationOptionsE,
    ) -> IModelDoc2:
        """
        Activates a loaded document and rebuilds it as specified.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~activatedoc3.html
        """

        in_name = VARIANT(VT_BSTR, str(name))
        in_use_user_preferences = VARIANT(VT_BOOL, use_user_preferences)
        in_option = VARIANT(VT_I4, option)

        out_errors = VARIANT(VT_BYREF | VT_I4, None)

        model_doc = self.com_object.ActivateDoc3(
            in_name,
            in_use_user_preferences,
            in_option,
            out_errors,
        )

        if out_errors.value != 0:
            out_errors = SWDocActivateErrorE(value=out_errors.value)
            self.logger.error(out_errors)
            raise Exception(out_errors)

        return IModelDoc2(model_doc)

    def activate_task_pane(self):
        """
        Activates the specified task pane.
        """
        raise NotImplementedError

    def add_callback(self):
        """
        Registers a general purpose callback handler.
        """
        raise NotImplementedError

    def add_file_open_item3(self):
        """
        Adds file types to the File > Open dialog box.
        """
        raise NotImplementedError

    def add_file_save_as_item2(self):
        """
        Adds a file type to the SOLIDWORKS File > Save As dialog box.
        """
        raise NotImplementedError

    def add_item_to_third_party_popup_menu(self):
        """
        Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in.
        """
        raise NotImplementedError

    def add_item_to_third_party_popup_menu2(self):
        """
        Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in.
        """
        raise NotImplementedError

    def add_menu(self):
        """
        Adds a menu item to a SOLIDWORKS menu for DLL applications.
        """
        raise NotImplementedError

    def add_menu_item5(self):
        """
        Adds a menu item and image to the SOLIDWORKS user interface.
        """
        raise NotImplementedError

    def add_menu_popup_item3(self):
        """
        Adds a menu item and zero or more submenus to shortcut menus of entities
        of the specified type in documents of the specified type.
        """
        raise NotImplementedError

    def add_menu_popup_item4(self):
        """
        Adds a menu item and zero or more submenus to shortcut menus of features
        of the specified type in documents of the specified type.
        """
        raise NotImplementedError

    def add_toolbar5(self):
        """
        Creates a Windows-style dockable toolbar.
        """
        raise NotImplementedError

    def add_toolbar_command2(self):
        """
        Specifies the application functions to call when a toolbar button is
        clicked or sets a separator.
        """
        raise NotImplementedError

    def allow_failed_feature_creation(self):
        """
        Sets whether to allow the creation of a feature that has rebuild errors.
        """
        raise NotImplementedError

    def arrange_icons(self):
        """
        Arranges the icons in SOLIDWORKS.
        """
        raise NotImplementedError

    def arrange_windows(self):
        """
        Arranges the open windows in SOLIDWORKS.
        """
        raise NotImplementedError

    def block_skinning(self):
        """
        Blocks skinning a window, which prevents a window from looking like a
        SOLIDWORKS window.
        """
        raise NotImplementedError

    def callback(self):
        """
        Allows an out-of-process executable or a SOLIDWORKS macro to call back a function in a SOLIDWORKS add-in DLL.
        """
        raise NotImplementedError

    def checkpoint_converted_document(self):
        """
        Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used.
        """
        raise NotImplementedError

    def close_all_documents(self, include_unsaved: bool) -> bool:
        """
        Closes all open documents in the SOLIDWORKS session.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~closealldocuments.html
        """
        in_include_unsaved = VARIANT(VT_BOOL, include_unsaved)

        com_object = self.com_object.CloseAllDocuments(in_include_unsaved)
        return bool(com_object)

    def close_and_reopen(self, doc: IModelDoc2, option: SWCloseReopenOptionE) -> Tuple[SWCloseReopenErrorE, IModelDoc2]:
        """
        Closes and reopens the specified drawing document without unloading its references from memory.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.html
        """
        if doc.get_type() != SWDocumentTypesE.SW_DOC_DRAWING:
            raise Exception("Document is not a drawing")

        in_doc = VARIANT(VT_DISPATCH, doc.com_object)
        in_option = VARIANT(VT_I4, option.value)

        out_new_doc = VARIANT(VT_BYREF | VT_DISPATCH, None)

        com_object = self.com_object.CloseAndReopen(in_doc, in_option, out_new_doc)
        return (SWCloseReopenErrorE(com_object), IModelDoc2(out_new_doc.value))

    def close_and_reopen2(
        self, doc: IModelDoc2, option: SWCloseReopenOptionE
    ) -> Tuple[SWCloseReopenErrorE, IModelDoc2]:
        """
        Closes and reopens the specified drawing document without unloading its references from memory.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen2.html
        """
        if doc.get_type() != SWDocumentTypesE.SW_DOC_DRAWING:
            raise Exception("Document is not a drawing")

        in_doc = VARIANT(VT_DISPATCH, doc.com_object)
        in_option = VARIANT(VT_I4, option.value)

        out_new_doc = VARIANT(VT_BYREF | VT_DISPATCH, None)

        com_object = self.com_object.CloseAndReopen2(in_doc, in_option, out_new_doc)
        return (SWCloseReopenErrorE(com_object), IModelDoc2(out_new_doc.value))

    def close_doc(self, name: str) -> None:
        """
        Closes the specified document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html
        """
        in_name = VARIANT(VT_BSTR, name)

        self.com_object.CloseDoc(in_name)

    def close_user_notification(self):
        """
        Closes the specified user notification.
        """
        raise NotImplementedError

    def command(self):
        """
        Opens the specified dialog or file.
        """
        raise NotImplementedError

    def copy_appearance(self):
        """
        Copies the appearance of the specified entity to the clipboard.
        """
        raise NotImplementedError

    def copy_document(self):
        """
        Copies a document and optionally updates references to it.
        """
        raise NotImplementedError

    def create_new_window(self):
        """
        Creates a client window containing the active document.
        """
        raise NotImplementedError

    def create_property_manager_page(self):
        """
        Creates a PropertyManager page.
        """
        raise NotImplementedError

    def create_taskpane_view3(self):
        """
        Creates an application-level Task Pane view.
        """
        raise NotImplementedError

    def define_attribute(self):
        """
        Creates an attribute definition, which is the first step in generating attributes.
        """
        raise NotImplementedError

    def define_message_bar(self):
        """
        Called by a SOLIDWORKS add-in, creates a message bar definition object.
        """
        raise NotImplementedError

    def define_user_notification(self):
        """
        Called by a SOLIDWORKS add-in, creates a user notification definition object.
        """
        raise NotImplementedError

    def display_status_bar(self):
        """
        Sets whether to display the status bar.
        """
        raise NotImplementedError

    def document_visible(self):
        """
        Allows the application to control the display of a document in a window upon creation or retrieval.
        """
        raise NotImplementedError

    def download_from_my_solidworks_settings(self):
        """
        Downloads the specified SOLIDWORKS Connected settings to SOLIDWORKS Desktop.
        """
        raise NotImplementedError

    def drag_toolbar_button(self):
        """
        Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup
        toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar.
        """
        raise NotImplementedError

    def drag_toolbar_button_from_command_id(self):
        """
        Copies a button to a toolbar using a command ID.
        """
        raise NotImplementedError

    def enum_documents2(self):
        """
        Gets a list of documents currently open in the application.
        """
        raise NotImplementedError

    def exit_app(self) -> None:
        """
        Shuts down SOLIDWORKS.

        Remarks:
        This method is not normally used with macros (*.swp) because it shuts down your SOLIDWORKS session.
        For C++ and Visual Basic projects, ending your program does not guarantee that the SOLIDWORKS processes are closed. During development, you can determine whether processes are left running by checking the Process Viewer and looking for any SLDWORKS processes. Typically, you do not want the SLDWORKS process running after your program has ended. Calling this method ensures that no SOLIDWORKS processes are left running when your program ends.
        However, the CreateObject ("SldWorks.Application") statement used to start up the SOLIDWORKS software either creates a new SOLIDWORKS session or it attaches to an existing SOLIDWORKS session. If the end-user currently has an open SOLIDWORKS session, then your program attaches to it. Performing this method ends that session.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.html
        """
        self.com_object.ExitApp()

    def export_hole_wizard_item(self):
        """
        Exports data for the specified Hole Wizard standard.
        """
        raise NotImplementedError

    def export_toolbox_item(self):
        """
        Exports data for the specified Toolbox standard.
        """
        raise NotImplementedError

    def frame(self) -> IFrame:
        """
        Gets the SOLIDWORKS main frame.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html
        """
        return IFrame(self.com_object.Frame)

    def get_3dexperience_state(self):
        """
        Gets the current state of SOLIDWORKS Connected.
        """
        raise NotImplementedError

    def get_active_configuration_name(self, file_path_name: Path) -> str:
        """
        Gets the name of the active configuration in the specified SOLIDWORKS document.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~getactiveconfigurationname.html
        """
        if file_path_name.exists():
            in_file_path_name = VARIANT(VT_BSTR, str(file_path_name))
            return str(self.com_object.GetActiveConfigurationName(in_file_path_name))
        else:
            raise FileNotFoundError(file_path_name)

    def get_active_display_pane(self):
        """
        Gets the active Display Pane.
        """
        raise NotImplementedError

    def get_add_in_object(self):
        """
        Gets an add-in object for the specified SOLIDWORKS add-in.
        """
        raise NotImplementedError

    def get_apply_selection_filter(self):
        """
        Gets the current state of the selection filter.
        """
        raise NotImplementedError

    def get_batch_uploaded_files_info(self):
        """
        Gets the files uploaded to 3DEXPERIENCE during a batch process.
        """
        raise NotImplementedError

    def get_build_numbers2(self):
        """
        Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application.
        """
        raise NotImplementedError

    def get_button_position(self):
        """
        Gets the center coordinates of the specified SOLIDWORKS toolbar button.
        """
        raise NotImplementedError

    def get_collision_detection_manager(self):
        """
        Gets the collision detection manager.
        """
        raise NotImplementedError

    def get_color_table(self):
        """
        Gets a color table from the SOLIDWORKS application.
        """
        raise NotImplementedError

    def get_command_id(self):
        """
        Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., toolbar button).
        """
        raise NotImplementedError

    def get_command_manager(self):
        """
        Gets the CommandManager for the specified add-in.
        """
        raise NotImplementedError

    def get_configuration_count(self):
        """
        Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed.
        """
        raise NotImplementedError

    def get_configuration_names(self):
        """
        Gets the names of the configurations in this SOLIDWORKS document, whether opened or closed.
        """
        raise NotImplementedError

    def get_current_file_user(self):
        """
        Gets the name of the user who has the specified document open.
        """
        raise NotImplementedError

    def get_current_language(self):
        """
        Gets the current language used by SOLIDWORKS.
        """
        raise NotImplementedError

    def get_current_license_type(self):
        """
        Gets the type of license for the current SOLIDWORKS session.
        """
        raise NotImplementedError

    def get_current_macro_path_folder(self):
        """
        Gets the name of the folder where the macro resides.
        """
        raise NotImplementedError

    def get_current_macro_path_name(self):
        """
        Gets the path name for the macro currently running.
        """
        raise NotImplementedError

    def get_current_working_directory(self):
        """
        Gets the current working directory being used by the SOLIDWORKS application.
        """
        raise NotImplementedError

    def get_data_folder(self):
        """
        Gets the data directory name currently used by SOLIDWORKS.
        """
        raise NotImplementedError

    def get_document_count(self) -> int:
        """
        Gets the number of open documents in the current SOLIDWORKS session.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~getdocumentcount.html
        """
        com_object = self.com_object.GetDocumentCount
        return int(com_object)

    def get_document_dependencies2(self):
        """
        Gets all of the model dependencies for a document.
        """
        raise NotImplementedError

    def get_documents(self):
        """
        Gets the open documents in this SOLIDWORKS session.
        """
        raise NotImplementedError

    def get_document_template(self):
        """
        Gets the name of the document template usable in NewDocument or INewDocument2.
        """
        raise NotImplementedError

    def get_document_visible(self):
        """
        Gets the visibility of the document to open.
        """
        raise NotImplementedError

    def get_environment(self):
        """
        Gets the IEnvironment object.
        """
        raise NotImplementedError

    def get_error_messages(self):
        """
        Gets the last 20 messages issued by SOLIDWORKS in the current session.
        """
        raise NotImplementedError

    def get_executable_path(self):
        """
        Gets the path to the SOLIDWORKS executable, sldworks.exe.
        """
        raise NotImplementedError

    def get_export_file_data(self, file_type: SWExportDataFileType_e) -> IExportPdfData:
        """
        Gets the data interface for the specified file type to which to export one or more drawing sheets.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetExportFileData.html
        """
        in_file_type = VARIANT(VT_I4, file_type.value)

        com_object = self.com_object.GetExportFileData(in_file_type)

        return IExportPdfData(com_object)

    def get_file_plmid(self):
        """
        Gets the Product Lifecycle Management (PLM) ID of the specified file stored in 3DEXPERIENCE.
        """
        raise NotImplementedError

    def get_first_document(self):
        """
        Gets the document that was opened first in this SOLIDWORKS session.
        """
        raise NotImplementedError

    def get_gtol_format_data(self):
        """
        Gets the Gtol format and XML schema versions supported by this version of SOLIDWORKS.
        """
        raise NotImplementedError

    def get_gtol_frame_xml_schema(self):
        """
        Gets the XML schema for Gtol frame symbol XML.
        """
        raise NotImplementedError

    def get_hole_standards_data(self):
        """
        Gets the hole standards for the specified hole type.
        """
        raise NotImplementedError

    def get_image_size(self):
        """
        Gets small, medium, and large image sizes for the current DPI setting of the display device.
        Also returns the default image size for images not based on the SOLIDWORKS icon size setting.
        """
        raise NotImplementedError

    def get_import_file_data(self):
        """
        Gets the IGES or DXF/DWG import data for the specified file.
        """
        raise NotImplementedError

    def get_interface_brightness_theme_colors(self):
        """
        Gets the theme and background colors of the SOLIDWORKS interface.
        """
        raise NotImplementedError

    def get_last_save_error(self):
        """
        Gets the last save error issued by Microsoft in the current session.
        """
        raise NotImplementedError

    def get_last_toolbar_id(self):
        """
        Gets the ID of the last toolbar added to the CommandManager.
        """
        raise NotImplementedError

    def get_latest_supported_file_version(self):
        """
        Gets the version number that this instance of SOLIDWORKS can read and write.
        """
        raise NotImplementedError

    def get_line_styles(self):
        """
        Gets all of the line styles in the specified file.
        """
        raise NotImplementedError

    def get_localized_menu_name(self):
        """
        Gets a localized menu name for the specified menu ID.
        """
        raise NotImplementedError

    def get_macro_methods(self):
        """
        Gets the names of the modules in the specified macro.
        """
        raise NotImplementedError

    def get_mass_properties2(self):
        """
        Gets the mass properties from the specified document and configuration.
        """
        raise NotImplementedError

    def get_material_database_count(self):
        """
        Gets the number of material databases.
        """
        raise NotImplementedError

    def get_material_databases(self):
        """
        Gets the names of the material databases.
        """
        raise NotImplementedError

    def get_material_schema_path_name(self):
        """
        Gets the path of the XML material schema file.
        """
        raise NotImplementedError

    def get_math_utility(self):
        """
        Gets the IMathUtility interface.
        """
        raise NotImplementedError

    def get_menu_strings(self):
        """
        Gets the name of the parent menu for the specified menu command.
        """
        raise NotImplementedError

    def get_modeler(self):
        """
        Gets the IModeler interface.
        """
        raise NotImplementedError

    def get_mouse_drag_mode(self):
        """
        Gets whether the specified command-mouse mode is in effect.
        """
        raise NotImplementedError

    def get_open_doc_spec(self, file_name: Path) -> IDocumentSpecification:
        """
        Gets the specifications to use when opening a model document.

        Args:
            file_name (Path): Path and file name of the document to open

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~getopendocspec.html
        """
        com_object = self.com_object.GetOpenDocSpec(str(file_name))
        return IDocumentSpecification(com_object)

    def get_open_document(self):
        """
        Gets the open document with the specified name.
        """
        raise NotImplementedError

    def get_open_document_by_name(self):
        """
        Gets the open document by the specified name.
        """
        raise NotImplementedError

    def get_opened_file_info(self):
        """
        Gets the name and options of the last model successfully opened by SOLIDWORKS.
        """
        raise NotImplementedError

    def get_open_file_name2(self):
        """
        Prompts the user for the name of the file to open.
        """
        raise NotImplementedError

    def get_preview_bitmap(self):
        """
        Gets the preview bitmap for the specified configuration of a document.
        """
        raise NotImplementedError

    def get_preview_bitmap_file(self):
        """
        Gets the preview bitmap of a document and saves it as a Windows bitmap file.
        """
        raise NotImplementedError

    def get_process_id(self):
        """
        Gets the process ID of the current SOLIDWORKS session.
        """
        raise NotImplementedError

    def get_ray_trace_renderer(self):
        """
        Gets a ray-trace rendering engine.
        """
        raise NotImplementedError

    def get_recent_files(self):
        """
        Gets a list of the most recently used files.
        """
        raise NotImplementedError

    def get_routing_settings(self):
        """
        Gets the routing settings.
        """
        raise NotImplementedError

    def get_running_command_info(self):
        """
        Gets command or PropertyManager page ID, title, and UI activation state.
        """
        raise NotImplementedError

    def get_safe_array_utility(self):
        """
        Gets the ISafeArrayUtility object.
        """
        raise NotImplementedError

    def get_save_to_3dexperience_options(self):
        """
        Initializes save options for a SOLIDWORKS Connected document.
        """
        raise NotImplementedError

    def get_search_folders(self):
        """
        Gets the current folder search path for referenced documents.
        """
        raise NotImplementedError

    def get_selection_filter(self):
        """
        Gets the current selection filter settings for the specified item type.
        """
        raise NotImplementedError

    def get_selection_filters(self):
        """
        Gets all active selection filters.
        """
        raise NotImplementedError

    def get_sso_formatted_url(self):
        """
        Formats the specified URL for single sign-on (SSO).
        """
        raise NotImplementedError

    def get_template_sizes(self):
        """
        Gets the sheet properties from a template document.
        """
        raise NotImplementedError

    def get_toolbar_dock2(self):
        """
        Gets the docking state of the toolbar.
        """
        raise NotImplementedError

    def get_toolbar_state2(self):
        """
        Gets the state of the toolbar.
        """
        raise NotImplementedError

    def get_toolbar_visibility(self):
        """
        Gets whether the specified toolbar is visible.
        """
        raise NotImplementedError

    def get_user_preference_double_value(self):
        """
        Gets system default user preference values of type double.
        """
        raise NotImplementedError

    def get_user_preference_integer_value(self):
        """
        Gets system default user preference values of type integer.
        """
        raise NotImplementedError

    def get_user_preference_string_list_value(self):
        """
        Gets the name of the DXF mapping file or string list user preferences.
        """
        raise NotImplementedError

    def get_user_preference_string_value(self):
        """
        Gets system default user preference values of type string.
        """
        raise NotImplementedError

    def get_user_preference_toggle(self):
        """
        Gets document default user preference toggle values.
        """
        raise NotImplementedError

    def get_user_progress_bar(self):
        """
        Gets a user progress indicator object.
        """
        raise NotImplementedError

    def get_user_type_lib_reference_count(self):
        """
        Gets the number of user-specified type library references.
        """
        raise NotImplementedError

    def get_user_unit(self):
        """
        Gets an empty IUserUnit object of the specified type.
        """
        raise NotImplementedError

    def hide_bubble_tooltip(self):
        """
        Hides the bubble tooltip displayed by ISldWorks::ShowBubbleTooltipAt2.
        """
        raise NotImplementedError

    def hide_toolbar2(self):
        """
        Hides a toolbar created with ISldWorks::AddToolbar5.
        """
        raise NotImplementedError

    def i_activate_doc3(self):
        """
        Activates a document that has already been loaded.
        This document becomes the active document and a pointer to it is returned.
        """
        raise NotImplementedError

    def i_copy_document(self):
        """
        Copies a document and optionally updates references to it.
        """
        raise NotImplementedError

    def i_create_property_manager_page(self):
        """
        Creates a PropertyManager page.
        """
        raise NotImplementedError

    def i_define_attribute(self):
        """
        Creates an attribute definition, which is the first step in generating attributes.
        """
        raise NotImplementedError

    def i_get_color_table(self):
        """
        Gets a color table from the SOLIDWORKS application.
        """
        raise NotImplementedError

    def i_get_configuration_names(self):
        """
        Gets the names of the configurations in this SOLIDWORKS document, opened or closed.
        """
        raise NotImplementedError

    def i_get_document_dependencies2(self):
        """
        Gets all of the model dependencies for a document.
        """
        raise NotImplementedError

    def i_get_document_dependencies_count2(self):
        """
        Gets the size of the array needed for a call to i_get_document_dependencies2.
        """
        raise NotImplementedError

    def i_get_documents(self):
        """
        Gets the open documents in this SOLIDWORKS session.
        """
        raise NotImplementedError

    def i_get_environment(self):
        """
        Gets the IEnvironment object.
        """
        raise NotImplementedError

    def i_get_first_document2(self):
        """
        Gets the document opened first in this SOLIDWORKS session.
        """
        raise NotImplementedError

    def i_get_mass_properties2(self):
        """
        Gets the mass properties from the specified document and configuration.
        """
        raise NotImplementedError

    def i_get_material_databases(self):
        """
        Gets the names of the material databases.
        """
        raise NotImplementedError

    def i_get_math_utility(self):
        """
        Gets the IMathUtility interface.
        """
        raise NotImplementedError

    def i_get_modeler(self):
        """
        Gets the IModeler interface.
        """
        raise NotImplementedError

    def i_get_open_document_by_name2(self):
        """
        Gets the open document with the specified name.
        """
        raise NotImplementedError

    def i_get_ray_trace_renderer(self):
        """
        Gets a ray-trace rendering engine.
        """
        raise NotImplementedError

    def i_get_selection_filters(self):
        """
        Gets all active selection filters.
        """
        raise NotImplementedError

    def i_get_selection_filters_count(self):
        """
        Gets the number of active selection filters.
        """
        raise NotImplementedError

    def i_get_template_sizes(self):
        """
        Gets the sheet properties from a template document.
        """
        raise NotImplementedError

    def i_get_user_type_lib_references(self):
        """
        Gets the specified user-specified type library references.
        """
        raise NotImplementedError

    def i_get_user_unit(self):
        """
        Gets an empty IUserUnit object of the specified type.
        """
        raise NotImplementedError

    def i_get_version_history_count(self):
        """
        Gets the size of the array required to hold data returned by IVersionHistory.
        """
        raise NotImplementedError

    def i_move_document(self):
        """
        Moves a document and optionally updates references to it.
        """
        raise NotImplementedError

    def import_hole_wizard_item(self):
        """
        Imports data for the specified Hole Wizard standard.
        """
        raise NotImplementedError

    def import_toolbox_item(self):
        """
        Imports data for the specified Toolbox standard.
        """
        raise NotImplementedError

    def i_new_document2(self):
        """
        Creates a new document based on the specified template.
        """
        raise NotImplementedError

    def install_quick_tip_guide(self):
        """
        Implements your add-in's copy of the Quick Tips.
        """
        raise NotImplementedError

    def i_remove_user_type_lib_references(self):
        """
        Removes the user-specified type library references.
        """
        raise NotImplementedError

    def is_background_processing_completed(self):
        """
        Gets whether SOLIDWORKS has finished background processing a drawing document.
        """
        raise NotImplementedError

    def is_command_enabled(self):
        """
        Gets whether the specified command is enabled.
        """
        raise NotImplementedError

    def i_set_selection_filters(self):
        """
        Sets the status for multiple selection filters.
        """
        raise NotImplementedError

    def i_set_user_type_lib_references(self):
        """
        Sets the user-specified type library references.
        """
        raise NotImplementedError

    def is_rapid_draft(self):
        """
        Gets whether the specified drawing file is in SOLIDWORKS Detached format.
        """
        raise NotImplementedError

    def is_same(self):
        """
        Gets whether the two specified objects are the same object.
        """
        raise NotImplementedError

    def is_task_pane_expanded(self):
        """
        Gets whether the Task Pane is expanded.
        """
        raise NotImplementedError

    def is_task_pane_visible(self):
        """
        Gets whether the Task Pane is visible.
        """
        raise NotImplementedError

    def i_version_history(self):
        """
        Gets a list of strings indicating the versions in which a model was saved.
        """
        raise NotImplementedError

    def load_add_in(self):
        """
        Loads the specified add-in in SOLIDWORKS.
        """
        raise NotImplementedError

    def load_admin_settings_file(self):
        """
        Loads the specified *.sldsettings file into SOLIDWORKS Connected.
        """
        raise NotImplementedError

    def load_file4(self):
        """
        Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect.
        """
        raise NotImplementedError

    def move_document(self):
        """
        Moves a document and optionally updates references to it.
        """
        raise NotImplementedError

    def new_document(self):
        """
        Creates a new document based on the specified template.
        """
        raise NotImplementedError

    def open_doc6(
        self,
        file_name: Path,
        file_type: SWDocumentTypesE,
        options: SWOpenDocOptionsE | None = None,
        configuration: str | None = None,
    ) -> IModelDoc2:
        """
        Opens an existing document and returns a pointer to the document object.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~opendoc6.html
        """

        if not file_name.exists():
            raise FileNotFoundError(file_name)

        in_file_name = VARIANT(VT_BSTR, str(file_name))
        in_file_type = VARIANT(VT_I4, file_type.value)
        in_options = VARIANT(VT_I4, options.value) if options else 0
        in_configuration = VARIANT(VT_BSTR, configuration) if configuration else ""

        out_errors = VARIANT(VT_BYREF | VT_I4, None)
        out_warnings = VARIANT(VT_BYREF | VT_I4, None)

        com_object = self.com_object.OpenDoc6(
            in_file_name,
            in_file_type,
            in_options,
            in_configuration,
            out_errors,
            out_warnings,
        )

        if out_warnings.value != 0:
            out_warnings = SWFileLoadWarningE(value=out_warnings.value)
            self.logger.warning(out_warnings.name)

        if out_errors.value != 0:
            out_errors = SWFileLoadErrorE(value=out_errors.value)
            self.logger.error(out_errors)
            raise Exception(out_errors)

        return IModelDoc2(com_object)

    def open_doc7(self, specification: IDocumentSpecification) -> IModelDoc2 | None:
        """
        Opens an existing document using a specification object and returns a pointer to the document object.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~opendoc7.html
        """
        if not specification.file_name.exists():
            raise FileNotFoundError(specification.file_name)

        in_specification = VARIANT(VT_DISPATCH, specification.com_object)
        com_object = self.com_object.OpenDoc7(in_specification)

        if in_specification.value.Warning != 0:
            try:
                out_warnings = SWFileLoadWarningE(value=in_specification.value.Warning)
                self.logger.warning(out_warnings.name)
            except ValueError:
                self.logger.error(f"Unknown SWFileLoadWarning: {in_specification.value.Warning}")

        if in_specification.value.Error != 0:
            out_errors = SWFileLoadErrorE(value=in_specification.value.Error)
            self.logger.error(out_errors)
            raise Exception(out_errors)

        return IModelDoc2(com_object) if com_object else None

    def paste_appearance(self):
        """
        Applies an appearance copied to the clipboard to the specified entity.
        """
        raise NotImplementedError

    def post_message_to_application(self):
        """
        Posts a message to the application that invoked this method.
        """
        raise NotImplementedError

    def post_message_to_application_x64(self):
        """
        Posts a message to the application in 64-bit environments.
        """
        raise NotImplementedError

    def pre_select_dwg_template_size(self):
        """
        Sets which drawing template to use when creating a drawing.
        """
        raise NotImplementedError

    def preset_new_drawing_parameters(self):
        """
        Presets drawing template and sheet size parameters to avoid showing the sheet format dialog.
        """
        raise NotImplementedError

    def preview_doc(self):
        """
        Displays a preview of a document to a specified window.
        """
        raise NotImplementedError

    def preview_doc_x64(self):
        """
        Displays a preview of a document in 64-bit applications.
        """
        raise NotImplementedError

    def quit_doc(self, name: Path) -> None:
        """
        Closes the specified document without saving changes.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html
        """
        self.com_object.QuitDoc(str(name))

    def record_line(self):
        """
        Adds a line of code to a VBA macro and the SOLIDWORKS journal file.
        """
        raise NotImplementedError

    def record_line_csharp(self):
        """
        Adds a line of code to a C# macro and the SOLIDWORKS journal file.
        """
        raise NotImplementedError

    def record_line_vbnet(self):
        """
        Adds a line of code to a VB.NET macro and the SOLIDWORKS journal file.
        """
        raise NotImplementedError

    def refresh_quick_tip_window(self):
        """
        Notifies SOLIDWORKS that the add-in's state changed to refresh quick tip content.
        """
        raise NotImplementedError

    def refresh_taskpane_content(self):
        """
        Refreshes the Design Library tab in the Task Pane.
        """
        raise NotImplementedError

    def register_third_party_popup_menu(self):
        """
        Registers a third-party shortcut menu.
        """
        raise NotImplementedError

    def register_tracking_definition(self):
        """
        Registers a tracking definition.
        """
        raise NotImplementedError

    def remove_callback(self):
        """
        Unregisters a general-purpose callback handler.
        """
        raise NotImplementedError

    def remove_file_open_item2(self):
        """
        Removes a file type from the File > Open dialog box added previously.
        """
        raise NotImplementedError

    def remove_file_save_as_item2(self):
        """
        Removes a file type from the File > Save As dialog box added previously.
        """
        raise NotImplementedError

    def remove_from_menu(self):
        """
        Removes the specified command from menus and toolbars.
        """
        raise NotImplementedError

    def remove_from_popup_menu(self):
        """
        Removes a menu item from specified context-sensitive (popup) menus.
        """
        raise NotImplementedError

    def remove_item_from_third_party_popup_menu(self):
        """
        Removes a menu item and icon from a third-party shortcut menu.
        """
        raise NotImplementedError

    def remove_menu(self):
        """
        Removes a menu item from the specified document frame.
        """
        raise NotImplementedError

    def remove_menu_popup_item2(self):
        """
        Removes an item on a pop-up (shortcut) menu.
        """
        raise NotImplementedError

    def remove_toolbar2(self):
        """
        Removes a toolbar created with AddToolbar5.
        """
        raise NotImplementedError

    def remove_user_type_lib_references(self):
        """
        Removes the user-specified type library references.
        """
        raise NotImplementedError

    def replace_referenced_document(self):
        """
        Replaces a referenced document.
        """
        raise NotImplementedError

    def reset_preset_drawing_parameters(self):
        """
        Resets drawing template behavior to default after preset parameters were set.
        """
        raise NotImplementedError

    def reset_untitled_count(self):
        """
        Resets the index of untitled documents.
        """
        raise NotImplementedError

    def restore_settings(self):
        """
        Restores SOLIDWORKS settings from a specified *.sldreg file.
        """
        raise NotImplementedError

    def resume_skinning(self):
        """
        Resumes skinning windows.
        """
        raise NotImplementedError

    def revision_number(self):
        """
        Gets the version number of the SOLIDWORKS installation.
        """
        raise NotImplementedError

    def run_attached_macro(self):
        """
        Runs the specified attached macro, module, and procedure.
        """
        raise NotImplementedError

    def run_batch_save_process(self):
        """
        Batch saves files to 3DEXPERIENCE.
        """
        raise NotImplementedError

    def run_command(self):
        """
        Runs the specified SOLIDWORKS command.
        """
        raise NotImplementedError

    def run_macro2(self):
        """
        Runs a macro from a project file.
        """
        raise NotImplementedError

    def save_settings(self):
        """
        Saves SOLIDWORKS settings to a specified *.sldreg file.
        """
        raise NotImplementedError

    def send_msg_to_user2(self):
        """
        Displays a message box that requires user interaction before continuing.
        """
        raise NotImplementedError

    def set_addin_callback_info2(self):
        """
        Sets add-in callback commands.
        """
        raise NotImplementedError

    def set_apply_selection_filter(self):
        """
        Sets the current state of the selection filter.
        """
        raise NotImplementedError

    def set_current_working_directory(self):
        """
        Sets the current working directory used by SOLIDWORKS.
        """
        raise NotImplementedError

    def set_missing_reference_path_name(self):
        """
        Sets the missing reference file name for ReferenceNotFoundNotify event.
        """
        raise NotImplementedError

    def set_mouse_drag_mode(self):
        """
        Sets the command-mouse mode.
        """
        raise NotImplementedError

    def set_multiple_filenames_prompt(self):
        """
        Sets new filenames to open in response to a prompt event.
        """
        raise NotImplementedError

    def set_new_filename(self):
        """
        Sets the name of the new SOLIDWORKS file.
        """
        raise NotImplementedError

    def set_prompt_filename2(self):
        """
        Sets the file to open in response to a SOLIDWORKS event.
        """
        raise NotImplementedError

    def set_search_folders(self):
        """
        Sets folder search paths for referenced documents.
        """
        raise NotImplementedError

    def set_selection_filter(self):
        """
        Sets the selection filter for the specified item type.
        """
        raise NotImplementedError

    def set_selection_filters(self):
        """
        Sets the status for multiple selection filters.
        """
        raise NotImplementedError

    def set_third_party_popup_menu_state(self):
        """
        Shows or hides a third-party popup (shortcut) menu.
        """
        raise NotImplementedError

    def set_toolbar_dock2(self):
        """
        Sets the docking state of a toolbar.
        """
        raise NotImplementedError

    def set_toolbar_visibility(self):
        """
        Sets whether a specified toolbar is visible.
        """
        raise NotImplementedError

    def set_user_preference_double_value(self):
        """
        Sets a system default user preference value (double).
        """
        raise NotImplementedError

    def set_user_preference_integer_value(self):
        """
        Sets a system default user preference value (integer).
        """
        raise NotImplementedError

    def set_user_preference_string_list_value(self):
        """
        Sets the name of the DXF mapping files.
        """
        raise NotImplementedError

    def set_user_preference_string_value(self):
        """
        Sets a system default user preference value (string).
        """
        raise NotImplementedError

    def set_user_preference_toggle(self):
        """
        Sets a system default user preference toggle.
        """
        raise NotImplementedError

    def show_batch_save_to_3dexperience_dlg(self):
        """
        Opens a dialog to save files to 3DEXPERIENCE.
        """
        raise NotImplementedError

    def show_bubble_tooltip(self):
        """
        Displays a bubble tooltip and flashes a toolbar button.
        """
        raise NotImplementedError

    def show_bubble_tooltip_at2(self):
        """
        Displays a bubble ToolTip at the specified screen location.
        """
        raise NotImplementedError

    def show_help(self):
        """
        Displays the specified Help topic.
        """
        raise NotImplementedError

    def show_third_party_popup_menu(self):
        """
        Sets where to show a third-party pop-up (shortcut) menu.
        """
        raise NotImplementedError

    def show_toolbar2(self):
        """
        Displays a toolbar. (Obsolete, not superseded)
        """
        raise NotImplementedError

    def show_user_notification(self):
        """
        Shows a user notification for a SOLIDWORKS add-in.
        """
        raise NotImplementedError

    def solidworks_explorer(self):
        """
        Starts SOLIDWORKS Explorer application.
        """
        raise NotImplementedError

    def uninstall_quick_tip_guide(self):
        """
        Uninstalls your add-in's Quick Tips.
        """
        raise NotImplementedError

    def unload_addin(self):
        """
        Unloads the specified add-in from SOLIDWORKS.
        """
        raise NotImplementedError

    def upload_to_my_solidworks_settings(self):
        """
        Uploads specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected.
        """
        raise NotImplementedError

    def version_history(self):
        """
        Gets a list of strings indicating the versions in which a model was saved.
        """
        raise NotImplementedError
