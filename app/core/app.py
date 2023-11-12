from fastapi import FastAPI, Response, Request
import logging
import random
import string
import time

from app.api.v1.routes.api import router as api_router
from app.core.config import get_config

logger = logging.getLogger(__name__)


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

    async def set_body(request: Request, body: bytes) -> None:
        async def receive():
            return {'type': 'http.request', 'body': body}

        request._receive = receive

    @application.middleware("http")
    async def log_requests(request: Request, call_next):
        idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        body = await request.body()
        await set_body(request, body)
        body_str = body.decode().replace('\n', ' ')
        logger.info(f"rid={idem} start request path={request.url.path}, path_params={request.path_params}, query_params={request.query_params}, body_params={body_str}")
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)
        logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

        return response

    application.include_router(api_router, prefix=prefix)

    return application
