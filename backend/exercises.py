import random

from midi import MidiFile, MidiInstrument, MidiNote, to_audio_data


def rhythm_exercise(seed: int, bpm: int = 120, count_in: int = 4) -> bytes:

    all_notes = []
    for i in range(count_in):
        all_notes.append(
            MidiNote(
                note=36,
                velocity=90,
                time=i,
                duration=0.5,
                track=MidiInstrument.DRUMS,
            )
        )

    num_measures = 1
    num_notes = 4
    granularity = 0.5
    notes = []
    random.seed(seed)

    while len(notes) < num_notes:
        i = random.randint(0, num_measures * (int(1 / granularity) * 2) - 1) * granularity
        j = i + random.randint(1, int(1 / granularity)) * granularity
        valid = True
        for note in notes:
            if note.time <= i or note.time + note.duration > i:
                valid = False
                break
            if j > note.time and j < note.time + note.duration:
                valid = False
                break
            if j > num_measures * 4:
                valid = False
                break
        if valid:
            notes.append(
                MidiNote(
                    note=66,
                    velocity=120,
                    time=i + count_in,
                    duration=j - i,
                    track=MidiInstrument.PIANO,
                )
            )

    all_notes += notes
    print(all_notes)

    midi = MidiFile(bpm=bpm, notes=all_notes)
    return to_audio_data(midi)
