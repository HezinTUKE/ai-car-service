from abc import ABC, abstractmethod

from dataclasses_json import DataClassJsonMixin


class IndexAbstraction(ABC):
    @abstractmethod
    async def create_document(self, dc: DataClassJsonMixin) -> bool:
        pass
