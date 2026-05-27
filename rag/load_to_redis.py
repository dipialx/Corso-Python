import os
import redis
import numpy as np


from redis.commands.search.field import TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

r = redis.Redis(host="localhost", port=6379, decode_responses=False)

INDEX_NAME = "idx:sherlock"
PREFIX = "sherlock:chunk:"
VECTOR_DIM = 384

def get_embedding(chunk):
    embedding = model.encode(chunk).astype(np.float32).tobytes()
    return embedding


def chunk_text(text, chunk_size=1000, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap
    return chunks


with open("SherlockHolmes.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = chunk_text(text)

print(f"Chunk creati: {len(chunks)}")

try:
    r.ft(INDEX_NAME).dropindex(delete_documents=True)
except Exception:
    pass

schema = (
    TextField("text"),
    VectorField(
        "embedding",
        "HNSW",
        {
            "TYPE": "FLOAT32",
            "DIM": VECTOR_DIM,
            "DISTANCE_METRIC": "COSINE",
        },
    ),
)

r.ft(INDEX_NAME).create_index(
    fields=schema,
    definition=IndexDefinition(
        prefix=[PREFIX],
        index_type=IndexType.HASH,
    ),
)

for i, chunk in enumerate(chunks):
    embedding = get_embedding(chunk)

    r.hset(
        f"{PREFIX}{i}",
        mapping={
            "text": chunk,
            "embedding": embedding,
        },
    )

    print(f"Salvato chunk {i + 1}/{len(chunks)}")

print("Caricamento completato.")