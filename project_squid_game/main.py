from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
#from kivymd_extensions.akivymd import *
from kivy.config import Config

#from test import MyWindows
from layout import MyLayout
#from kivymd_extensions.akivymd.uix.windows import AKFloatingWindow
import json as j


Config.set("kivy", "window_icon", "")

with open("../project_game_squid_game/media/json_file/f1.json") as f:
    data = j.load(f)




#Window.size = (1440, 900)





class MyGame(MDApp):

    def build(self):
        self.icon = data["logo_game"]["img1"]
        self.title = "SG version béta"
        self.load_file_kv()
        self.theme_cls.theme_style = "Dark"

        return MyLayout()
        #return MyWindows()


    def load_file_kv(self):
        Builder.load_file("layout.kv")
        #Builder.load_file("test.kv")




if __name__ == '__main__':
    obj = MyGame()
    obj.run()