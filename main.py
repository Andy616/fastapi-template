from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.routes import root_router
from core.exception_handlers import http_exception_handler, validation_exception_handler
from starlette.middleware.cors import CORSMiddleware

from logging.config import dictConfig
from core.logger import LogConfig
from core.config import settings


dictConfig(LogConfig().dict())


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    exception_handlers={
        StarletteHTTPException: http_exception_handler,
        RequestValidationError: validation_exception_handler
    },
    swagger_ui_parameters={"displayRequestDuration": True}
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Routers
app.include_router(root_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True, debug=True)
