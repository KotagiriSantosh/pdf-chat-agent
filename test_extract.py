from pdf_utils import extract_text

# Adjust filename if needed
text = extract_text("sample.pdf")
# Print the first 300 characters to confirm it works
print(text[:300])
