from application.dataclasses.question_metadata_dc import QuestionMetadataDc
from application.dataclasses.rag_os_filter import *
from application.dataclasses.user_point import UserPoint
from application.enums.metadata import FuncMetadata
from application.indexes.rag_index import RagIndex
from application.schemas.service_schemas.response_schemas.rag_schema import RagResponseItemSchema, RagResponseSchema
from application.utils.ai_heplers import question_encoding, embedding


class RagUtils:
    @classmethod
    async def rag_query(cls, question: str):
        result = RagResponseSchema(data=[])

        question_metadata = question_encoding(question)
        question_metadata = QuestionMetadataDc.from_dict(question_metadata)

        generated_query = cls.generate_os_query(question, question_metadata)

        res = await RagIndex.retrieve_by_query(query=generated_query)

        for doc in res:
            score = doc["_score"]
            if score and score < 0.70:
                continue

            result.data.append(
                RagResponseItemSchema(service_id=doc["_id"], content=doc["_source"]["content"], score=score or 100)
            )

        if not result.data:
            result.data.append(RagResponseItemSchema(service_id=None, content="No relevant service found.", score=0.0))

        return result.model_dump()

    @classmethod
    def generate_os_query(
        cls, question: str, question_metadata: QuestionMetadataDc, user_point: UserPoint = None
    ) -> dict:
        query_vector = embedding(question)

        query_body = RagOsFilterRequestBody()
        query_body.query.bool.must.append(
            RagMustOsFilter(
                knn=RagKNNFilter(
                    embedding=RagEmbeddingFilter(
                        vector=query_vector,
                        k=30,
                    )
                )
            )
        )

        if (question_metadata.max_distance or question_metadata.func == FuncMetadata.MAX_DISTANCE) and user_point:
            query_body.query.bool.filter.geo_distance = RagGeoDistanceAttrsFilter(
                distance=f"{question_metadata.max_distance}km",
                point={"lat": user_point.latitude, "lon": user_point.longitude},
            )

        if question_metadata.country:
            query_body.query.bool.filter.append(RagBoolOsAttrsFilter(term={"country": question_metadata.country.name}))

        if question_metadata.city:
            query_body.query.bool.filter.append(RagBoolOsAttrsFilter(term={"city": question_metadata.city}))

        if question_metadata.offer_type:
            query_body.query.bool.nested = RagNestedTermFilter(
                term={"offers.offer_type": question_metadata.offer_type.name}
            )

        if question_metadata.max_price:
            query_body.query.bool.nested = RagNestedTermFilter(
                term={"offers.base_price": {"lte": question_metadata.max_price}}
            )

        if question_metadata.func == FuncMetadata.CHEAPEST:
            query_body.sort.append(
                {
                    "offers.base_price": {
                        "order": "asc",
                        "mode": "min",
                        "nested": {
                            "path": "offers",
                            "filter": {"term": {"offers.offer_type": question_metadata.offer_type.name}},
                        },
                    }
                }
            )

        if question_metadata.func == FuncMetadata.MAX_DISTANCE and user_point:
            query_body.sort.append(
                {
                    "_geo_distance": {
                        "point": {"lat": user_point.latitude, "lon": user_point.longitude},
                        "order": "asc",
                        "unit": "km",
                        "mode": "min",
                        "distance_type": "arc",
                    }
                }
            )

        return cls.dict_cleaner(query_body.to_dict())

    @classmethod
    def dict_cleaner(cls, obj: dict | list) -> dict | list:
        empty_values = (None, {}, [], "")

        if isinstance(obj, dict):
            return {k: cls.dict_cleaner(v) for k, v in obj.items() if cls.dict_cleaner(v) not in empty_values}
        if isinstance(obj, list):
            return [cls.dict_cleaner(v) for v in obj if cls.dict_cleaner(v) not in empty_values]

        return obj
