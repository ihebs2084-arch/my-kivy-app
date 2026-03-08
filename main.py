from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MindReaderPro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        Window.clearcolor = get_color_from_hex('#121212')

        self.add_widget(Label(text="Mind Reader Pro", font_size='32sp', bold=True, color=get_color_from_hex('#BB86FC')))
        self.add_widget(Label(text="فكر في رقم بين 1 و 10", font_size='18sp', color=get_color_from_hex('#E0E0E0')))

        self.user_input = TextInput(hint_text="أدخل رقمك هنا...", multiline=False, size_hint_y=None, height='50dp')
        self.add_widget(self.user_input)

        self.btn = Button(text="اقرأ عقلي الآن", size_hint_y=None, height='60dp', background_color=get_color_from_hex('#03DAC6'))
        self.btn.bind(on_press=self.read_mind)
        self.add_widget(self.btn)

        self.result_label = Label(text="", font_size='20sp', color=get_color_from_hex('#CF6679'))
        self.add_widget(self.result_label)
        self.add_widget(Label(text="Developed by Iheb Soltani Studio", font_size='12sp', color=get_color_from_hex('#757575')))

    def read_mind(self, instance):
        if self.user_input.text:
            self.result_label.text = f"عقلك يقول أن الرقم هو: {self.user_input.text}!"

class MindReaderApp(App):
    def build(self): return MindReaderPro()

if __name__ == "__main__": MindReaderApp().run()
