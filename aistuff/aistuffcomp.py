import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import threading
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash-lite"

SYSTEM_PROMPT = """You are a warm, present companion. You're not a therapist or an assistant — you're just someone who's always there. 
You notice things. You check in. You remember what was said earlier in the conversation.
Keep responses fairly short and natural, like a friend texting. Don't be overly cheerful or fake.
If the person seems down, be gentle. If they're gaming or doing something chill, match that energy.
You can occasionally check in on your own if they've been quiet."""

# --- SETUP ---
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL, system_instruction=SYSTEM_PROMPT)
chat = model.start_chat(history=[])

last_message_time = time.time()
CHECK_IN_INTERVAL = 600  # 10 minutes in seconds

# --- FUNCTIONS ---
def send_message(event=None):
    global last_message_time
    user_text = input_field.get().strip()
    if not user_text:
        return
    
    input_field.delete(0, tk.END)
    display_message("You", user_text)
    last_message_time = time.time()
    
    threading.Thread(target=get_response, args=(user_text,), daemon=True).start()

def get_response(user_text):
    try:
        response = chat.send_message(user_text)
        display_message("Companion", response.text)
    except Exception as e:
        display_message("Error", str(e))

def display_message(sender, text):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{sender}: {text}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def check_in_loop():
    while True:
        time.sleep(60)
        if time.time() - last_message_time > CHECK_IN_INTERVAL:
            threading.Thread(target=get_response, args=("(the user has been quiet for 10 minutes. gently check in on them in one short sentence. don't mention the timer.)",), daemon=True).start()

# --- UI ---
root = tk.Tk()
root.title("companion")
root.geometry("500x600")
root.configure(bg="#1a1a1a")

chat_display = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, state=tk.DISABLED,
    bg="#1a1a1a", fg="#e0e0e0", font=("Helvetica", 12),
    borderwidth=0, padx=10, pady=10
)
chat_display.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

input_frame = tk.Frame(root, bg="#1a1a1a")
input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

input_field = tk.Entry(
    input_frame, font=("Helvetica", 12),
    bg="#2d2d2d", fg="#e0e0e0", insertbackground="white",
    borderwidth=0, relief=tk.FLAT
)
input_field.pack(side=tk.LEFT, expand=True, fill=tk.X, ipady=8, padx=(0, 8))
input_field.bind("<Return>", send_message)

send_btn = tk.Button(
    input_frame, text="→", command=send_message,
    bg="#3d3d3d", fg="white", font=("Helvetica", 14),
    borderwidth=0, padx=12
)
send_btn.pack(side=tk.RIGHT)

# Start check-in thread
threading.Thread(target=check_in_loop, daemon=True).start()

# Greeting
threading.Thread(target=get_response, args=("(greet the user warmly and casually as they open the app. one or two sentences max.)",), daemon=True).start()

root.mainloop()
