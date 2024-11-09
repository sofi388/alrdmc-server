# Load model directly
from transformers import AutoTokenizer, AutoModel, pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
model = AutoModel.from_pretrained(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
pipeline_generation_keywords = pipeline("text-generation", model='meta-llama/Llama-3.2-1B-Instruct', torch_dtype=torch.bfloat16)


def generate_semantic_vector(text: str):
    """
    To use this function, you can just call it with any text and it will return the semantic vector for that text
    """
    # First, generate the keywords of the text
    pipeline_generation_keywords("From the following text, extract a list of specific keywords related to the topic: " + text)

    inputs = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )
    outputs = model(**inputs)
    last_layer_states = outputs[0]
    # Sum and divide by the number of tokens
    pooled_output = last_layer_states.sum(axis=1).mul(1.0 / last_layer_states.shape[1])
    return pooled_output.squeeze().tolist()
