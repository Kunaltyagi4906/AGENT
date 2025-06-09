import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="test.wav", duration=5, fs=44100):
    sd.default.device = 2  # ⬅️ change this to the correct mic index from above
    print(f"🎙️ Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Saved to {filename}")
