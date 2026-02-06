from contextlib import asynccontextmanager
from logging.config import dictConfig

from fastapi import FastAPI

from application import config
from application.controllers.opensearch_controller import OpensearchController
from application.controllers.rag_controller import RagController
from application.events.listener import RabbitProcessorListener


@asynccontextmanager
async def lifespan(_: FastAPI):
    rabbit = await RabbitProcessorListener.connect()
    await rabbit.listen()

    try:
        yield
    finally:
        await rabbit.disconnect()

dictConfig(config.log_config)

app = FastAPI(lifespan=lifespan)

app.include_router(RagController.router)
app.include_router(OpensearchController.router)
