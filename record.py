from dotenv import load_dotenv
import sounddevice as sd
import scipy.io.wavfile
import os


def record_audio(duration_seconds=60, sample_rate=48000):
    load_dotenv()
    recording = sd.rec(
        device=int(os.getenv("DEVICE_INDEX")),
        samplerate=sample_rate,
        channels=2,
        dtype="float32",
        frames=int(duration_seconds * sample_rate),
    )
    sd.wait()
    scipy.io.wavfile.write("output.wav", sample_rate, recording)


if __name__ == "__main__":
    print(sd.query_devices())
