import os
import glob
from music21 import converter, instrument, note, chord

def get_notes_from_midi(root_dir, limit=None):
    """Parse all MIDI files recursively from the provided directory."""
    notes = []
    count = 0

    # Recursively search for all .mid files in the root directory and its subdirectories
    for folder, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(".mid"):
                midi_path = os.path.join(folder, filename)

                try:
                    midi = converter.parse(midi_path)
                    parts = instrument.partitionByInstrument(midi)
                    notes_to_parse = (
                        parts.parts[0].recurse() if parts else midi.flat.notes
                    )

                    for element in notes_to_parse:
                        if isinstance(element, note.Note):
                            notes.append(str(element.pitch))
                        elif isinstance(element, chord.Chord):
                            notes.append('.'.join(str(n) for n in element.normalOrder))

                    count += 1
                    if limit and count >= limit:
                        print(f"Loaded {limit} MIDI files.")
                        return notes  # Stop when limit is reached

                except Exception as e:
                    print(f"Error processing {midi_path}: {e}")

    print(f"Loaded {count} MIDI files in total.")
    return notes
