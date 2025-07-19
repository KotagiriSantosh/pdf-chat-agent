from pdf_utils import extract_text, chunk_text

# 1. Extract full text
text = extract_text("sample.pdf")

# 2. Chunk it
chunks = chunk_text(text, chunk_size=1000)

# 3. Output number of chunks & first chunk preview
print(f"Total chunks: {len(chunks)}\n")
print("First chunk preview:\n")
print(chunks[0])
