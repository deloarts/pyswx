from tests.conftest import TEST_DRAWING_01
from tests.conftest import TEST_DRAWING_01_EXPORT_PDF


def test_open_drawing():
    """"""

    from pyswx import PySWX
    from pyswx.api.sldworks.interfaces.i_drawing_doc import IDrawingDoc
    from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
    from pyswx.tools.drawing_tools import open_drawing

    swx = PySWX().application
    swx.close_all_documents(include_unsaved=True)

    drw_model, drw_doc = open_drawing(swx=swx, drawing_path=TEST_DRAWING_01, document_specification=None)

    assert isinstance(drw_model, IModelDoc2)
    assert isinstance(drw_doc, IDrawingDoc)

    swx.close_all_documents(include_unsaved=True)


def test_export_drawing():
    """"""
    from pyswx import PySWX
    from pyswx.tools.drawing_tools import export_drawing

    swx = PySWX().application
    swx.close_all_documents(include_unsaved=True)

    export_drawing(
        swx=swx,
        drawing_path=TEST_DRAWING_01,
        export_type="pdf",
        export_path=TEST_DRAWING_01_EXPORT_PDF,
        close_document=True,
        save_document=False,
        view_pdf_afterwards=False,
        document_specification=None,
    )

    assert TEST_DRAWING_01_EXPORT_PDF.exists()

    swx.close_all_documents(include_unsaved=True)
