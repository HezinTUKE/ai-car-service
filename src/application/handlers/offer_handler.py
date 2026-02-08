import logging

from application.dataclasses.offer_cars_relation_dc import OfferDC
from application.dataclasses.offer_index_dc import OfferIndexDC
from application.handlers.index_abstraction import IndexAbstraction
from application.indexes.offer_index import OfferIndex


class OfferHandler(IndexAbstraction):
    logger = logging.getLogger(" ")

    def __init__(self, service_name: str, service_id: str):
        self.service_name = service_name
        self.service_id = service_id

    async def create_document(self, offer_dc: OfferDC):
        offer_index_dc = OfferIndexDC(
            service_id=self.service_id,
            offer_type=offer_dc.offer_type,
            price= offer_dc.base_price * (1 - offer_dc.sale / 100),
            currency=offer_dc.currency,
            car_brands=[occ.car_brand for occ in offer_dc.offer_car_compatibility],
            car_types=[occ.car_type for occ in offer_dc.offer_car_compatibility],
        )

        offer_index_dc.embedding_text = f""

        try:
            await OfferIndex.create_or_update_document(offer_dc.offer_id, offer_index_dc.to_dict())
        except Exception:
            self.logger.exception("Failed to create document for offer index", exc_info=True)
            return False
