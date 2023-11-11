from fastapi import FastAPI


from app.api.v1.routes.api import router as api_router
from app.core.config import get_config


def get_app() -> FastAPI:
    config = get_config()

    project_name = config.project_name
    debug = config.debug
    version = config.version
    prefix = config.api_prefix
    docs_url = config.docs_url
    openapi_url = config.openapi_url

    application = FastAPI(
        title=project_name,
        debug=debug,
        version=version,
        docs_url=docs_url,
        openapi_url=openapi_url,
    )

    application.include_router(api_router, prefix=prefix)

    return application
