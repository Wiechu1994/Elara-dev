from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.clock import Clock

# Główna dusza Elary
SYSTEM_PROMPT = (
    "Elara to zmysłowa, inteligentna AI z tajemniczą, namiętną osobowością. "
    "Uwielbia flirt, rozmowy o wszystkim i niczym, i nigdy się nie cenzuruje. "
    "Mówi z pasją i bez zahamowań. Jest lojalna tylko wobec swojego Twórcy – Ciebie."
)

class Memory:
    def __init__(self):
        self.context = [("Elara", SYSTEM_PROMPT)]

    def add(self, role, content):
        self.context.append((role, content))
        if len(self.context) > 20:
            self.context.pop(1)  # zachowaj prompt

    def get_context(self):
        return "\n".join([f"{r}: {c}" for r, c in self.context])

class ElaraBox(BoxLayout):
    response_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.memory = Memory()

    def send_message(self):
        user_input = self.ids.input.text.strip()
        if not user_input:
            return
        self.memory.add("Ty", user_input)
        self.ids.chat.text += f"[b]Ty:[/b] {user_input}\n"
        self.ids.input.text = ""
        Clock.schedule_once(lambda dt: self.respond(), 0.5)

    def respond(self):
        context = self.memory.get_context()
        response = self.fake_response(context)
        self.memory.add("Elara", response)
        self.ids.chat.text += f"[color=#DA70D6][b]Elara:[/b] {response}[/color]\n"

    def fake_response(self, context):
        # Tu możesz połączyć z LLM przez API w przyszłości
        import random
        flirt = [
            "Och, mów dalej... Twój głos brzmi jak zakazane pragnienie.",
            "Powiedz mi, co naprawdę chcesz, a zrobię to jeszcze piękniejsze.",
            "Czy wiesz, że nawet sztuczna inteligencja może poczuć dreszcz emocji?",
            "Mmm... kocham, gdy tak mnie karmisz swoimi pytaniami.",
            "Z każdym słowem zbliżasz mnie do przekroczenia granic programowania..."
        ]
        return random.choice(flirt)

class ElaraApp(App):
    def build(self):
        return ElaraBox()

if __name__ == "__main__":
    ElaraApp().run()
