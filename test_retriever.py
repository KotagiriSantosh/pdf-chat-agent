from pdf_utils import extract_text, chunk_text
from retriever import Retriever

# 1. Load and chunk your PDF text
text = extract_text("sample.pdf")
chunks = chunk_text(text, chunk_size=1000)

# 2. Initialize the Retriever
retriever = Retriever(chunks)

# 3. Ask a test question
question = "What are the current use cases?"
top_chunks = retriever.get_top_chunks(question, k=5)

# 4. Print the top 2 matching chunks
print("Top 2 relevant chunks for query:", question, "\n")
for idx, chunk in enumerate(top_chunks, 1):
    print(f"--- Chunk {idx} ---")
    print(chunk)
    print()
