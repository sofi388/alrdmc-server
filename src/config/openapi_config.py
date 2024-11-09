from pydantic import BaseModel
from flask_openapi3 import Info, Tag

info = Info(title="alrdmc API", version="0.1.0")

semantic_vector_tag = Tag(name="semantic_vectors", description="object containing all semantic vectors")
semantic_vector_summary = "get all semantic vectors in DB"

class SemanticVectorObject(BaseModel):
    semantic_vector: list[float]
    semantic_vector_url: str