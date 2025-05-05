from dotenv import load_dotenv
from openai import OpenAI
import os


def summarise_text(text):
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"Based on the following transcription, respond with an image generation prompt of no more than 1 sentence, that could be used to create an accurate representation of the scene described.\n\n{text}"
    response = client.responses.create(model="gpt-4.1", input=prompt)

    return response.output_text


if __name__ == "__main__":
    print(summarise_text("The quick brown fox jumps over the lazy dog."))
