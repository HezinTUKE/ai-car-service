from dataclasses_json import dataclass_json, Undefined, DataClassJsonMixin
from dataclasses import dataclass

from application.enums.country import Country


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ServiceIndexDC(DataClassJsonMixin):
    name: str
    description: str
    point: dict
    country: Country
    city: str
    original_full_address: str
    embedding_text: str = ""

    def format_embedding_text(self, translated_description: str = ""):
        self.embedding_text = (
            f"{self.name} is a car service located in {self.city}, {self.country.value}. "
            f"The service address is {self.original_full_address} Description: {translated_description}"
        )
