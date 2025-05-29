"""
swAppNotify_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html

Status: 🟢
"""

from enum import IntEnum


class SWAppNotifyE(IntEnum):
    """Application notifications."""

    SW_APP_FILE_OPEN_NOTIFY = 1  # Obsolete
    SW_APP_FILE_CLOSE_NOTIFY = 32  # FileCloseNotify
    SW_APP_FILE_NEW_NOTIFY = 2  # Obsolete
    SW_APP_FILE_NEW_NOTIFY2 = 12  # FileNewNotify2
    SW_APP_FILE_NEW_PRE_NOTIFY = 26  # FileNewPreNotify
    SW_APP_FILE_OPEN_NOTIFY2 = 13  # FileOpenNotify2
    SW_APP_FILE_OPEN_POST_NOTIFY = 22  # FileOpenPostNotify
    SW_APP_FILE_OPEN_PRE_NOTIFY = 21  # FileOpenPreNotify
    SW_APP_ACTIVE_DOC_CHANGE_NOTIFY = 4  # ActiveDocChangeNotify
    SW_APP_ACTIVE_MODEL_DOC_CHANGE_NOTIFY = 5  # ActiveModelDocChangeNotify
    SW_APP_BACKGROUND_PROCESSING_START_NOTIFY = 33  # BackgroundProcessingStartNotify
    SW_APP_BACKGROUND_PROCESSING_END_NOTIFY = 34  # BackgroundProcessingEndNotify
    SW_APP_BEGIN_3D_INTERCONNECT_TRANSLATION_NOTIFY = (
        37  # Begin3DInterconnectTranslationNotify
    )
    SW_APP_END_3D_INTERCONNECT_TRANSLATION_NOTIFY = (
        38  # End3DInterconnectTranslationNotify
    )
    SW_APP_BEGIN_RECORD_NOTIFY = 24  # Not used
    SW_APP_END_RECORD_NOTIFY = 25  # Not used
    SW_APP_BEGIN_TRANSLATION_NOTIFY = 16  # BeginTranslationNotify
    SW_APP_END_TRANSLATION_NOTIFY = 16  # EndTranslationNotify
    SW_APP_COMMAND_CLOSE_NOTIFY = 29  # CommandCloseNotify
    SW_APP_COMMAND_OPEN_PRE_NOTIFY = 31  # CommandOpenPreNotify
    SW_APP_DESTROY_NOTIFY = 3  # DestroyNotify
    SW_APP_DISPLAY_PANE_ACTIVATION_NOTIFY = 45  # DisplayPaneActivationNotify
    SW_APP_DOCUMENT_CONVERSION_NOTIFY = 9  # DocumentConversionNotify
    SW_APP_DOCUMENT_LOAD_NOTIFY = 27  # Obsolete
    SW_APP_DOCUMENT_LOAD_NOTIFY2 = 28  # DocumentLoadNotify2
    SW_APP_INTERFACE_BRIGHTNESS_THEME_CHANGE_NOTIFY = (
        35  # InterfaceBrightnessThemeChangeNotify
    )
    SW_APP_JOURNAL_WRITE_NOTIFY = 27  # Not used
    SW_APP_LIGHT_PM_CREATE_NOTIFY = -1  # Not used (no value given)
    SW_APP_LIGHT_SHEET_CREATE_NOTIFY = 18  # LightSheetCreateNotify
    SW_APP_LIGHTWEIGHT_COMPONENT_OPEN_NOTIFY = 10  # Not used
    SW_APP_NON_NATIVE_FILE_OPEN_NOTIFY = 7  # NonNativeFileOpenNotify
    SW_APP_ON_IDLE_NOTIFY = 20  # OnIdleNotify
    SW_APP_PROMPT_FOR_FILENAME_NOTIFY = 15  # PromptForFilenameNotify
    SW_APP_PROMPT_FOR_MULTIPLE_FILENAMES_NOTIFY = 30  # PromptForMultipleFileNamesNotify
    SW_APP_PROPERTY_SHEET_CREATE_NOTIFY = 6  # PropertySheetCreateNotify
    SW_APP_REFERENCED_FILE_PRE_NOTIFY = 23  # ReferencedFilePreNotify
    SW_APP_REFERENCED_FILE_PRE_NOTIFY2 = 36  # ReferencedFilePreNotify2
    SW_APP_REFERENCE_NOT_FOUND_NOTIFY = 14  # ReferenceNotFoundNotify
    SW_APP_STANDARDS_DATABASE_CHANGE_NOTIFY = 19  # Not used
    SW_APP_TASK_PANE_COLLAPSE_NOTIFY = 44  # TaskPaneCollapseNotify
    SW_APP_TASK_PANE_EXPAND_NOTIFY = 43  # TaskPaneExpandNotify
    SW_APP_TASK_PANE_HIDE_NOTIFY = 41  # TaskPaneHideNotify
    SW_APP_TASK_PANE_PINNED_NOTIFY = 39  # TaskPanePinnedNotify
    SW_APP_TASK_PANE_SHOW_NOTIFY = 42  # TaskPaneShowNotify
    SW_APP_TASK_PANE_UNPINNED_NOTIFY = 40  # TaskPaneUnpinnedNotify
