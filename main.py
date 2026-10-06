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