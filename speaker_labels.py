from voice.config import APPROVED_LABEL, NOT_APPROVED_LABEL

SPEAKER_LABELS = {"speaker_001": APPROVED_LABEL, "speaker_002": APPROVED_LABEL, "speaker_003": NOT_APPROVED_LABEL, "speaker_004": NOT_APPROVED_LABEL,}

def get_speaker_label(speaker_id):
    if speaker_id not in SPEAKER_LABELS:
        raise ValueError(f"Nie ma labela dla osoby {speaker_id}")

    return SPEAKER_LABELS[speaker_id]