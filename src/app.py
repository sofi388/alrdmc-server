import flask
import threading
from flask_openapi3 import OpenAPI
import logging

from config.config import PORT
from config.openapi_config import semantic_vector_tag, semantic_vector_summary, \
                            info, SemanticVectorObject
from semanticize import generate_semantic_vector
from db_logic.poller import poller

logger = logging.getLogger("flask.app")

poller = threading.Thread(target=poller, args=(logger,))
poller.start()

app = OpenAPI(__name__, info=info)
@app.get("/semantic_vectors", summary=semantic_vector_summary, tags=[semantic_vector_tag])
def get_semantic_vectors():
    """
    A GET endpoint to fetch all semantic vectors
    from the database
    """
    logger.info(f"fetching semantic vectors from DB")
    ### DB query logic here
    
    semantic_vector_objects = [SemanticVectorObject(
        semantic_vector=generate_semantic_vector("lol"),
        semantic_vector_url="https://social.mtdv.me/articles/initiative"
    )
    ]
    ### make semantic_vector_list contain all semantic vectors
    logger.info(f"got {len(semantic_vector_objects)} semantic vectors from DB")

    return flask.jsonify([ semantic_vector_object.__dict__ for semantic_vector_object in semantic_vector_objects])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)