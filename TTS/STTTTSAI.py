import speech_recognition as sr
import tkinter as tk
import pyttsx3
import threading
import queue
import time

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
        
        # Create the speech recognizer and configure settings
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000  # Adjusting for a higher sensitivity (background noise)
        self.recognizer.dynamic_energy_threshold = True  # Auto adjust to background noise
        self.language = "en-US"  # Set language to English (for recognition)
        
        # Text-to-Speech (TTS) engine initialization
        self.tts_engine = pyttsx3.init()
        english_voice = get_english_voice(self.tts_engine)
        if english_voice:
            self.tts_engine.setProperty('voice', english_voice)
        
        # Tkinter UI setup
        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening, bg="green", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Listening", command=self.stop_listening, bg="red", fg="white", state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.text_display = tk.Text(root, height=10, width=50)
        self.text_display.pack(pady=10)
        
        self.stop_listening_function = None
        
        # Queue for managing incoming audio chunks and the threads
        self.audio_queue = queue.Queue(maxsize=2)  # Limit the queue size to 2
        self.is_listening = False
        
        # Queue for TTS
        self.tts_queue = queue.Queue()  # TTS processing queue
        self.tts_thread = threading.Thread(target=self.process_tts_queue, daemon=True)
        self.tts_thread.start()

        # Buffer for accumulating words before speaking
        self.sentence_buffer = []  # Sentence buffer to store words as they are recognized
        self.buffer_lock = threading.Lock()

        # Flag for sentence completed
        self.sentence_completed = threading.Event()

    def append_word(self, word):
        """Thread-safe method to append text to the Text widget."""
        self.text_display.insert(tk.END, f"{word} ")
        self.text_display.see(tk.END)
    
    def speak_text(self, text):
        """Put the text in the TTS queue."""
        self.tts_queue.put(text)
    
    def process_tts_queue(self):
        """Worker thread that processes the TTS queue."""
        while True:
            text = self.tts_queue.get()  # Block until something is in the queue
            self.tts_engine.say(text)  # Speak the text
            # Allow TTS to be processed asynchronously
            self.tts_engine.runAndWait()  # This should now not block further actions

    def process_audio_segment(self, audio_segment):
        """Process each audio segment for speech recognition."""
        try:
            text = self.recognizer.recognize_google(audio_segment, language=self.language)
            if text:
                words = text.split()
                with self.buffer_lock:
                    self.sentence_buffer.extend(words)  # Add words to the buffer
                
                # Append recognized words to the display immediately
                for word in words:
                    self.root.after(0, self.append_word, word)
                
                # Trigger the check for sentence completion
                self.sentence_completed.clear()
                self.root.after(1000, self.check_sentence_completion)
        except sr.UnknownValueError:
            pass  # Could not understand audio; ignore and continue.
        except sr.RequestError:
            self.text_display.insert(tk.END, "\nNetwork error.\n")

    def check_sentence_completion(self):
        """Check if the sentence is complete after a 1-second pause in speech."""
        with self.buffer_lock:
            if self.sentence_buffer:
                sentence = " ".join(self.sentence_buffer)
                self.speak_text(sentence)
                self.sentence_buffer.clear()  # Clear the buffer after speaking
                self.sentence_completed.set()  # Indicate that the sentence is complete

    def listen_and_process_audio(self):
        """Main listening loop."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            while self.is_listening:
                try:
                    # Listen to the microphone in non-blocking mode, and pass it to the queue
                    audio_segment = self.recognizer.listen(source, timeout=5)
                    if self.audio_queue.full():
                        # If the queue is full, wait for the backup thread to finish before adding the next chunk
                        continue
                    self.audio_queue.put(audio_segment)  # Add the audio to the queue for processing
                except sr.WaitTimeoutError:
                    pass  # Timeout error, no speech detected
                except Exception as e:
                    print(f"Error listening: {e}")

    def process_audio(self):
        """Process the audio segment from the queue using the available thread."""
        while self.is_listening:
            if not self.audio_queue.empty():
                audio_segment = self.audio_queue.get()
                self.process_audio_segment(audio_segment)
    
    def start_listening(self):
        """Start listening and processing the audio in the background."""
        self.is_listening = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start the main listening loop in a separate thread
        self.listener_thread = threading.Thread(target=self.listen_and_process_audio, daemon=True)
        self.listener_thread.start()

        # Start the audio processing thread
        self.processor_thread = threading.Thread(target=self.process_audio, daemon=True)
        self.processor_thread.start()
    
    def stop_listening(self):
        """Stop listening and processing audio."""
        self.is_listening = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.text_display.insert(tk.END, "\nStopped listening.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = STTApp(root)
    root.mainloop()
