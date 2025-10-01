from typing import Dict
from .vm import VM

class VMAWS(VM):
    def __init__(self, tipo_instancia: str, region: str, vpc: str, ami: str):
        super().__init__("AWS VM")
        self.tipo_instancia = tipo_instancia
        self.region = region
        self.vpc = vpc
        self.ami = ami

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo_maquina,
            "tipo_instancia": self.tipo_instancia,
            "region": self.region,
            "vpc": self.vpc,
            "ami": self.ami,
        }
