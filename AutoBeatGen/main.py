from modules.data_processing import get_notes_from_midi
from modules.Beat_gen import generate_beat_sequence
from modules.midi_generator import sequence_to_midi

def main():
    midi_root_dir = "C:\\Users\\haris\\Downloads\\lakh"  # Root folder for MIDI files

    print("Loading notes from MIDI files...")
    notes = get_notes_from_midi(midi_root_dir, limit=10)  # Adjust the limit as needed

    print(f"Extracted {len(notes)} notes/chords from MIDI files.")

    print("Generating beat sequence...")
    beat_sequence = generate_beat_sequence(notes, sequence_length=50)
    print(f"Generated beat sequence: {beat_sequence}")

    # Convert the beat sequence into a MIDI file
    print("Converting beat sequence to MIDI...")
    sequence_to_midi(beat_sequence, output_file="generated_beat.mid")

if __name__ == "__main__":
    main()
