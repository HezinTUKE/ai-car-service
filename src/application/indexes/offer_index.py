from application.enums.indexes import OpensearchIndexes
from application.indexes.base_index import BaseIndex


class OfferIndex(BaseIndex):
    index = OpensearchIndexes.OFFER_INDEX.value

    __mapping__ = {
        "settings": {"index": {"knn": True}},
        "mappings": {
            "properties": {
                "service_id": {"type": "keyword"},
                "offer_type": {"type": "keyword"},
                "price": {"type": "float"},
                "currency": {"type": "keyword"},
                "car_brands": {"type": "keyword"},
                "car_types": {"type": "keyword"},
                "embedding_text": {"type": "text", "index": False},
                "embedding": {
                    "type": "knn_vector",
                    "dimension": 768,
                    "method": {"name": "hnsw", "space_type": "cosinesimil", "engine": "nmslib"},
                },
            }
        },
    }
