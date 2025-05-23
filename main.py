from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file("elara.kv")

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
            self.context.pop(1)

    def get_context(self
