from midi2audio import FluidSynth

# Specify the input MIDI file path
input_midi_file = "generation_1.mid"

# Specify the output WAV file path (replace with desired name)
output_wav_file = "converted_music.wav"

try:
  # Create a FluidSynth instance (ensure FluidSynth is installed)
  synth = FluidSynth()

  # Convert MIDI to audio using the specified output format (WAV)
  synth.midi_to_audio(input_midi_file, output_wav_file)

  print(f"MIDI file '{input_midi_file}' converted to WAV file '{output_wav_file}'.")

except Exception as e:
  print(f"Error during conversion: {e}")
