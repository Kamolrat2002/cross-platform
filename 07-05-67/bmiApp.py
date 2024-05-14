from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Scr_bmi(Screen): 
    pass
     
class Scr_knowledge(Screen):
    pass

class UI(ScreenManager):
    pass

class bmiApp(App):
    def build(self):
        return UI()

if __name__=='__main__':
    bmiApp().run()