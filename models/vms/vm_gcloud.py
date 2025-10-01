from typing import Dict
from .vm import VM

class VMGoogleCloud(VM):
    def __init__(self, machine_type: str, zona: str, disco_base: str, proyecto: str):
        super().__init__("Google Cloud VM")
        self.machine_type = machine_type
        self.zona = zona
        self.disco_base = disco_base
        self.proyecto = proyecto

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo_maquina,
            "machine_type": self.machine_type,
            "zona": self.zona,
            "disco_base": self.disco_base,
            "proyecto": self.proyecto,
        }
