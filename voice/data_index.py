# Here we take recording paths and label them
from pathlib import Path
from speaker_labels import get_speaker_label

# Here we return an array structure of data about recordings
def collect_recordings(directory):
    directory = Path(directory)

    if not directory.is_dir():
        raise ValueError(f"Nie znaleziono katalogu: {directory}")

    recordings = []

    for speaker_folder in sorted(directory.iterdir()):
        if not speaker_folder.is_dir():
            continue

        speaker_id = speaker_folder.name
        label = get_speaker_label(speaker_id)

        for audio_path in sorted(speaker_folder.glob("*.wav")):
            recordings.append((audio_path, speaker_id, label))

    if len(recordings) == 0:
        raise ValueError(f"Brak nagrań WAV w katalogu: {directory}")

    return recordings

# We check how many people and recordings of each class we have in the data
def summarize_recordings(recordings):
    recording_counts = {0: 0, 1: 0}
    speakers = {0: set(), 1: set()}

    for audio_path, speaker_id, label in recordings:
        recording_counts[label] += 1
        speakers[label].add(speaker_id)

    for label in (0, 1):
        print("Klasa:", label, "| Nagrania:", recording_counts[label], "| Osoby:", len(speakers[label]),)

    if recording_counts[0] == 0 or recording_counts[1] == 0:
        raise ValueError("Zbiór musi zawierać nagrania obu klas.")