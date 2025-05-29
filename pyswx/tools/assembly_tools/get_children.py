"""
ASSEMBLY TOOLS // GET CHILDREN
"""

from pathlib import Path
from typing import List

from pyswx.api.sldworks.interfaces.i_component_2 import IComponent2
from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.tools.assembly_tools.open_assembly import open_assembly


def get_children(
    swx: ISldWorks,
    assembly_path_or_model: Path | IModelDoc2,
    close_document: bool = False,
    save_document: bool = True,
    document_specification: IDocumentSpecification | None = None,
) -> List[IComponent2]:
    """
    Returns the first level of children in the assembly.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        assembly_path_or_model (Path): The path to the assembly or the IModelDoc2-PySWX instance.
        close_document (bool, optional): Whether to close the document after export. Defaults to False.
        save_document (bool, optional): Whether to save the document before closing. Defaults to True.
        document_specification (IDocumentSpecification | None, optional): The document specification to use. Defaults to None.

    Remarks:
        The following document specification options are set:
        - document_type: SWDocumentTypesE.SW_DOC_PART
        - use_light_weight_default: True
        - light_weight: True
        - silent: True
        - ignore_hidden_components: True

        Document is saved silently.

        The returned IModelDoc2 instance might be None if the child component is suppressed, lightweight or not loaded
        in memory by SolidWorks.

    Raises:
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not an assembly.
    """
    if isinstance(assembly_path_or_model, Path):
        assembly_model, _ = open_assembly(
            swx=swx,
            assembly_path=assembly_path_or_model,
            document_specification=document_specification,
        )
    else:
        assembly_model = assembly_path_or_model

    children: List[IComponent2] = []
    root_component = (
        assembly_model.configuration_manager.active_configuration.get_root_component3(
            resolve=True
        )
    )

    if root_component:
        for child in root_component.get_children():
            swx.logger.debug(child.name2, child.get_path_name())
            children.append(child)

    if save_document:
        assembly_model.save_3(options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT)

    if close_document:
        swx.quit_doc(name=assembly_model.get_path_name())

    return children
