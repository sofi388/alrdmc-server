import flask
from flask_openapi3 import OpenAPI

from config import PORT
from openapi_config import semantic_vector_tag, semantic_vector_summary, \
                            info, SemanticVectorObject

app = OpenAPI(__name__, info=info)

@app.get("/semantic_vectors", summary=semantic_vector_summary, tags=[semantic_vector_tag])
def get_semantic_vectors():
    """
    A GET endpoint to fetch all semantic vectors
    from the database
    """

    ### DB query logic here
    semantic_vector_objects = [SemanticVectorObject(
        semantic_vector=[i/768 for i in range(768)],
        semantic_vector_url="https://social.mtdv.me/articles/initiative"
    )
    ]
    ### make semantic_vector_list contain all semantic vectors

    return flask.jsonify([ semantic_vector_object.__dict__ for semantic_vector_object in semantic_vector_objects])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)