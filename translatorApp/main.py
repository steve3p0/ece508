import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('1.9.0')
# 2.0.0


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))


class TranslatorApp(App):

    def build(self):
        # return Label(text="NeuralRandom")
        return MyRoot()


translatorapp = TranslatorApp()
translatorapp.run()