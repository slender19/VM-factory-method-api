from .factory import ProveedorFactory
from .schemas import ProvisionResponse
from .utils import generate_vm_id, mask_sensitive
from loguru import logger

class ProvisionService:
    def provisionar(self, provider: str, parametros: dict) -> ProvisionResponse:
        try:
            proveedor = ProveedorFactory.get_proveedor(provider)
        except ValueError as e:
            return ProvisionResponse(provider=provider, status="error", error=str(e))

        try:
            vm = proveedor.crear_vm(parametros)
            vm_id = generate_vm_id(provider)

            
            safe_params = mask_sensitive(parametros)
            logger.info(f"Provision request: provider={provider}, vm_id={vm_id}, params={safe_params}")

            return ProvisionResponse(
                provider=provider,
                status="success",
                vm_id=vm_id,
                vm=vm.get_info()
            )
        except Exception as e:
            logger.error(f"Provision failed for provider={provider}: {e}")
            return ProvisionResponse(provider=provider, status="error", error=str(e))
