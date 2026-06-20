import os
import json
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

DATA_FOLDER = "Saved_Articles"

chunks = []

# 1. Load all JSON articles
for root, dirs, files in os.walk(DATA_FOLDER):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

                title = data["title"]
                paragraphs = data["paragraphs"]

                # 2. combine paragraphs into chunks
                full_text = title + "\n" + "\n".join(paragraphs)

                # simple chunking (you can improve later)
                words = full_text.split()
                chunk_size = 120

                for i in range(0, len(words), chunk_size):
                    chunk = " ".join(words[i:i + chunk_size])
                    chunks.append(chunk)

print(f"Total chunks: {len(chunks)}")

# 3. Create embeddings
embeddings = model.encode(chunks)

# convert to numpy
embeddings = np.array(embeddings).astype("float32")

# 4. Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# 5. Save FAISS index
with open("faiss_index.pkl", "wb") as f:
    pickle.dump(index, f)

# 6. Save chunks
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("FAISS + chunks saved successfully!")