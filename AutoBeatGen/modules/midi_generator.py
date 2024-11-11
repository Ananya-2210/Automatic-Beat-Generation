from music21 import stream, note, chord

def sequence_to_midi(sequence, output_file="generated_beat.mid"):
    """
    Convert the generated beat sequence (notes and integers) to a MIDI file.
    """
    # Create a new stream to hold the notes/chords
    midi_stream = stream.Stream()

    for element in sequence:
        if isinstance(element, int):  # If it's an integer, treat it as a note pitch
            # Convert the integer to a MIDI note (e.g., 60 = C4)
            new_note = note.Note(element)
            midi_stream.append(new_note)
        elif '.' in element:  # If it's a chord represented by a string
            chord_notes = [int(n) for n in element.split('.')]
            new_chord = chord.Chord(chord_notes)
            midi_stream.append(new_chord)
        else:  # Single note represented by a string (e.g., 'F#4')
            new_note = note.Note(element)
            midi_stream.append(new_note)

    # Write the stream to a MIDI file
    midi_stream.write('midi', fp=output_file)
    print(f"MIDI file generated: {output_file}")
