from fastapi import Path, Body
from api.config import Responses
from core.router import get_router
from core.exceptions import FatalError
from schemas.user import User

router = get_router()


@router.get("/{id}", responses=Responses, response_model=User, description="Get User By ID")
async def invoice_users(
        id: int = Path(title="User ID"),
):
    return User(id=id)


@router.post("/", responses=Responses, response_model=User, description="Create User")
async def invoice_users(
        user: User = Body(),
):
    if user.id == 1:
        raise FatalError(status_code=400, detail="test error")
    return user
