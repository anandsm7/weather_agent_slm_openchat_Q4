from llama_cpp import Llama
import config as cfg

llm = Llama(
    model_path=cfg.MODEL_PATH,
    n_threads=2,
    n_ctx=2048,
    n_batch=256,
    use_mlock=True,
    use_mmap=True
)

def call_model(prompt: str, max_tokens: int = 200):
    return llm(prompt, max_tokens=max_tokens, stop=["\n\n", "Query::"])["choices"][0]["text"]