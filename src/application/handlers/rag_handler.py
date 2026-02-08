from application.dataclasses.offer_cars_relation_dc import EventData
from application.handlers.offer_handler import OfferHandler
from application.handlers.service_handler import ServiceHandler
from application.utils.rag_utils import RagUtils


class RagHandler:
    @classmethod
    async def rag_query(cls, question: str):
        return await RagUtils.rag_query(question)

    @classmethod
    async def process_service_rag_event(cls, event_data: dict):
        event_data = EventData.from_dict(event_data)
        service_handler = ServiceHandler()

        for service in event_data.services:
            await service_handler.create_document(service)
            offer_handler = OfferHandler(service.service_id, service.service_id)
            for offer in service.offers:
                await offer_handler.create_document(offer)
