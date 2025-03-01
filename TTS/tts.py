import tkinter as tk
import pyttsx3

def get_english_voice():
    """Automatically selects an English voice (US or UK) if available."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "english" in voice.name.lower():
            return voice.id  # Return first English voice found
    return None  # Default to system voice if no English voice found

def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        english_voice = get_english_voice()
        if english_voice:
            engine.setProperty('voice', english_voice)  # Set English voice
        engine.say(text)
        engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Journal TTS Bot")
root.geometry("300x300")  
root.minsize(200, 200)  
root.configure(bg="#2e2a28")  # Dark theme

# Configure grid layout
root.grid_rowconfigure(2, weight=1)  
root.grid_columnconfigure(0, weight=1)

# Title label
title_label = tk.Label(root, text="My TTS", bg="#2e2a28",
    font=("Georgia", 20, "bold"), fg="#e0d6c9")
title_label.grid(row=0, column=0, pady=(10, 5), sticky="n")

# Instruction label
instruction_label = tk.Label(root, text="Type your entry below:", bg="#2e2a28",
    font=("Georgia", 14), fg="#c5b9ae")
instruction_label.grid(row=1, column=0, pady=(0, 10), sticky="n")

# Text box (dark theme)
text_box = tk.Text(root, font=("Times New Roman", 12), bg="#3b3633", fg="#e0d6c9",
    insertbackground="#e0d6c9", bd=2, relief="groove", wrap="word")
text_box.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# Button frame
button_frame = tk.Frame(root, bg="#2e2a28")
button_frame.grid(row=3, column=0, pady=10, sticky="s")

# Speak button (dark theme)
speak_button = tk.Button(button_frame, text="Speak", command=speak_text,
    font=("Georgia", 14), bg="#715b51", fg="#e0d6c9",
    activebackground="#8a7568", bd=2, relief="raised")
speak_button.pack()

root.mainloop()
