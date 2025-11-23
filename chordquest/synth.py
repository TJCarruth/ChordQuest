import numpy as np
import pyaudio

# Audio Settings

Rate = 44100        # samples per second

duration = 2.0      # seconds


# Frequestionc for C maj chord

frequencies = [261.63, 329.63, 392.00] # C4, E4, G4


# Generate waveform

t = np.linspace(0, duration, int(Rate*duration), False)
wave = sum(np.sin(f*2**np.pi*t) for f in frequencies)
wave = (wave / np.max(np.abs(wave)) * 32767).astype(np.int16)


# Play audio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=Rate, output=True)
stream.write(wave.tobytes())
stream.stop_stream()
stream.close()
p.terminate()
