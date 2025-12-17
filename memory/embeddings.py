from sentence_transformers import SentenceTransformer
import numpy as np
import torch

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initializes the transformer model. 
        'all-MiniLM-L6-v2' is chosen for its balance of speed and 384-dim accuracy.
        """
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = SentenceTransformer(model_name, device=self.device)

    def embed_text(self, text: str) -> np.ndarray:
        """
        Converts a string (e.g., a failed PR step) into a normalized embedding.
        """
        if not text.strip():
            return np.zeros(self.model.get_sentence_embedding_dimension())
            
        embedding = self.model.encode(text, convert_to_numpy=True)
        # Normalize to unit length for better L2/Cosine similarity search
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
        return embedding

    def embed_batch(self, texts: list) -> np.ndarray:
        """Batch processing for faster initial indexing."""
        return self.model.encode(texts, convert_to_numpy=True)
