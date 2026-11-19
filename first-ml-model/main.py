import numpy as np
import soundfile as sf
from pathlib import Path


# these arrays are like a truth table
# the raw data processed --> the exact processing we applied
# none of this is learned data from the model! Just what we give it!
X = [] # In processed input
y = [] # The gain we applied to the input

audio_files = list(Path("audio").glob("*.wav")) # Point the program to the audio files

# Loop through audio files, convert to mono, and normalize amplitudes
for file in audio_files:

    audio, sr = sf.read(file)

    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    rms = np.sqrt(np.mean(audio ** 2))

# this model is learning a linear line through the processed audio (RMS) and
# the gain applied
# We ALWAYS extract features first. Raw audio means nothing to the model so we need 
# represent it in a useful way

