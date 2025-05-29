#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pythoncom
from win32com.client import Dispatch

from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.const import VERSION

__version__ = VERSION


class PySWX:
    def __init__(self, version: int | None = None):
        if version is None:
            self.version = f"SldWorks.Application"
        else:
            self.version = f"SldWorks.Application.{version - 2012 + 20}"

    @property
    def application(self) -> ISldWorks:
        return ISldWorks(Dispatch(self.version))

    @property
    def application_co_initialise(self) -> ISldWorks:
        return ISldWorks(Dispatch(self.version, pythoncom.CoInitialize()))
