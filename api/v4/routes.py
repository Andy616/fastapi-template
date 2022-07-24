from core.router import get_router
from .endpoints import user

api_router = get_router()

api_router.include_router(user.router, prefix="/user", tags=["User"])
