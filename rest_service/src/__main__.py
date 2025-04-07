from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from src.api import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


def create_app() -> FastAPI:
    fastapi = FastAPI(docs_url='/swagger', lifespan=lifespan)
    fastapi.include_router(router)
    return fastapi


if __name__ == '__main__':
    uvicorn.run(
        'src.__main__:create_app',
        factory=True,
        host='0.0.0.0',
        port=6080,
        workers=1,
        # access_log=False,
    )
