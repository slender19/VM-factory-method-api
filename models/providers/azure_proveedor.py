from typing import Dict
from ..vms import VMAzure, VM
from .proveedor import Proveedor

class AzureProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMAzure(
            tamaño_maquina=parametros["tamaño_maquina"],
            resource_group=parametros["resource_group"],
            imagen=parametros["imagen"],
            red_virtual=parametros["red_virtual"],
        )
