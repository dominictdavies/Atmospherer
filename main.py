from record import record_audio
from transcribe import get_audio_transcription
from summarise import summarise_text
from generate import generate_image
from wallpaper import set_wallpaper
import time


def print_gap(text: str):
    print(f"\n{text}\n")


if __name__ == "__main__":
    try:
        while True:
            print("Waiting...")
            time.sleep(40)

            print("Recording audio...")
            record_audio(duration_seconds=20)

            print("Getting audio transcription...")
            transcription = get_audio_transcription()
            print_gap(transcription)

            print("Summarising...")
            summary = summarise_text(transcription)
            print_gap(summary)

            print("Generating wallpaper...")
            wallpaper_destination = generate_image(summary)
            print_gap(f"Saved at: {wallpaper_destination}")

            print("Setting wallpaper...")
            set_wallpaper(wallpaper_destination)
            print_gap("Enjoy!")
    except KeyboardInterrupt:
        print("Exiting...")
