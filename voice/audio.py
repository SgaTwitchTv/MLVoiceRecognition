import torch
import torchaudio
import numpy as np
import soundfile as sf

from voice.config import SAMPLE_RATE, CLIP_SAMPLES

# A function to load audio from the file
def load_audio(file_path):
    audio, sample_rate = sf.read(file_path, dtype="float32", always_2d=True,)

    if len(audio) == 0:
        raise ValueError(f"Nagranie jest puste: {file_path}")

    if not np.isfinite(audio).all():
        raise ValueError(f"Nieprawidłowe wartości w nagraniu: {file_path}")

    mono_audio = audio.mean(axis=1)

    return mono_audio, sample_rate

# A function to transform a basic numpy table into PyTorch tensor
def prepare_waveform(mono_audio, source_sample_rate):
    if source_sample_rate <= 0:
        raise ValueError("Próbkowanie musi być dodatnie.")

    waveform = torch.from_numpy(mono_audio).float()

    if source_sample_rate != SAMPLE_RATE:
        waveform = torchaudio.functional.resample(waveform, orig_freq=source_sample_rate, new_freq=SAMPLE_RATE,)

    return waveform

# A function responsible for cropping a waveform
def crop_waveform(waveform):
    sample_count = waveform.shape[0]

    if sample_count < CLIP_SAMPLES:
        raise ValueError("Nagranie musi mieć co najmniej 3 sekundy.")

    start_index = (sample_count - CLIP_SAMPLES) // 2
    end_index = start_index + CLIP_SAMPLES

    return waveform[start_index:end_index]