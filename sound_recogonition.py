import sounddevice as sd
from scipy.io.wavfile import write
import os

# Parameters
fs = 16000  # Sample rate
seconds = 1  # Duration
command_name = "on"  # Change this for each word
save_path = f"./data/{command_name}/"

if not os.path.exists(save_path):
    os.makedirs(save_path)

print(f"Recording 10 samples for '{command_name}'...")

for i in range(10):
    print(f"Sample {i+1}: Speak now!")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write(f"{save_path}{command_name}_{i}.wav", fs, recording)
    print("Saved.")

print("Done! Repeat for other commands.")
