from dataclasses_json import dataclass_json, Undefined, DataClassJsonMixin
from dataclasses import dataclass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class OfferIndexDC(DataClassJsonMixin):
    service_id: str
    offer_type: str
    price: float
    currency: str
    car_brands: list[str]
    car_types: list[str]
    embedding_text: str = ""

    def format_embedding_text(self, service_name: str, city: str, country: str, offer_description: str, human_readable_offer_type: str = ""):
        self.embedding_text = (f"{service_name} offers a {human_readable_offer_type} service in {city.title()}, {country.title()}."
                               f"The service includes {offer_description} The price of service is {self.price} {self.currency}."
                               f"This offer is suitable for {', '.join(self.car_brands)}, including {', '.join(self.car_types)}.")
