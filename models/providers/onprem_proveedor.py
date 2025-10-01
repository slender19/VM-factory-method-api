from typing import Dict
from ..vms import VMOnPremise, VM
from .proveedor import Proveedor

class OnPremiseProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMOnPremise(
            cpu=parametros["cpu"],
            ram=parametros["ram"],
            disco=parametros["disco"],
            red_fisica=parametros["red_fisica"],
        )
