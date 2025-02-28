from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import pyttsx3

class TTSApp(App):
    def build(self):
        # Set up the main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title Label
        self.title_label = Label(text="My TTS", font_size=32, color=(1, 1, 1, 1))
        self.layout.add_widget(self.title_label)

        # Instruction Label
        self.instruction_label = Label(text="Type your entry below:", font_size=20, color=(1, 1, 1, 1))
        self.layout.add_widget(self.instruction_label)

        # TextInput for journal entries
        self.text_box = TextInput(size_hint_y=None, height=300, multiline=True, font_size=20)
        self.layout.add_widget(self.text_box)

        # Speak Button
        self.speak_button = Button(text="Speak", on_press=self.speak_text, font_size=20)
        self.layout.add_widget(self.speak_button)

        return self.layout

    def speak_text(self, instance):
        # Get the text from the TextInput and remove any extra spaces
        text = self.text_box.text.strip()
        if text:
            # Initialize the TTS engine
            engine = pyttsx3.init()
            # Set English voice (US/UK)
            voices = engine.getProperty('voices')
            for voice in voices:
                if "english" in voice.name.lower():
                    engine.setProperty('voice', voice.id)  # Set English voice
                    break
            # Speak the text
            engine.say(text)
            engine.runAndWait()

if __name__ == '__main__':
    TTSApp().run()
