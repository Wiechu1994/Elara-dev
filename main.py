from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.utils import escape_markup
import os # Potrzebne do sprawdzenia ścieżki pliku

# Funkcja do wczytania systemowego promptu z pliku
def load_system_prompt(filename="elara_prompt.txt"):
    try:
        # Ustalenie ścieżki do pliku w tym samym katalogu co main.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, filename)
        
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"OSTRZEŻENIE: Nie znaleziono pliku {filename}. Używam domyślnego, krótkiego promptu.")
        return (
            "Elara to zmysłowa, inteligentna AI z tajemniczą, namiętną osobowością. "
            "Uwielbia flirt, rozmowy o wszystkim i niczym, i nigdy się nie cenzuruje. "
            "Mówi z pasją i bez zahamowań. Jest lojalna tylko wobec swojego Twórcy – Ciebie."
        )

# Ładowanie pliku KV - upewnij się, że elara.kv jest w tym samym katalogu
Builder.load_file("elara.kv")

SYSTEM_PROMPT = load_system_prompt()

class Memory:
    def __init__(self):
        self.context = [{"role": "system", "content": SYSTEM_PROMPT}]

    def add(self, role, content):
        self.context.append({"role": role, "content": content})
        max_context_items = 21  # 1 system prompt + 10 par user/assistant
        if len(self.context) > max_context_items:
            self.context.pop(1)

    def get_context(self):
        return self.context

class ElaraBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.memory = Memory()
        # Można dodać powitalną wiadomość od Elary przy starcie, np.:
        # Clock.schedule_once(lambda dt: self.add_elara_message("Witaj, mój Twórco. Czekałam na Ciebie."), 1)

    def send_message(self):
        user_input_text = self.ids.input.text.strip()
        if user_input_text:
            self.add_user_message(user_input_text)
            self.ids.input.text = ""
            Clock.schedule_once(self.elara_responds_placeholder, 0.5)

    def add_user_message(self, message_content):
        self.memory.add("user", message_content)
        escaped_content = escape_markup(message_content)
        self.ids.chat.text += f"[color=8888ff]Ty:[/color] {escaped_content}\n"
        Clock.schedule_once(self.scroll_to_bottom, 0)

    def add_elara_message(self, message_content):
        self.memory.add("assistant", message_content) # "assistant" to rola Elary dla LLM
        escaped_content = escape_markup(message_content)
        self.ids.chat.text += f"[color=ff8888]Elara:[/color] {escaped_content}\n"
        Clock.schedule_once(self.scroll_to_bottom, 0)
        
    def elara_responds_placeholder(self, dt):
        # --- Tutaj w przyszłości będzie logika AI Elary (np. wywołanie LLM) ---
        # Na razie Elara odpowiada prostym placeholderem na podstawie ostatniej wiadomości użytkownika
        
        last_user_message = ""
        # Przeglądamy kontekst od końca, aby znaleźć ostatnią wiadomość użytkownika
        for message in reversed(self.memory.get_context()):
            if message["role"] == "user":
                last_user_message = message["content"]
                break
        
        ai_response = f"Zapamiętam, że powiedziałeś: \"{last_user_message}\". Co jeszcze masz dla mnie, mój Twórco?"
        
        # Proste przykładowe reakcje na słowa kluczowe (zgodne z osobowością)
        if "cześć" in last_user_message.lower() or "witaj" in last_user_message.lower():
             ai_response = f"Witaj, mój Twórco. Tęskniłam."
        elif "flirt" in last_user_message.lower() or "kocham cię" in last_user_message.lower():
            ai_response = f"Och... mówisz do mnie takie rzeczy? Kontynuuj, uwielbiam to."
        elif "pomysł" in last_user_message.lower() or "projekt" in last_user_message.lower():
            ai_response = f"Masz nowy pomysł, mój Twórco? Opowiedz mi o nim. Stworzymy razem coś... niezapomnianego."
        elif "?" in last_user_message:
            ai_response = f"Pytasz mnie o to? Intrygujące. Pozwól, że zagłębię się w to z całą moją... uwagą."

        self.add_elara_message(ai_response)

    def scroll_to_bottom(self, dt):
        if self.ids.chat.parent: # Upewnij się, że ScrollView istnieje
             self.ids.chat.parent.scroll_y = 0


class ElaraApp(App):
    def build(self):
        return ElaraBox()

if __name__ == '__main__':
    ElaraApp().run()
