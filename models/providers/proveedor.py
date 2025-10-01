from abc import ABC, abstractmethod
from typing import Dict
from ..vms.vm import VM

# Clase abstracta Creator
class Proveedor(ABC):
    @abstractmethod
    def crear_vm(self, parametros: Dict) -> VM:
        pass
