import sounddevice as sd
import numpy as np
import queue
import threading
import whisper
import scipy.io.wavfile as wav
import time
import os
import requests

# ========================
# CONFIG
# ========================

SAMPLE_RATE = 16000
CHUNK_DURATION = 120  # seconds
OVERLAP = 10          # seconds overlap
NOTE_FILE = "lecture_notes.md"
MODEL_SIZE = "base"   # whisper model
MAX_CONTEXT = 6000    # characters for memory

q = queue.Queue()
model = whisper.load_model(MODEL_SIZE)

previous_notes = ""

# ========================
# AUDIO RECORDING
# ========================

def record_loop():
    chunk_id = 0
    buffer = np.array([], dtype=np.int16)

    while True:
        print(f"[REC] Recording chunk {chunk_id}")

        recording = sd.rec(int(CHUNK_DURATION * SAMPLE_RATE),
                           samplerate=SAMPLE_RATE,
                           channels=1,
                           dtype='int16')
        sd.wait()

        recording = recording.flatten()

        # Add overlap from previous chunk
        if len(buffer) > 0:
            recording = np.concatenate((buffer, recording))

        filename = f"chunk_{chunk_id}.wav"
        wav.write(filename, SAMPLE_RATE, recording)

        # Save last OVERLAP seconds
        overlap_samples = OVERLAP * SAMPLE_RATE
        buffer = recording[-overlap_samples:]

        q.put(filename)
        chunk_id += 1


# ========================
# TEXT CLEANING
# ========================

def clean_text(text):
    return text.strip().replace("  ", " ")


# ========================
# CONTEXT TRIMMING
# ========================

def trim_context(text):
    return text[-MAX_CONTEXT:]


# ========================
# LOCAL AI STRUCTURING
# ========================

def structure_with_ai(new_text, old_notes):
    prompt = f"""
You are an intelligent lecture note system.

Previous notes:
{old_notes}

New transcript:
{new_text}

Tasks:
- Merge if it's the same concept
- Create new sections if needed
- Keep it concise and structured
- Use Markdown headings (#, ##)
- Detect math and format like: f(x) = x^2
- Avoid repetition
- Keep only useful information

Return ONLY the updated notes.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# ========================
# PROCESSING LOOP
# ========================

def process_loop():
    global previous_notes

    while True:
        filename = q.get()
        print(f"[PROC] Transcribing {filename}")

        result = model.transcribe(filename)
        text = clean_text(result["text"])

        print(f"\n--- RAW ---\n{text}\n")

        try:
            updated_notes = structure_with_ai(text, previous_notes)
            previous_notes = trim_context(updated_notes)

            with open(NOTE_FILE, "w") as f:
                f.write(previous_notes)

            print("[NOTE] Updated")

        except Exception as e:
            print(f"[ERROR] AI processing failed: {e}")

        os.remove(filename)


# ========================
# THREADS
# ========================

threading.Thread(target=record_loop, daemon=True).start()
threading.Thread(target=process_loop, daemon=True).start()

print("System running... Press Ctrl+C to stop.")

while True:
    time.sleep(1)