from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class Dlt_a1(Screen):
    pass
class Dlt_a2(Screen):
    pass
class UI(ScreenManager):
    pass
class DLTApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    DLTApp().run()