from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, chunks: list[str]):
        """
        chunks: list of text pieces (strings)
        """
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer().fit(chunks)
        self.matrix = self.vectorizer.transform(chunks)

    def get_top_chunks(self, query: str, k: int = 5) -> list[str]:
        """
        Returns the top k chunks most similar to the query.
        """
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix)[0]
        top_idxs = sims.argsort()[-k:][::-1]
        return [self.chunks[i] for i in top_idxs]
