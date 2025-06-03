# PySWX

A python wrapper for the SolidWorks API.

![state](https://img.shields.io/badge/State-wip-red.svg?style=for-the-badge)
![version](https://img.shields.io/github/v/release/deloarts/pyswx?style=for-the-badge&color=orange)

[![python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
![sldworks](https://img.shields.io/badge/SolidWorks-2024+-blue.svg?style=for-the-badge)
![OS](https://img.shields.io/badge/OS-WIN11-blue.svg?style=for-the-badge)

<img src="https://github.com/deloarts/pyswx/blob/main/assets/images/icon.png?raw=true" width="200" height="200">

**PySWX** is a wrapper for the SolidWorks API 2024, based on the [official help site](https://help.solidworks.com/2024/english/api/sldworksapiprogguide/Welcome.htm). It provides a typed interface and some useful features.

> ✏️ This project is in an early stage of development. The API is not complete and the documentation is not yet available. If you want to contribute to this project, please open an issue or a pull request. To see the current state of this project, check out the [development branch](https://github.com/deloarts/pyswx/tree/development).

## 1 installation

### 1.1 system requirements

- Windows 11
- SolidWorks 2024 or later
- [Python 3.12](https://www.python.org/downloads/)

> ✏️ These requirements aren't strict, you can try and use **PySWX** on older or more recent systems, but it isn't tested on these.

### 1.2 pip

```powershell
python -m pip install pyswx
```

or

```powershell
python -m pip install git+ssh://git@github.com/deloarts/pyswx.git
```

If you're using poetry add it to you **pyproject.toml** file using:

```powershell
poetry add pyswx
```

## 2 usage

**PySWX** works with [VS Code Intellisense](https://code.visualstudio.com/docs/editing/intellisense) and provides type hints for the SolidWorks API:

![/assets/images/intellisense.png](https://github.com/deloarts/pyswx/blob/main/assets/images/intellisense.png?raw=true)

All methods and classes are documented with docstrings, which can be viewed in the Intellisense popup.
Like in the example above you can refer to the official documentation of [IModelDocExtension](https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html).

> ✏️ **PySWX** uses PEP8 style for methods, classes and variables.
>
> ✏️ **PySWX** is not completed, methods that aren't implemented yet will raise a `NotImplementedError` when called.

### 2.1 example: open a part

```python
# Open a part and export it as step

from pathlib import Path

from pyswx import PySWX
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsVersionE

PATH_TO_PART = Path("C:\\path\\to\\your\\part.SLDPRT")

swx = PySWX(version=2024).application

part_open_spec = swx.get_open_doc_spec(file_name=PATH_TO_PART)
part_open_spec.document_type = SWDocumentTypesE.SW_DOC_PART
part_open_spec.use_light_weight_default = True
part_open_spec.light_weight = True
part_open_spec.silent = True

part_model = swx.open_doc7(specification=part_open_spec)

if part_open_spec.warning is not None:
    swx.logger.warning(part_open_spec.warning.name)

if part_open_spec.error is not None:
    swx.logger.error(part_open_spec.error.name)
    raise Exception(part_open_spec.error.name)

part_model = swx.activate_doc_3(
    name=part_model.get_path_name(),
    use_user_preferences=False,
    option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
)

step_path = part_model.get_path_name().with_suffix(".step")

part_model.extension.save_as_3(
    name=step_path,
    version=SWSaveAsVersionE.SW_SAVE_AS_CURRENT_VERSION,
    options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT,
    export_data=None,
    advanced_save_as_options=None,
)
```

For more examples see the [examples](https://github.com/deloarts/pyswx/tree/main/examples) folder.

### 2.2 tools

**PySWX** comes with some tools to help you work with the SolidWorks API, e.g. the above code can be shortcutted with:

```python
from pyswx import PySWX
from pyswx.tools.part_tools import export_step

PATH_TO_PART = Path("C:\\path\\to\\your\\part.SLDPRT")

swx = PySWX().application
export_step(swx, PATH_TO_PART)
```

For all tools check out the [tools]([/tools](https://github.com/deloarts/pyswx/tree/main/pyswx/tools)) folder.

### 2.3 com object

**PySWX** provides a way to access the SolidWorks COM object directly. This is useful if you want to use methods that are not yet implemented in **PySWX**:

```python
...
doc_model = swx.open_doc7(specification=part_open_spec)
doc_model_com_object = doc_model.com_object # Here we access the actual com object
configuration_names_com_object = doc_model_com_object.GetConfigurationNames

# Note: Notice how the case of the object after the com_object changes from snake_case to PascalCase.
# The com object is the actual SolidWorks COM object, so you can use it like you would use the SolidWorks API in VBA. 
```

To convert a com object to a **PySWX** object, you can pass it to the interface:

```python
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
doc_model = IModelDoc2(doc_model_com_object)
```

### 2.4 divergencies

The SolidWorks API exposes methods that work with `ByRef [out]` arguments, which are not supported in Python.
Such a methods is, for example, the [GetConfigurationParams](https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.iconfigurationmanager~getconfigurationparams.html) method:

```VB
Function GetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByRef Params As System.Object, _
   ByRef Values As System.Object _
) As System.Boolean
```

This method sets the `Params` and the `Values` via the given arguments, and returns only a bool (in this case `True`, if the method was successful).
As this isn't possible in Python, the equivalent **PySWX** method returns a `Tuple`, the method return value and all ByRef-argument values:

```Python
type ParamsRetrieved = bool
type ParamNames = List[str]
type ParamValues = List[str]

def get_configuration_params(self, config_name: str) -> Tuple[ParamsRetrieved, ParamNames, ParamValues]:
    ...
```

### 2.5 obsolete methods and properties

The SolidWorks API exposes obsolete methods and properties. Those are not included in **PySWX**.
You are still able to access them via the `com_object`.

## 3 developing

For developing you would, additionally to the system requirements, need to install:

- [Poetry](https://python-poetry.org/docs/master/#installation)
- [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)

### 3.1 repository

#### 3.1.1 cloning

Clone the repo to your local machine:

```powershell
cd $HOME
New-Item -Path '.\git\pyswx' -ItemType Directory
cd .\git\pyswx\
git clone git@github.com:deloarts/pyswx.git
```

Or use GitHub Desktop.

#### 3.1.2 main branch protection

> ❗️ Never develop new features and fixes in the main branch!

The main branch is protected: it's not allowed to make changes directly to it. Create a new branch in order work on issues. The new branch should follow the naming convention from below.

#### 3.1.3 branch naming convention

1. Use grouping tokens at the beginning of your branch names, such as:
    - feature: A new feature that will be added to the project
    - fix: For bugfixes
    - tests: Adding or updating tests
    - docs: For updating the docs
    - wip: Work in progress, won't be finished soon
    - junk: Just for experimenting
2. Use slashes `/` as delimiter in branch names (`feature/docket-export`)
3. Avoid long descriptive names, rather refer to an issue
4. Do not use bare numbers as leading parts (`fix/108` is bad, `fix/issue108` is good)

#### 3.1.4 issues

Use the issue templates for creating an issue. Please don't open a new issue if you haven't met the requirements and add as much information as possible. Further:

- Format your code in an issue correctly with three backticks, see the [markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- Add the full error trace.
- Do not add screenshots for code or traces.

### 3.2 poetry

#### 3.2.1 setup

If you prefer the environment inside the projects root, use:

```powershell
poetry config virtualenvs.in-project true
```

> ⚠️ Make sure not to commit the virtual environment to GitHub. See **.gitignore** to find out which folders are ignored.

#### 3.2.2 install

Install all dependencies (assuming you are inside the projects root folder):

```powershell
poetry install
```

Update packages with:

```powershell
poetry update
```

#### 3.2.3 tests

Tests are done with pytest. For testing with poetry run:

```powershell
poetry run pytest
```

> ⚠️ Test discovery in VS Code only works when SolidWorks is running and all documents are closed!

### 3.3 status indicators

Each api module has its own status indicator in the module docstring:

indicator | status | description
--- | --- | ---
🟢 | Completed | The module represents the SolidWorks API completely
🟠 | Methods Imported | All SolidWorks API methods are imported, but aren't fully implemented yet
🔴 | Not Completed | The module is not completed and some SolidWorks API methods may be missing

### 3.4 new revision checklist

1. Update **dependencies**: `poetry update`
2. Update the **version** in
   - [pyproject.toml](pyproject.toml)
   - [__ init __.py](pyswx/__init__.py)
   - [README.md](README.md)
3. Run all **tests**: `poetry run pytest`
4. Check **pylint** output: `poetry run pylint pyswx/`
5. Update the **lockfile**: `poetry lock`
6. Update the **requirements.txt**: `poetry export -f requirements.txt -o requirements.txt`
7. **Build** the package: `poetry build`

## 4 license

[MIT License](LICENSE)

## 5 changelog

[**v0.1.0**](https://github.com/deloarts/pyswx/releases/tag/v0.1.0): Add new interfaces and properties for IComponent2, IConfiguration, IModelDoc2, ISldWorks and ISwAddin.  
[**v0.0.1**](https://github.com/deloarts/pyswx/releases/tag/v0.0.1): First stable version.  

## 6 to do

Using VS Code [Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) to keep track of to-dos.
