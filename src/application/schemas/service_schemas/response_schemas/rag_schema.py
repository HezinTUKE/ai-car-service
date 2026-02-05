from uuid import UUID

from pydantic import BaseModel


class RagResponseItemSchema(BaseModel):
    service_id: UUID | None
    content: str
    score: float


class RagResponseSchema(BaseModel):
    data: list[RagResponseItemSchema]
