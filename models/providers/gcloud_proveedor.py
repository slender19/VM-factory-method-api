from typing import Dict
from ..vms import VMGoogleCloud, VM
from .proveedor import Proveedor

class GoogleCloudProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMGoogleCloud(
            machine_type=parametros["machine_type"],
            zona=parametros["zona"],
            disco_base=parametros["disco_base"],
            proyecto=parametros["proyecto"],
        )
