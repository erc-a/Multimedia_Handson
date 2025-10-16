import librosa
import soundfile as sf

def cut_first_minute_librosa(input_path, output_path, start_seconds=0):
    # Load the audio file
    y, sr = librosa.load(input_path, sr=None)
    
    # Calculate start sample and end sample
    start_sample = int(sr * start_seconds)
    samples_per_minute = sr * 60
    end_sample = start_sample + samples_per_minute
    
    # Cut the audio from start_seconds for 60 seconds
    first_minute = y[start_sample:end_sample]
    
    # Save the cut audio
    sf.write(output_path, first_minute, sr)

# Input files
song1 = r"bruno_major_to_let_a_good_thing_die.wav"
song2 = r"bruno_mars_locked_out_of_heaven.wav"

# Output files
output1 = song1.replace(".wav", "_1min.wav")
output2 = song2.replace(".wav", "_1min.wav")

# Process both songs
# Bruno Major: mulai dari detik 0
cut_first_minute_librosa(song1, output1, start_seconds=0)

# Bruno Mars: mulai dari detik ke-3
cut_first_minute_librosa(song2, output2, start_seconds=3)

print("Done! First minute of both songs has been extracted.")
print(f"Bruno Major: 1 minute starting from 0 seconds")
print(f"Bruno Mars: 1 minute starting from 3 seconds")