import logging

from application.dataclasses.offer_cars_relation_dc import OfferDC
from application.dataclasses.offer_index_dc import OfferIndexDC
from application.enums import country
from application.handlers.index_abstraction import IndexAbstraction
from application.indexes.offer_index import OfferIndex
from application.utils.ai_heplers import translate


class OfferHandler(IndexAbstraction):
    logger = logging.getLogger(" ")

    def __init__(self, service_name: str, service_id: str, city: str, country: country.Country):
        self.service_name = service_name
        self.service_id = service_id
        self.city = city
        self.country = country

    async def create_document(self, offer_dc: OfferDC):
        offer_index_dc = OfferIndexDC(
            service_id=self.service_id,
            offer_type=offer_dc.offer_type,
            price=offer_dc.base_price * (1 - offer_dc.sale / 100),
            currency=offer_dc.currency.value,
            car_brands=[occ.car_brand for occ in offer_dc.offer_car_compatibility],
            car_types=[occ.car_type for occ in offer_dc.offer_car_compatibility],
        )
        translated_text = translate(offer_dc.description) if offer_dc.description else ""
        offer_index_dc.format_embedding_text(
            service_name=self.service_name,
            city=self.city,
            country=self.country.value,
            offer_description=translated_text,
        )

        try:
            await OfferIndex.create_or_update_document(offer_dc.offer_id, offer_index_dc.to_dict())
        except Exception:
            self.logger.exception("Failed to create document for offer index", exc_info=True)
            return False
