from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class LoginScreen(Screen): 
    def submit_text(self,num):
        #self.ids.txt_num.text=num
        if num == "ac":
            self.ids.txt_num.text=""
        else:
            self.ids.txt_num.text=self.ids.txt_num.text+num

class MainScreen(Screen):    # UI1
    pass
class UI(ScreenManager): # จัดการหน้าจอต่างๆ
    pass

class otteriApp(App):
    def build(self):
        return UI()

if __name__=='__main__':
    otteriApp().run()