from fastapi import FastAPI, HTTPException
from .schemas import ProvisionRequest, ProvisionResponse
from .services import ProvisionService

app = FastAPI(title="VM Factory API")

service = ProvisionService()

@app.post("/provision", response_model=ProvisionResponse)
def provisionar(req: ProvisionRequest):
    resp = service.provisionar(req.provider, req.parametros)
    if resp.status == "error":
        raise HTTPException(status_code=400, detail=resp.error)
    return resp

