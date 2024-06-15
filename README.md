# AudioConcatenator

AudioConcatenator is a Python script designed to concatenate multiple audio files in the `.waptt.opus` format into a single MP3 file. This format is typically generated when downloading audio samples from WhatsApp. The primary goal of this tool is to create a consolidated audio sample of a voice, which can be used in voice cloning software or text-to-speech (TTS) libraries.

## Objective

The main objective of this project is to provide an easy way to concatenate multiple WhatsApp audio samples (in `.waptt.opus` format) into one continuous MP3 file. This is particularly useful for creating a comprehensive audio sample of a voice, which can be used for various purposes such as voice cloning and text-to-speech (TTS) applications.

## Requirements

- Python 3.x
- pydub library
- ffmpeg

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AudioConcatenator.git
   cd AudioConcatenator

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required Python packages:
```bash
pip install pydub
```

Ensure you have ffmpeg installed:

On Ubuntu:
sudo apt-get install ffmpeg
sudo apt-get install ffmpeg
On macOS using Homebrew:
bash
Copiar código
brew install ffmpeg
On Windows, download and install ffmpeg from ffmpeg.org and add it to your system PATH.
Usage
Place all your .waptt.opus audio files in the input_audio_files directory.

Run the script:

bash
Copiar código
python main.py
The concatenated audio will be saved as combined_audio.mp3 in the project directory.

Example
Suppose you have the following .waptt.opus files in the input_audio_files directory:

Audio WhatsApp 2024-04-30 14.57.37.waptt.opus
Audio WhatsApp 2024-04-30 19.14.42.waptt.opus
Audio WhatsApp 2024-05-23 11.40.41.waptt.opus
Running the script will concatenate these files into a single MP3 file named combined_audio.mp3.

Troubleshooting
If you encounter any issues with loading the files or ffmpeg, ensure that:

The ffmpeg executable is properly installed and added to your system PATH.
The .waptt.opus files are correctly placed in the input_audio_files directory.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

Happy coding!

markdown
Copiar código

### Additional Steps

1. Save the above content in a file named `README.md` in the root directory of your project.
2. Ensure your directory structure looks like this:

AudioConcatenator/
├── input_audio_files/
│ ├── Audio WhatsApp 2024-04-30 14.57.37.waptt.opus
│ ├── Audio WhatsApp 2024-04-30 19.14.42.waptt.opus
│ └── ... (other .waptt.opus files)
├── venv/
├── combined_audio.mp3
├── main.py
└── README.md

sql
Copiar código

3. Commit your changes to the repository:

```bash
git add README.md
git commit -m "Add README.md"
git push origin main
This README provides clear instructions on the project's purpose, requirements, installation steps, usage, and troubleshooting, making it easy for others to understand and use your project.
