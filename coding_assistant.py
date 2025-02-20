import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_coding_help(question):
    prompt = f"Provide a detailed answer with code examples for the following programming question:\n{question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    question = input("Enter your programming question: ")
    answer = get_coding_help(question)
    print("\nCoding Assistant Answer:\n", answer)
