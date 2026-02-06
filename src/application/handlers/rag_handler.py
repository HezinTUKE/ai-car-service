from application.dataclasses.offer_cars_relation_dc import EventData
from application.utils.rag_utils import RagUtils


class RagHandler:
    @classmethod
    async def rag_query(cls, question: str):
        return await RagUtils.rag_query(question)

    @classmethod
    async def process_service_rag_event(cls, event_data: dict):
        event_data = EventData.from_dict(event_data)

        for service in event_data.services:
            await RagUtils.update_or_create_rag_idx(service)
