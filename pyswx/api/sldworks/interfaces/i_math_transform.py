"""
IMathTransform Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html

Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface


class IMathTransform(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IMathTransform({self.com_object})"
