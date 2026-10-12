from pathlib import Path

import torch

from voice.data_index import collect_recordings
from voice.audio import load_audio, prepare_waveform, crop_waveform
from voice.extractor import load_extractor, extract_embeddings

# A function that prepares the embeddings from the waves
def prepare_embeddings(directory, output_path, extractor):
    recordings = collect_recordings(directory)

    vectors = []
    labels = []
    speaker_ids = []
    source_files = []

    for audio_path, speaker_id, label in recordings:
        waveform, source_sample_rate = load_audio(audio_path)
        waveform_tensor = prepare_waveform(waveform, source_sample_rate)
        clip = crop_waveform(waveform_tensor)
        batch = clip.unsqueeze(0)

        embeddings = extract_embeddings(extractor, batch)
        vector = embeddings[0].cpu().clone()

        vectors.append(vector)
        labels.append(label)
        speaker_ids.append(speaker_id)
        source_files.append(str(audio_path))

        print("Przetworzono:", audio_path)

    features = torch.stack(vectors)
    targets = torch.tensor(labels, dtype=torch.float32)

    data = {
        "embeddings": features,
        "labels": targets,
        "speaker_ids": speaker_ids,
        "source_files": source_files,
        "extractor": "speechbrain/spkrec-ecapa-voxceleb",
        "sample_rate": 16000,
        "clip_seconds": 3,
    }

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    torch.save(data, output_path)

    print("Zapisano:", output_path)
    print("Embeddingi:", features.shape)
    print("Etykiety:", targets.shape)

# if we launch directly via shell, then go for the cast of the upper function
if __name__ == "__main__":
    extractor = load_extractor()
    prepare_embeddings(directory="data/train", output_path="embeddings/train.pt", extractor=extractor,)