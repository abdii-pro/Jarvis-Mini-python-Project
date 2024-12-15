# Voice-Controlled Assistant - Jarvis

This Python project implements a simple voice-controlled assistant named "Jarvis" that can perform the following tasks:

### Features
1. **Open Popular Websites**: 
   - Commands like `open Google`, `open Facebook`, `open YouTube`, or `open LinkedIn` will launch the respective websites in a browser.
   
2. **Play Music**: 
   - You can play a song by saying `play <song_name>`. The program uses a `musicLibrary` module to fetch the corresponding song link and opens it in the browser.

3. **Voice-Activated**: 
   - Jarvis listens for the wake word `Jarvis` to activate itself and then waits for a follow-up command.

### How It Works
1. The script uses:
   - **`SpeechRecognition`**: For capturing and recognizing voice input.
   - **`pyttsx3`**: For text-to-speech functionality, enabling Jarvis to speak back to the user.
   - **`webbrowser`**: For opening web pages in the default browser.
   - A `musicLibrary` module (which must define a dictionary mapping song names to URLs).

2. **Flow**:
   - Jarvis initializes and waits for the wake word (`Jarvis`).
   - Once activated, it listens for a specific command, such as opening websites or playing a song, and executes the corresponding action.

### Requirements
To run this program, you need to install the following Python libraries:
```bash
pip install speechrecognition pyaudio
pip install pyttsx3
pip install setuptools
```

### Usage
1. Clone the repository and ensure Python 3 is installed.
2. Install the required packages listed above.
3. Run the script:
   ```bash
   python jarvis.py
   ```
4. Speak to Jarvis to control it using voice commands!

### Note
- The `musicLibrary` module is required for the "play" command to function. It should be a Python file containing a dictionary called `music`, with song names as keys and their respective URLs as values.
- Ensure your microphone is connected and configured correctly for accurate voice recognition.
