
# Load model directly
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
model = AutoModel.from_pretrained(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

def generate_semantic_vector(text: str):
    """
    To use this function, you can just call it with any text and it will return the semantic vector for that text
    """
    inputs = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )
    outputs = model(**inputs)
    return outputs.pooler_output