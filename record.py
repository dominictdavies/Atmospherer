import sounddevice as sd
import scipy.io.wavfile


def record_audio(device_index, duration_seconds=60, sample_rate=48000):
    recording = sd.rec(
        int(sample_rate * duration_seconds),
        device=device_index,
        samplerate=sample_rate,
        channels=2,
        dtype="int16",
    )
    sd.wait()
    scipy.io.wavfile.write("output.wav", sample_rate, recording)


if __name__ == "__main__":
    print(sd.query_devices())
