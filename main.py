<<<<<<< HEAD
sample_rate = 16000
samples = [0.02, 0.08, -0.04, -0.12]

def sample_time(index, sample_rate):
    return index / sample_rate

def peak_amplitude(samples):
    peak = 0.0

    for sample in samples:
        amplitude = abs(sample)
        if(amplitude > peak):
            peak = amplitude

    return peak

def apply_gain(samples, gain):
    result = []

    for sample in samples:
        new_sample = sample * gain
        result.append(new_sample)

    return result

def normalize_audio(samples):
    peak = peak_amplitude(samples)
    if(peak == 0):
        return samples.copy()

    gain = 1.0 / peak
    return apply_gain(samples, gain)

normailzed_samples = normalize_audio(samples)

print("Przed: ", samples)
print("Po: ", normailzed_samples)
print("Szczyt po: ", peak_amplitude(normailzed_samples))
=======
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
>>>>>>> abc6146285783dc69d031745aa901c5908ad5816
