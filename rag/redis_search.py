import redis
import numpy as np
from redis.commands.search.query import Query

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

r = redis.Redis(host="localhost", port=6379, decode_responses=False)

INDEX_NAME = "idx:sherlock"
VECTOR_DIM = 384

def get_embedding(chunk):
    embedding = model.encode(chunk).astype(np.float32).tobytes()
    return embedding

def redis_search(query_text):

    query_vector = get_embedding(query_text)

    query = (
        Query("*=>[KNN 5 @embedding $vec AS score]")
        .sort_by("score")
        .return_fields("text", "score")
        .dialect(2)
    )

    results = r.ft(INDEX_NAME).search(
        query,
        query_params={"vec": query_vector},
    )

    for doc in results.docs:
        print("\n--- RISULTATO ---")
        print("Score:", doc.score)
        print(doc.text.replace("\n"," "))

    return results

