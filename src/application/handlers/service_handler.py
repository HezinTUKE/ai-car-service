import logging

from application.dataclasses.offer_cars_relation_dc import ServiceDC
from application.dataclasses.service_index_dc import ServiceIndexDC
from application.handlers.index_abstraction import IndexAbstraction
from application.indexes.service_index import ServiceIndex
from application.utils.ai_heplers import translate


class ServiceHandler(IndexAbstraction):
    logger = logging.getLogger(" ")

    async def create_document(self, dc: ServiceDC):
        index_dc = ServiceIndexDC(
            name=dc.name,
            description=dc.description,
            point={"lat": dc.latitude, "lon": dc.longitude},
            country=dc.country,
            city=dc.city,
            original_full_address=dc.original_full_address,
        )

        translated_text = translate(dc.description) if dc.description else ""
        index_dc.format_embedding_text(translated_text)

        try:
            await ServiceIndex.create_or_update_document(dc.service_id, index_dc.to_dict())
        except Exception:
            self.logger.exception("Failed to create document for service index", exc_info=True)
            return False
