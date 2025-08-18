from tests.conftest import TEST_PART_01
from tests.conftest import TEST_PART_01_EXPORT_STEP


def test_open_part():
    """"""

    from pyswx import PySWX
    from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
    from pyswx.api.sldworks.interfaces.i_part_doc import IPartDoc
    from pyswx.tools.part_tools import open_part

    swx = PySWX().application
    swx.close_all_documents(include_unsaved=True)

    part_model, part_doc = open_part(swx=swx, part_path=TEST_PART_01, document_specification=None)

    assert isinstance(part_model, IModelDoc2)
    assert isinstance(part_doc, IPartDoc)

    swx.close_all_documents(include_unsaved=True)


def test_export_part():
    """"""

    from pyswx import PySWX
    from pyswx.tools.part_tools import export_part

    swx = PySWX().application
    swx.close_all_documents(include_unsaved=True)

    export_part(
        swx=swx,
        part_path=TEST_PART_01,
        export_type="step",
        export_path=TEST_PART_01_EXPORT_STEP,
        close_document=True,
        save_document=False,
        document_specification=None,
    )

    assert TEST_PART_01_EXPORT_STEP.exists()

    swx.close_all_documents(include_unsaved=True)
