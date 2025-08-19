from pathlib import Path

drawing_template = next(Path("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates").glob("*.DRWDOT"))


def run(part_file_location: Path, drawing_file_location: Path):
    from pyswx import PySWX
    from pyswx.api.sldworks.interfaces.i_drawing_doc import IDrawingDoc
    from pyswx.api.swconst.enumerations import SWDocumentTypesE
    from pyswx.api.swconst.enumerations import SWDwgPaperSizesE
    from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE
    from pyswx.api.swconst.enumerations import SWSaveAsVersionE

    swx = PySWX().application
    swx.close_all_documents(include_unsaved=True)

    model_doc = swx.new_document(drawing_template, SWDwgPaperSizesE.SW_DWG_PAPER_A4SIZE)
    assert model_doc
    model_doc.extension.save_as_3(
        name=drawing_file_location,
        version=SWSaveAsVersionE.SW_SAVE_AS_CURRENT_VERSION,
        options=None,
        export_data=None,
        advanced_save_as_options=None,
    )

    model_doc = swx.activate_doc_3(
        drawing_file_location, use_user_preferences=False, option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC
    )
    drw_doc = IDrawingDoc(model_doc.com_object)
    assert drw_doc.com_object

    drw_doc.create_draw_view_from_model_view_3(part_file_location, "*Front", 0.2, 0.15, 0)
    drw_doc.create_draw_view_from_model_view_3(part_file_location, "*Top", 0.2, -0.05, 0)
    drw_doc.create_draw_view_from_model_view_3(part_file_location, "*Isometric", 0.45, 0.1, 0)

    model_doc.extension.save_as_3(
        name=drawing_file_location,
        version=SWSaveAsVersionE.SW_SAVE_AS_CURRENT_VERSION,
        options=None,
        export_data=None,
        advanced_save_as_options=None,
    )
    swx.close_all_documents(include_unsaved=True)
