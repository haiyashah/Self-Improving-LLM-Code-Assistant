import faiss
import numpy as np
import pickle
import os

class ReasoningMemory:
    def __init__(self, dim=384, index_path="memory.index"):
        self.index_path = index_path
        self.dim = dim
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            with open(index_path + ".meta", "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.metadata = []

    def add(self, embedding: np.ndarray, meta: dict):
        # Normalize for L2 distance
        vector = np.array([embedding], dtype='float32')
        self.index.add(vector)
        self.metadata.append(meta)
        self.save()

    def query(self, embedding: np.ndarray, k=3):
        vector = np.array([embedding], dtype='float32')
        distances, indices = self.index.search(vector, k)
        
        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.metadata):
                results.append(self.metadata[i])
        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".meta", "wb") as f:
            pickle.dump(self.metadata, f)
