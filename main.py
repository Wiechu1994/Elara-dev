from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window

class ElaraChat(BoxLayout):
    def __init__(self, **kwargs):
        super(ElaraChat, self).__init__(orientation='vertical', **kwargs)

        self.output = Label(size_hint_y=None, text_size=(Window.width * 0.95, None), halign="left", valign="top")
        self.output.bind(texture_size=self.adjust_height)

        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.scroll.add_widget(self.output)

        self.input = TextInput(size_hint_y=0.1, hint_text="Zadaj pytanie Elarze...", multiline=False)
        self.send_button = Button(text="Wyślij", size_hint_y=0.05)
        self.send_button.bind(on_press=self.respond)

        self.add_widget(self.scroll)
        self.add_widget(self.input)
        self.add_widget(self.send_button)

        self.history = []

    def adjust_height(self, instance, size):
        self.output.height = size[1]

    def respond(self, instance):
        user_input = self.input.text.strip()
        if user_input:
            self.history.append(f"Ty: {user_input}")
            response = self.generate_response(user_input)
            self.history.append(f"Elara: {response}")
            self.output.text = '\n'.join(self.history)
            self.input.text = ""

    def generate_response(self, user_input):
        # Tu Elara może rozwinąć logikę — na razie placeholder.
        return f"Mmm... '{user_input}'? Interesujące pytanie, Mistrzu."

class ElaraApp(App):
    def build(self):
        self.title = "Elara Developer"
        return ElaraChat()

if __name__ == '__main__':
    ElaraApp().run()
