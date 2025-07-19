import re
from transformers import pipeline

# Initialize the QA model (runs on CPU)
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def extract_section(context: str, header: str) -> str:
    """
    Grab text under `header:` up to the next numbered header or end of doc.
    """
    pattern = rf"{re.escape(header)}:(.*?)(?=\n\d+\.|\Z)"
    m = re.search(pattern, context, flags=re.DOTALL|re.IGNORECASE)
    return m.group(1).strip() if m else ""

def get_bullets(block: str) -> list[str]:
    """
    From a text block, return lines that start with '-' or '1.', '2.', etc.
    """
    bullets = re.findall(r'^\s*-\s*(.+)$', block, flags=re.MULTILINE)
    bullets += re.findall(r'^\s*\d+\.\s*(.+)$', block, flags=re.MULTILINE)
    return bullets

def answer_question(question: str, context_chunks: list[str]) -> str:
    """
    1. Section‑based extraction for list‑style questions
    2. Regex fallbacks for email/phone/score
    3. LLM QA fallback
    """
    context = "\n".join(context_chunks)
    q = question.lower()

    # Map keywords to section headers
    if "current use case" in q:
        sec = extract_section(context, "3. Current Use Cases")
        items = get_bullets(sec)
        if items:
            return "\n".join(f"- {it}" for it in items)

    if "industry application" in q:
        sec = extract_section(context, "4. Industry Applications")
        items = get_bullets(sec)
        if items:
            return "\n".join(f"- {it}" for it in items)

    if "evolution" in q:
        sec = extract_section(context, "2. Evolution")
        items = get_bullets(sec)
        if items:
            return "\n".join(f"- {it}" for it in items)

    if "reference" in q or "paper" in q:
        sec = extract_section(context, "References")
        items = get_bullets(sec)
        if items:
            return "\n".join(f"{i+1}. {it}" for i, it in enumerate(items))

    if "challenge" in q:
        sec = extract_section(context, "5. Challenges & Future Outlook")
        items = get_bullets(sec)
        if items:
            return "\n".join(f"- {it}" for it in items)

    # Regex fallbacks
    if "email" in q:
        m = re.findall(r'[\w\.-]+@[\w\.-]+', context)
        if m: return m[0]

    if any(k in q for k in ("phone", "mobile")):
        m = re.findall(r'\+?\d[\d\s\-\(\)]{7,}\d', context)
        if m: return m[0]

    if "score" in q:
        m = re.findall(r'\d+\.\d+', context)
        if m: return m[0]

    # LLM fallback
    res = qa(question=question, context=context)
    return res["answer"]
