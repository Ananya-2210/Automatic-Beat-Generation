import numpy as np

def generate_beat_sequence(notes, sequence_length=100):
    """Generate a beat sequence from the list of notes."""
    unique_notes = list(set(notes))  # Get all unique notes
    note_to_int = {note: i for i, note in enumerate(unique_notes)}

    # Generate a random sequence
    beat_sequence = np.random.choice(unique_notes, sequence_length)
    int_sequence = [note_to_int[note] for note in beat_sequence]

    print("Generated beat sequence:", beat_sequence)
    return int_sequence
