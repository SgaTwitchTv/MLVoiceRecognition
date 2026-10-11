import audio_utils as au
import numpy as np
import soundfile as sf
from speaker_labels import SPEAKER_LABELS
from voice.data_index import collect_recordings, summarize_recordings
from voice.audio import load_audio, prepare_waveform

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

####################################################################

label = SPEAKER_LABELS["speaker_001"]
print("Etykieta:", label)

try:
    train_recordings = collect_recordings("data/train") #data_index

    print("Zbiór treningowy:")
    summarize_recordings(train_recordings) #data_index

    audio_path, speaker_id, label = train_recordings[0]

    waveform, source_sample_rate = load_audio(audio_path) #audio_py

    # All the data about the recording
    print("Plik:", audio_path)
    print("Osoba:", speaker_id)
    print("Klasa:", label)
    print("Kształt fali:", waveform.shape)
    print("Próbkowanie pliku:", source_sample_rate)
    print("Pierwsze amplitudy:", waveform[:10])

    waveform_tensor = prepare_waveform(waveform, source_sample_rate,)

    print("Typ obiektu:", type(waveform_tensor))
    print("Typ liczb:", waveform_tensor.dtype)
    print("Kształt tensora:", waveform_tensor.shape)

except ValueError as error:
    print("Błąd danych:", error)