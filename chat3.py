import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


content="come preparare le lasagne"
embedding = model.encode(content).astype(np.float32).tobytes()


print(len(embedding))
print(embedding)
