import speech_recognition as sr
import tkinter as tk
import pyttsx3
from threading import Thread

def get_english_voice(engine):
    """Return the voice id for the first English voice found."""
    voices = engine.getProperty('voices')
    for voice in voices:
        if "english" in voice.name.lower():
            return voice.id  # Return first English voice found
    return None  # Default to system voice if no English voice found

class STTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech-to-Text AI")
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 30  # Lower threshold for quicker response
        self.recognizer.dynamic_energy_threshold = True  # Auto adjust to background noise
        self.language = "en-US"  # Set language to English (for recognition)
        
        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening, bg="green", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Listening", command=self.stop_listening, bg="red", fg="white", state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.text_display = tk.Text(root, height=10, width=50)
        self.text_display.pack(pady=10)
        
        self.stop_listening_function = None
        
        # Initialize TTS engine and set to an English voice.
        self.tts_engine = pyttsx3.init()
        english_voice = get_english_voice(self.tts_engine)
        if english_voice:
            self.tts_engine.setProperty('voice', english_voice)
    
    def append_word(self, word):
        self.text_display.insert(tk.END, f"{word} ")
        self.text_display.see(tk.END)
    
    def callback(self, recognizer, audio):
        try:
            # Recognize speech using Google Speech Recognition with specified language.
            text = recognizer.recognize_google(audio, language=self.language)
            words = text.split()
            # Insert each word with a slight delay to simulate a real-time word-by-word update.
            for i, word in enumerate(words):
                self.root.after(i * 100, lambda w=word: self.append_word(w))
            # Launch TTS in a separate thread so it doesn't block further recognition.
            Thread(target=self.speak_text, args=(text,), daemon=True).start()
        except sr.UnknownValueError:
            pass  # Could not understand audio; ignore and continue.
        except sr.RequestError:
            self.text_display.insert(tk.END, "\nNetwork error.\n")
    
    def speak_text(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def start_listening(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        # Use a short ambient noise adjustment for faster calibration.
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Start background listening. The callback will be called for each detected phrase.
        self.stop_listening_function = self.recognizer.listen_in_background(sr.Microphone(), self.callback)
    
    def stop_listening(self):
        if self.stop_listening_function:
            self.stop_listening_function(wait_for_stop=False)
            self.stop_listening_function = None
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.text_display.insert(tk.END, "\nStopped listening.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = STTApp(root)
    root.mainloop()
