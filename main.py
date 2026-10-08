import audio_utils as au
import numpy as np
import soundfile as sf

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

#sf.read zwraca 2 wartosci: audio i sample rate
#audio to tablica probek
#sample_rate - liczba probek na sekunde
audio, sample_rate = sf.read("nagranie.wav", dtype="float32", always_2d=True)
print("Ksztalt: ", audio.shape)
print("Probkowanie: ", sample_rate)

mono_audio = audio.mean(axis=1)
print("Ksztalt mono: ", mono_audio.shape)
print("Pierwsze probki: ", mono_audio[:10])

duration = len(mono_audio) / sample_rate
print("Dlugosc w sekundach: ", duration)

fragment = au.cut_audio(mono_audio, sample_rate, start_seconds=0.0, end_seconds=1.0)
print("Liczba probek fragmentu: ", len(fragment))