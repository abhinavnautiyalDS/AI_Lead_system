from pydantic import BaseModel

class LeadRequest(BaseModel):
    message: str