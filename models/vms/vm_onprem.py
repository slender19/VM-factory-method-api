from typing import Dict
from .vm import VM

class VMOnPremise(VM):
    def __init__(self, cpu: str, ram: str, disco: str, red_fisica: str):
        super().__init__("On Premise VM")
        self.cpu = cpu
        self.ram = ram
        self.disco = disco
        self.red_fisica = red_fisica

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo_maquina,
            "cpu": self.cpu,
            "ram": self.ram,
            "disco": self.disco,
            "red_fisica": self.red_fisica,
        }
