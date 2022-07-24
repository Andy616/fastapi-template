from pydantic import BaseModel
from typing import Optional, Any


class Response(BaseModel):
    success: bool
    message: Optional[Any] = None


class ErrorResponse(Response):
    success = False
