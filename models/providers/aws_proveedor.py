from typing import Dict
from ..vms import VMAWS, VM
from .proveedor import Proveedor

class AWSProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMAWS(
            tipo_instancia=parametros["tipo_instancia"],
            region=parametros["region"],
            vpc=parametros["vpc"],
            ami=parametros["ami"],
        )
