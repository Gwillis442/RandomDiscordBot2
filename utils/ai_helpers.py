from openai import OpenAI


class AIHelper:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY or gptApiKey in your .env file.")
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, prompt, model="gpt-4o-mini", max_tokens=150):
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful discord bot. Answer the user's question concisely."},
                {"role": "user", "content": prompt}
                ],
            max_tokens=max_tokens
        )

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("OpenAI returned an empty response.")

        return content.strip()