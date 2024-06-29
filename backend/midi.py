import platform
import subprocess
from dataclasses import dataclass
from enum import Enum
from io import BytesIO
from itertools import groupby
from pathlib import Path
from typing import Dict, Iterator, List, Self, Tuple, Union

import mido
import numpy as np

FILES_DIR = Path(__file__).parent / "files"
TMP_DIR = FILES_DIR / "tmp"
SOUND_FONTS_DIR = FILES_DIR / "sound_fonts"
# SAMPLE_RATE: int = 44100
TICKS_PER_BEAT: int = 64

MIDI_DRIVER = {
    "Windows": "dsound",
    "Linux": "alsa",
    "Darwin": "coreaudio",
}[platform.system()]


class MidiInstrument(Enum):
    DRUMS = "Drums.sf2"
    PIANO = "Piano.sf2"

    @property
    def num(self) -> int:
        return {
            MidiInstrument.DRUMS: 0,
            MidiInstrument.PIANO: 1,
        }[self]


@dataclass
class NoteOn:
    track_num: int
    time: int  # in ticks
    note: int
    velocity: int

    @property
    def args(self) -> Tuple[int, int, int]:
        return self.track_num, self.note, self.velocity

    def message(self, t0: int) -> mido.Message:
        return mido.Message(
            "note_on", time=self.time - t0, channel=self.track_num, note=self.note, velocity=self.velocity
        )


@dataclass
class NoteOff:
    track_num: int
    time: int
    note: int

    @property
    def args(self) -> Tuple[int, int]:
        return self.track_num, self.note

    def message(self, t0: int) -> mido.Message:
        return mido.Message("note_off", time=self.time - t0, channel=self.track_num, note=self.note)


NoteSignal = Union[NoteOn, NoteOff]


@dataclass
class MidiNote:
    note: int
    velocity: int
    time: float  # in quarter notes
    duration: float  # in quarter notes
    track: MidiInstrument

    def __hash__(self):
        return hash((self.note, self.time))

    @property
    def on_tick(self) -> int:
        return int(self.time * TICKS_PER_BEAT)

    @property
    def on(self) -> NoteOn:
        return NoteOn(
            track_num=self.track.num,
            time=self.on_tick,
            note=self.note,
            velocity=self.velocity,
        )

    @property
    def off_tick(self) -> int:
        return int((self.time + self.duration) * TICKS_PER_BEAT)

    @property
    def off(self) -> NoteOff:
        return NoteOff(
            track_num=self.track.num,
            time=self.off_tick,
            note=self.note,
        )


@dataclass
class MidiFile:
    bpm: int
    notes: list[MidiNote]

    def enumerate_note_signals(self) -> Iterator[Tuple[int, Dict[int, List[NoteSignal]]]]:
        note_ons = [note.on for note in self.notes]
        note_offs = [note.off for note in self.notes]
        signals = sorted(note_ons + note_offs, key=lambda x: x.time)
        for time, group in groupby(signals, key=lambda x: x.time):
            yield time, {track_num: list(signal) for track_num, signal in groupby(group, key=lambda x: x.track_num)}

    def to_bytes(self) -> bytes:
        mid = mido.MidiFile(type=1, ticks_per_beat=TICKS_PER_BEAT)
        tick_track = mido.MidiTrack()
        tick_track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm)))
        # set sound font to drumset 0
        tick_track.append(mido.Message("program_change", channel=0, program=115))
        # tick_track.append(mido.Message("control_change", channel=0, control=9, value=120, skip_checks=True))

        piano_track = mido.MidiTrack()
        piano_track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm)))

        mid.tracks.append(tick_track)
        mid.tracks.append(piano_track)

        tracks = [tick_track, piano_track]
        t0: list[int] = [0 for _ in tracks]
        t1: list[int] = [0 for _ in tracks]

        for tick, signals in self.enumerate_note_signals():
            for track_num, track_signals in signals.items():
                t1[track_num] = tick
                for signal in track_signals:
                    tracks[track_num].append(signal.message(t0[track_num]))
                t0[track_num] = t1[track_num]

        midi_out = BytesIO()
        mid.save(file=midi_out)
        return midi_out.getvalue()


def to_audio_data(midi: MidiFile) -> bytes:

    midi_file_path = TMP_DIR / "temp.mid"
    audio_file_path = TMP_DIR / "temp.wav"

    midi_file_path.write_bytes(midi.to_bytes())

    timidity_command = ["timidity", "-Ow", "-o", str(audio_file_path), str(midi_file_path)]
    subprocess.run(timidity_command)

    audio_data = audio_file_path.read_bytes()

    audio_file_path.unlink()
    midi_file_path.unlink()

    return audio_data
