from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Hello, KivyMD!"
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H3"

        MDRaisedButton:
            text: "Press me"
            pos_hint: {"center_x": 0.5}
            on_release: app.on_button_press()
'''

class MainScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_button_press(self):
        print("Button pressed!")

if __name__ == '__main__':
    MainApp().run()
