from dotenv import load_dotenv
from openai import OpenAI
import os


def get_audio_transcription():
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    audio_file = open("output.wav", "rb")

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe", file=audio_file
    )

    return transcription.text


if __name__ == "__main__":
    print(get_audio_transcription())
