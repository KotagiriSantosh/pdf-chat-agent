from pdf_utils import extract_text, chunk_text
from retriever import Retriever
from qa_pipeline import answer_question

# 1. Extract & chunk the PDF text
text = extract_text("sample.pdf")
chunks = chunk_text(text, chunk_size=1000)

# 2. Retrieve top 2 chunks for our question
retriever = Retriever(chunks)
question = "What are the current use cases?"
top_chunks = retriever.get_top_chunks(question, k=5)

# 3. Get the answer from the QA pipeline
answer = answer_question(question, top_chunks)

print("Question:", question)
print("Answer:", answer)
