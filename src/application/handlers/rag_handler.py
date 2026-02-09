import asyncio

from application.dataclasses.offer_cars_relation_dc import EventData
from application.dataclasses.user_point import UserPoint
from application.handlers.offer_handler import OfferHandler
from application.handlers.service_handler import ServiceHandler
from application.utils.rag_utils import RagUtils


class RagHandler:
    @classmethod
    async def rag_query(cls, question: str, user_latitude: float = None, user_longitude: float = None):
        user_point = (
            UserPoint(latitude=user_latitude, longitude=user_longitude) if user_latitude and user_longitude else None
        )
        return await RagUtils.rag_query(question, user_point)

    @classmethod
    async def process_service_rag_event(cls, event_data: dict):
        event_data = EventData.from_dict(event_data)
        service_handler = ServiceHandler()

        for service in event_data.services:
            await service_handler.create_document(service)
            offer_handler = OfferHandler(service.name, service.service_id, service.city, service.country)
            for offer in service.offers:
                await offer_handler.create_document(offer)

            await asyncio.sleep(0.01)
