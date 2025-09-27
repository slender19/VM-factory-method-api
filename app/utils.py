import uuid

SENSITIVE_KEYS = ["password", "token", "secret", "key"]

def generate_vm_id(provider: str) -> str:
    return f"{provider}-{uuid.uuid4()}"

def mask_sensitive(data: dict) -> dict:
    masked = {}
    for k, v in data.items():
        if any(sk in k.lower() for sk in SENSITIVE_KEYS):
            masked[k] = "***"
        else:
            masked[k] = v
    return masked
