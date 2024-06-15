from pydub import AudioSegment
import os

# Define the directory containing the audio files
directory = 'C:/Users/igor/Projects/AudioConcatenator/input_audio_files'

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Directory '{directory}' does not exist.")
    exit(1)

# List all files in the directory for debugging purposes
print("Files in directory:")
for filename in os.listdir(directory):
    print(filename)

# Initialize an empty AudioSegment
combined_audio = AudioSegment.empty()

# Iterate through all files in the directory
files_processed = 0
for filename in os.listdir(directory):
    if filename.endswith('.waptt.opus'):
        file_path = os.path.join(directory, filename)
        try:
            # Print debug message
            print(f"Attempting to load file: {file_path}")
            # Load the audio file without specifying the format
            audio = AudioSegment.from_file(file_path)
            # Concatenate the audio file to the combined audio
            combined_audio += audio
            print(f"Loaded and concatenated: {filename}")
            files_processed += 1
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            print("Trying to detect format automatically...")
            try:
                audio = AudioSegment.from_file(file_path)
                combined_audio += audio
                print(f"Loaded and concatenated with format detection: {filename}")
                files_processed += 1
            except Exception as e:
                print(f"Failed to load {filename} even with format detection: {e}")

# Check if there are any audio segments loaded
if files_processed == 0:
    print("No audio files were loaded. Please check the files in the directory.")
    exit(1)

# Export the combined audio as an MP3 file
output_file = "C:/Users/igor/Projects/AudioConcatenator/combined_audio.mp3"
combined_audio.export(output_file, format='mp3')

print(f"All audio files have been concatenated into {output_file}")
