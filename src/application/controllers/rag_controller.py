from fastapi import APIRouter
from application.controllers import RAG_CONTROLLER_PREFIX


class RagController:
    router = APIRouter(tags=["RAG_CONTROLLER_PREFIX"], prefix=f"/{RAG_CONTROLLER_PREFIX}")

    @staticmethod
    @router.get("/answer", description="Retrieve RAG answer based on query")
    def retrieve_rag_answer():
        pass
