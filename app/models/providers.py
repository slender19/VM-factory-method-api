from abc import ABC, abstractmethod
from typing import Dict
from .vm import VMAzure, VMAWS, VMGoogleCloud, VMOnPremise, VM

# Clase abstracta Creator
class Proveedor(ABC):
    @abstractmethod
    def crear_vm(self, parametros: Dict) -> VM:
        pass


# Creadores concretos
class AWSProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMAWS(
            tipo_instancia=parametros["tipo_instancia"],
            region=parametros["region"],
            vpc=parametros["vpc"],
            ami=parametros["ami"],
        )


class AzureProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMAzure(
            tamaño_maquina=parametros["tamaño_maquina"],
            resource_group=parametros["resource_group"],
            imagen=parametros["imagen"],
            red_virtual=parametros["red_virtual"],
        )


class GoogleCloudProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMGoogleCloud(
            machine_type=parametros["machine_type"],
            zona=parametros["zona"],
            disco_base=parametros["disco_base"],
            proyecto=parametros["proyecto"],
        )


class OnPremiseProveedor(Proveedor):
    def crear_vm(self, parametros: Dict) -> VM:
        return VMOnPremise(
            cpu=parametros["cpu"],
            ram=parametros["ram"],
            disco=parametros["disco"],
            red_fisica=parametros["red_fisica"],
        )
