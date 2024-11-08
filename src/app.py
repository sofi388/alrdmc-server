import flask
from flask_openapi3 import OpenAPI

from config import PORT
from openapi_config import semantic_vector_tag, semantic_vector_summary, \
                            info

app = OpenAPI(__name__, info=info)

@app.get("/semantic_vectors", summary=semantic_vector_summary, tags=[semantic_vector_tag])
def get_semantic_vectors():
    """
    A GET endpoint to fetch all semantic vectors
    from the database
    """

    ### DB query logic here
    semantic_vector_list = [
        [0.0,0.1,0.2,0.4,1.1],
        [0.0,0.1,0.2,0.4,1.1]
    ]
    ### make semantic_vector_list contain all semantic vectors

    return flask.jsonify(semantic_vector_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)