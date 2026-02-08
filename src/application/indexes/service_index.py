from application.enums.indexes import OpensearchIndexes
from application.indexes.base_index import BaseIndex


class ServiceIndex(BaseIndex):
    index = OpensearchIndexes.SERVICE_INDEX.value

    __mapping__ = {
        "settings": {"index": {"knn": True}},
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "embedding_text": {"type": "text", "index": False},
                "embedding": {
                    "type": "knn_vector",
                    "dimension": 768,
                    "method": {"name": "hnsw", "space_type": "cosinesimil", "engine": "nmslib"},
                },
                "point": {"type": "geo_point"},
                "country": {"type": "keyword"},
                "city": {"type": "keyword"},
                "original_full_address": {"type": "keyword"},
            }
        },
    }
