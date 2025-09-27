from abc import ABC, abstractmethod
from typing import Dict

# Clase base Producto
class VM(ABC):
    def __init__(self, tipo_maquina: str):
        self.tipo_maquina = tipo_maquina

    @abstractmethod
    def get_info(self) -> Dict:
        pass


# Productos concretos
class VMAzure(VM):
    def __init__(self, tamaño_maquina: str, resource_group: str, imagen: str, red_virtual: str):
        super().__init__("Azure VM")
        self.tamaño_maquina = tamaño_maquina
        self.resource_group = resource_group
        self.imagen = imagen
        self.red_virtual = red_virtual

    def get_info(self) -> Dict:
        return {
            "tipo": self.tipo_maquina,
            "tamaño_maquina": self.tamaño_maquina,
            "resource_group": self.resource_group,
            "imagen": self.imagen,
            "red_virtual": self.red_virtual,
        }


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
