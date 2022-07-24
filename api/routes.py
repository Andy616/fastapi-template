from core.router import get_router
from .health import health_router
from .v4.routes import api_router


root_router = get_router()

root_router.include_router(health_router, tags=["Health"])
root_router.include_router(api_router, prefix="/api/v4")
