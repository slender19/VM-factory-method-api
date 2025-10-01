from .models.providers import (
    AWSProveedor,
    AzureProveedor,
    GoogleCloudProveedor,
    OnPremiseProveedor,
    Proveedor,
)

class ProveedorFactory:
    _registry = {
        "aws": AWSProveedor,
        "azure": AzureProveedor,
        "google_cloud": GoogleCloudProveedor,
        "on_premise": OnPremiseProveedor,
    }

    @classmethod
    def get_proveedor(cls, name: str) -> Proveedor:
        prov_cls = cls._registry.get(name.lower())
        if not prov_cls:
            raise ValueError(f"Proveedor no soportado: {name}")
        return prov_cls()
