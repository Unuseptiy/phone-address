import uvicorn

from app.core.app import get_app
from app.core.config import get_config


app = get_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=get_config().host,
        port=get_config().port,
        reload=True
    )

