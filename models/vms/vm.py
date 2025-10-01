from abc import ABC, abstractmethod
from typing import Dict

# Clase base Producto
class VM(ABC):
    def __init__(self, tipo_maquina: str):
        self.tipo_maquina = tipo_maquina

    @abstractmethod
    def get_info(self) -> Dict:
        pass
