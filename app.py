from pdf_utils import extract_text, chunk_text
from retriever import Retriever
from qa_pipeline import answer_question

def main():
    pdf = input("Enter PDF filename (e.g. sample.pdf): ").strip()
    print("🔄 Parsing…")
    text = extract_text(pdf)
    print("🔄 Chunking…")
    chunks = chunk_text(text, chunk_size=1000)

    retriever = Retriever(chunks)
    print("\n✅ Agent ready—type your question or 'exit':\n")

    while True:
        q = input("Q: ").strip()
        if q.lower() in ("exit", "quit"):
            print("👋 Goodbye!")
            break

        top = retriever.get_top_chunks(q, k=5)
        ans = answer_question(q, top)
        print("\nA:")
        print(ans)
        print("-" * 40, "\n")

if __name__ == "__main__":
    main()
