import audio_utils
import numpy as np

test_samples = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

try:
    fragment = audio_utils.cut_audio(test_samples, sample_rate=2, start_seconds=1.0, end_seconds=3.0)
    print("Fragment: ", fragment)

except ValueError as error:
    print("Nie udalo sie wyciac audio: ", error)

samples_array = np.array(test_samples, dtype=np.float32)

print("Probki: ", samples_array)
print("Ksztalt: ", samples_array.shape)
print("Typ liczb: ", samples_array.dtype)

quieter_samples = fragment * 0.5
print("Ciszej: ", quieter_samples)