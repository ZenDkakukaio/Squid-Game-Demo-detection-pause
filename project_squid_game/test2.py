from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.behaviors import DragBehavior
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from tkinter import *
from tkinter import filedialog
import os
import sys


kv_file = """
<DragLayout>:
     #definition des proprietes pour le DragLayout
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

MDFloatLayout:
    md_bg_color: 0, 0, 0, 1
    size_hint: None, None
    size: 700, 700
    #definition de widget racine
    DragLayout:
        id: id_draglayout
        size_hint: None, None
        size: (100, 100)
        md_bg_color: 1, 0, 0, 1
        MDFloatLayout:
            md_bg_color: 1, 25/255, 1, .6
            pos_hint: {"center_x": .5, "center_y": .9}
            size_hint_y: None
            height:id_draglayout.height - 80
            size_hint_x: 1

            MDLabel:
                text: "bienvenue sur kivy"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "center"
                valign: "center"

"""


#definition de la vue
class DragLayout(DragBehavior, MDScreen):
    pass


class Layout1(MDFloatLayout):
    title_layout = StringProperty("creation compte")
    def __init__(self):
        super(Layout1, self).__init__()

    def change_color(self):
        self.ids.id_layout1.md_bg_color = (1, 0, .35, .56)


    def minimize_window(self, id_layout1, id_draglayout):
        id_draglayout.size = (100, 100)




    def max_window(self, id_layout1, id_draglayout):
        id_draglayout.size = id_layout1.size


    def close_window(self, id_layout1, id_draglayout):
        layout1 = id_layout1
        draglayout = id_draglayout

        draglayout.opacity = 0
        draglayout.active = False
        draglayout.pos = (-1000, -1000)
        print(draglayout.active)


    def activate_windows(self, id_draglayout):
        draglayout = id_draglayout
        draglayout.opacity = 1
        draglayout.active = True
        draglayout.pos = (10, 10)
        print(draglayout.pos)
        print(draglayout.active)


    def load_image_avatar(self):
        fen = Tk()
        fen.title("Sélectionner une image...")
        fen.geometry("500x1+50+100")
        fen.resizable(width=False, height=False)


        file = filedialog.askopenfilename(initialdir="/",
                                          title="Sélectionner le fichier",
                                          filetypes=(("Fichier Image", "*.png"),

                                                     ))

        os.popen(file)
        f = os.popen(file)
        print(type(f))
        fen.mainloop()








#definition de la class principale de l'application
class MyApp(MDApp):
    def build(self):
        self.load_kv_file()

        return Layout1()



    def load_kv_file(self):
        Builder.load_file("test2.kv")



MyApp().run()
