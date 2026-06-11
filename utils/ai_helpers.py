from openai import OpenAI


class AIHelper:
    def __init__(self, provider="openai", api_key=None, base_url=None, model=None):
        self.provider = (provider or "openai").lower()

        if self.provider == "ollama":
            # Ollama exposes an OpenAI-compatible API at /v1 by default.
            resolved_base_url = (base_url or "http://localhost:11434/v1").rstrip("/")
            resolved_api_key = api_key or "ollama"
            self.client = OpenAI(api_key=resolved_api_key, base_url=resolved_base_url)
            self.default_model = model or "llama3.1:8b"
            return

        if not api_key:
            raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY or gptApiKey in your .env file.")

        self.client = OpenAI(api_key=api_key)
        self.default_model = model or "gpt-4o-mini"

    def generate_response(self, prompt, model=None, max_tokens=150):
        model_name = model or self.default_model
        response = self.client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful discord bot. Answer the user's question concisely."},
                {"role": "user", "content": prompt}
                ],
            max_tokens=max_tokens
        )

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError(f"{self.provider} backend returned an empty response.")

        return content.strip()
