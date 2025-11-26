from sentence_transformers import SentenceTransformer
import os
import numpy as np

class EmbeddingModel:
    def __init__(self) -> None:
        """
        Initialize the embedding model using SentenceTransformer.
        
        Args:
            None. Users must set MODEL_NAME in environment variables.
        """
        model_name = os.getenv("MODEL_NAME")
        if not model_name:
            raise ValueError("MODEL_NAME environment variable not set.")
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, desc: str) -> list:
        """
        Generate embedding for the ticket desc.

        Args:
            text (str): The ticket description to embed.
        
        Returns:
            list: The embedding vector as a list.
        """
        return self.model.encode(desc).tolist()
    
    @staticmethod
    def compute_cosine_similarity(a: list, b: list) -> float:
        """
        Compute cosine similarity between two embedding vectors.

        Args:
            a (list): First embedding vector.
            b (list): Second embedding vector.

        Returns:
            float: Cosine similarity score.
        """
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
