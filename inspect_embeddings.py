import torch

from voice.config import EMBEDDING_DIM

# Loading data to the network   
data = torch.load("embeddings/train.pt", map_location="cpu", weights_only=True,)

features = data["embeddings"]
labels = data["labels"]
speaker_ids = data["speaker_ids"]
source_files = data["source_files"]

print("Ekstraktor:", data["extractor"])
print("Embeddingi:", features.shape)
print("Etykiety:", labels.shape)

# Structure control
if features.ndim != 2:
    raise ValueError("Embeddingi muszą mieć dwa wymiary: [N, 192].")

if features.shape[1] != EMBEDDING_DIM:
    raise ValueError("Nieprawidłowa długość embeddingu.")

if labels.ndim != 1:
    raise ValueError("Etykiety muszą mieć jeden wymiar: [N].")

example_count = features.shape[0]

if example_count == 0:
    raise ValueError("Zbiór jest pusty.")

if labels.shape[0] != example_count:
    raise ValueError("Liczba etykiet nie odpowiada liczbie embeddingów.")

if len(speaker_ids) != example_count or len(source_files) != example_count:
    raise ValueError("Brakuje opisów niektórych przykładów.")

# Value control
if not torch.isfinite(features).all().item():
    raise ValueError("Embeddingi zawierają NaN lub nieskończoności.")

valid_labels = (labels == 0) | (labels == 1)

if not valid_labels.all().item():
    raise ValueError("Etykiety muszą mieć wartość 0 albo 1.")

print("Pierwsza osoba:", speaker_ids[0])
print("Pierwszy plik:", source_files[0])
print("Pierwsza etykieta:", labels[0].item())
print("Pierwsze 10 cech:", features[0, :10])

print("Struktura i wartości danych: OK")