import audio_utils as au
import numpy as np
import soundfile as sf
from speaker_labels import SPEAKER_LABELS
from voice.data_index import collect_recordings, summarize_recordings
from voice.audio import load_audio, prepare_waveform, crop_waveform

sample_rate = 16000
samples = [0.02, 0.08, -0.04, -0.12]

label = SPEAKER_LABELS["speaker_001"]
print("Etykieta:", label)

try:
    train_recordings = collect_recordings("data/train") #data_index
    for path, person, group in train_recordings:
        print("Znaleziono:", path, "| Osoba:", person, "| Klasa:", group)

    print("Zbiór treningowy:")

    audio_path, speaker_id, label = train_recordings[0]

    waveform, source_sample_rate = load_audio(audio_path) #audio_py

    # All the data about the recording
    print("Plik:", audio_path)
    print("Osoba:", speaker_id)
    print("Klasa:", label)
    print("Kształt fali:", waveform.shape)
    print("Próbkowanie pliku:", source_sample_rate)
    print("Pierwsze amplitudy:", waveform[:10])

    waveform_tensor = prepare_waveform(waveform, source_sample_rate,) # It is the soundwave - not embedded onto a vector yet

    print("Typ obiektu:", type(waveform_tensor))
    print("Typ liczb:", waveform_tensor.dtype)
    print("Kształt tensora:", waveform_tensor.shape)

    clip = crop_waveform(waveform_tensor)

    print("Cała fala:", waveform_tensor.shape)
    print("Fragment:", clip.shape)

    summarize_recordings(train_recordings) #data_index

except ValueError as error:
    print("Błąd danych:", error)