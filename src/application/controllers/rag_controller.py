from fastapi import APIRouter
from application.controllers import RAG_CONTROLLER_PREFIX
from application.handlers.rag_handler import RagHandler
from application.schemas.response_schemas.rag_schema import RagResponseSchema


class RagController:
    router = APIRouter(tags=["RAG_CONTROLLER_PREFIX"], prefix=f"/{RAG_CONTROLLER_PREFIX}")

    @staticmethod
    @router.get("/answer", response_model=RagResponseSchema)
    async def retrieve_rag_answer(
        question: str,
        user_latitude: float = None,
        user_longitude: float = None,
    ):
        return await RagHandler.rag_query(question, user_latitude, user_longitude)
