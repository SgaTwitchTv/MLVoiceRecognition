def cut_audio(samples, sample_rate, start_seconds, end_seconds):
    if sample_rate <= 0:
        raise ValueError("Czestotlwosc probkowania musi byc dodatnia")

    duration = len(samples) / sample_rate

    if start_seconds < 0:
        raise ValueError("Poczatek nie moze byc ujemny")

    if end_seconds <= start_seconds:
        raise ValueError("Koniec musi byc pozniej niz poczatek")

    if end_seconds > duration:
        raise ValueError("Koniec przekracza dlugosc nagrania")

    start_index = int(start_seconds * sample_rate)
    end_index = int(end_seconds * sample_rate)

    return samples[start_index:end_index]