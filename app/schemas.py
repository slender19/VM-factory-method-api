from pydantic import BaseModel
from typing import Dict, Optional

class ProvisionRequest(BaseModel):
    provider: str
    parametros: Dict

class ProvisionResponse(BaseModel):
    provider: str
    status: str   # "success" o "error"
    vm_id: Optional[str] = None
    vm: Optional[Dict] = None
    error: Optional[str] = None
