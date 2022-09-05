from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.audio import SoundLoader
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.animation import Animation
from kivy.metrics import dp


from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from datetime import datetime
from time import strftime

from project_game_squid_game.start import MyGameStart

from project_game_squid_game.database.modele import MyGamePlayer
import re
import webbrowser

import json as j






with open("../project_game_squid_game/media/json_file/f1.json") as f1:
    data = j.load(f1)






class MyLayout(ScreenManager):

    data_logo_game = data["logo_game"]["img1"]
    data_font1 = data["font1"]["game_of_squid"]
    data_acceuil_flou = data["acceuil_flou"]["img1"]
    data_sc_sc2 = data["bg_screen2"]["img1"]
    data_authentification = data["bg_authentification"]["img1"]
    data_poupe = data["poupe"]["img1"]
    data_chef = data["chef"]["img1"]
    data_coq = data["coq"]["img1"]
    data_lapin = data["lapin"]["img1"]
    data_taureau = data["taureau"]["img1"]
    data_piece1 = data["piece1"]["img1"]
    data_piece2 = data["piece2"]["img1"]
    data_piece3 = data["piece3"]["img1"]
    data_piece4 = data["piece4"]["img1"]
    data_piece5 = data["piece5"]["img1"]
    data_piece6 = data["piece6"]["img1"]
    data_piece7 = data["piece7"]["img1"]
    data_element1 = data["element1"]["img1"]
    data_element2 = data["element2"]["img1"]
    data_element3 = data["element3"]["img1"]
    data_element4 = data["element4"]["img1"]
    data_element5 = data["element5"]["img1"]
    data_element6 = data["element6"]["img1"]
    data_element7 = data["element7"]["img1"]
    data_element8 = data["element8"]["img1"]
    data_logo2_squid_game = data["logo2_squid_game"]["img1"]
    data_plate_menu = data["plate_menu"]["img1"]
    data_tuto1 = data["tuto1"]["tuto1"]
    data_tuto2 = data["tuto2"]["tuto2"]
    data_tuto3 = data["tuto3"]["tuto3"]
    data_tuto4 = data["tuto4"]["tuto4"]
    data_tuto5 = data["tuto5"]["tuto5"]
    data_tuto6 = data["tuto6"]["tuto6"]




    number_load = StringProperty("0")

    count = 1

    data_about = {
        "code source": "github",
        "infos": "information",
    }







    state_screen1 = True


    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        #self.verify_account_in_info_screen()
        self.manager_open = False
        self.file_manager_avatar = MDFileManager(
            exit_manager = self.exit_manager,
            select_path = self.select_path,
            preview = True,
            show_hidden_files = True
        )

        self.dialog = None
        self.state_audio_intro = True





    def push_sound_effect_click(self):
        c = SoundLoader.load("../project_game_squid_game/media/sound/audio_1_squid_game6.wav")
        if c:
            c.play()


    def push_sound_effect_click_2(self):
        c = SoundLoader.load("../project_game_squid_game/media/sound/audio_1_squid_game2.wav")
        if c:
            c.play()




    def call_timer(self):
        self.push_sound_effect_click()
        Clock.schedule_interval(self.account, 1/20)




    def push_sound_intro(self, dt):

        s = SoundLoader.load("../project_game_squid_game/media/sound/audio_1_squid_game11.wav")
        if s:

            time_sound_intro = s.length
            s.play()




    def account(self, dt):

        if self.state_screen1:
            self.count += 1
            self.number_load = str(self.count)
            if self.count == 100:
                self.count = 100
                self.number_load = "Validation des entrées..."
                toast("lancement du jeu...")


                return self.change_screen1()




        elif self.state_screen1 == False:
            toast("erreur lors du chargement du jeu...")

        else:
            toast("erreur lors du chargement du jeu...")





    def change_screen1(self):
        self.transition = SlideTransition(duration= .8, direction="left")
        self.current = "sc2"

        self.anim_piece()

        time_s = 0

        Clock.schedule_interval(self.push_sound_intro, 6.87)






    def open_didactiel(self,didac, one, options):
        self.push_sound_effect_click()
        options.opacity = 0
        didac.opacity = 0
        animation_didac = Animation(opacity=0)
        animation_didac += Animation(opacity=1, duration=2)
        animation_didac.start(one)




    def open_menu_game(self,menu_story ,menu_game):
        self.push_sound_effect_click()
        animation_story = Animation(opacity=0, duration=3)

        animation_story.start(menu_story)

        animation_game = Animation(opacity=0)
        animation_game += Animation(opacity=1, duration=5)
        animation_game.start(menu_game)


    def open_menu_story(self, menu_story, menu_game):
        self.push_sound_effect_click()
        animation_game = Animation(opacity=0, duration=3)

        animation_game.start(menu_game)

        animation_story = Animation(opacity=0)
        animation_story += Animation(opacity=1, duration=5)
        animation_story.start(menu_story)



    def  open_options(self, didac, one, options):
        self.push_sound_effect_click()
        didac.opacity = 0
        one.opacity = 0
        animation_options = Animation(opacity=0)
        animation_options += Animation(opacity=1, duration=1)
        animation_options.start(options)










    def anim_piece(self):
        self.get_eror_push_game()
        anim_piece1 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece1 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece1 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece1 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece1 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece1 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece1 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece1.start(self.ids.id_piece1)

        anim_piece2 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece2 += Animation(duration=2, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece2 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece2 += Animation(duration=2, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece2 += Animation(duration=2, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece2 += Animation(duration=2, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece2 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": .5})
        anim_piece2.start(self.ids.id_piece2)

        anim_piece3 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece3 += Animation(duration=3, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece3 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece3 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece3 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece3 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece3 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": .5})
        anim_piece3.start(self.ids.id_piece3)

        anim_piece4 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece4 += Animation(duration=4, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece4 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece4 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece4 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece4 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece4 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 0})
        anim_piece4.start(self.ids.id_piece4)

        anim_piece5 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece5 += Animation(duration=5, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece5 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece5 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece5 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece5 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece5 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": .25, "center_y": .5})
        anim_piece5.start(self.ids.id_piece5)

        anim_piece6 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece6 += Animation(duration=6, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece6 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece6 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece6 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece6 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece6 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": .45, "center_y": .5})
        anim_piece6.start(self.ids.id_piece6)

        anim_piece7 = Animation(duration=2, opacity=0, size=(1, 1), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece7 += Animation(duration=7, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": 1})
        anim_piece7 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 1})
        anim_piece7 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": 1, "center_y": 0})
        anim_piece7 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 0})
        anim_piece7 += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": 0, "center_y": 1})
        anim_piece7 += Animation(duration=.5, opacity=1, size=(40, 40), pos_hint={"center_x": .65, "center_y": .5})
        anim_piece7.start(self.ids.id_piece7)

        anim_label_O = Animation(duration= 4, opacity=0)
        anim_label_O += Animation(duration=4, opacity=1)
        anim_label_O.start(self.ids.idlabel_O)

        anim_label_c = Animation(duration=8, opacity=0)
        anim_label_c += Animation(duration=8, opacity=1)
        anim_label_c.start(self.ids.idlabel_c)

        anim_label_t = Animation( opacity=0)
        anim_label_t += Animation(duration=12, opacity=1)
        anim_label_t.start(self.ids.idlabel_t)


    def call_windows_creation_account(self):
        print("activation de la fenetre des comptes...")





    def create_account(self):
        self.push_sound_effect_click()
        toast("creation de compte")
        self.ids.id_screen_account.opacity = 1



    def close_account_screen(self):
        self.push_sound_effect_click()
        self.ids.id_screen_account.opacity = 0
        self.ids.id_screen_account.active = False
        self.ids.id_screen_account.pos = (-1000, -1000)



    def registred_account_data(self):
        pass



    def load_image_avatar(self):
        self.file_manager_avatar.show('/')
        self.file_manager_avatar.show_hidden_files = True
        self.manager_open = True



    def select_path(self, path):
        toast("Chargement des medias...")
        try:
            self.exit_manager()
            toast(path)
            self.save_data_account(path)

        except Exception as E:
            toast(str(E))



    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager_avatar.close()





    def get_info_account(self):
        self.push_sound_effect_click()
        self.ids.id_info_account_screen.opacity = 1




    def close_info_account_screen(self):
        self.push_sound_effect_click()
        self.ids.id_info_account_screen.opacity = 0
        self.ids.id_info_account_screen.active = False
        self.ids.id_info_account_screen.pos = (-1000, -1000)








    def save_data_account(self, p):
        self.push_sound_effect_click()
        pattern_space = re.compile("\s+")
        if pattern_space.match(self.ids.id_textfield_account.text) or self.ids.id_textfield_account.text == "":
            snackbar_error = Snackbar(
                text="[color=#ddbb34]Veuillez remplir les champs d'identification!!![/color]",
                snackbar_y="10dp",
                snackbar_x="100dp",
            )
            snackbar_error.size_hint_x = (

                                                 Window.width - (snackbar_error.snackbar_x * 2)
                                         ) / Window.width

            snackbar_error.buttons = [
                MDIconButton(
                    icon="alert",
                    theme_text_color="Custom",
                    text_color=(1, 201 / 255, 14 / 255, .8),
                    on_release=snackbar_error.dismiss,
                ),
            ]
            snackbar_error.open()

        elif not pattern_space.match(self.ids.id_textfield_account.text):
            obj_db = MyGamePlayer()
            obj_db.insert_database(self.ids.id_textfield_account.text, p, str(datetime.today()))


            self.get_info_account_db(p)
            with open("../project_game_squid_game/database/info data base.txt", "w") as f_db:
                f_db.write(f"-----creation new compte: {self.ids.id_textfield_account.text}--------{str(datetime.now())}\n")
            snackbar_error = Snackbar(
                text="[color=#ffffff]Validation du processus!!![/color]",
                snackbar_y="10dp",
                snackbar_x="100dp",
            )
            snackbar_error.size_hint_x = (

                                                 Window.width - (snackbar_error.snackbar_x * 2)
                                         ) / Window.width

            snackbar_error.buttons = [
                MDIconButton(
                    icon="bookmark-check",
                    theme_text_color="Custom",
                    text_color=(34 / 255, 177 / 255, 76 / 255, .9),
                    on_release=snackbar_error.dismiss,
                ),
            ]
            snackbar_error.open()


        else:
            toast("non Validation du processus, Veuillez reprendre...")



    def get_info_account_db(self, p):
        self.push_sound_effect_click()
        obj_db = MyGamePlayer()
        l = obj_db.get_account_data()
        list_row = []
        list_row1 = []
        list_row2 = []

        for row in l:
            list_row.append(row[1])
            list_row1.append(row[2])
            list_row2.append(row[3])
            if (self.ids.id_textfield_account.text in list_row[:]) and (p in list_row1[:]):
                self.ids.id_get_name_account_db.text = self.ids.id_textfield_account.text
                self.ids.id_date_creation_date.text = str(datetime.today())
                self.ids.id_image_avatar.source = p
                self.ids.id_button_push_game_1.opacity = 1
                self.ids.id_button_push_game_1.active = True
                self.ids.id_button_push_game_1.pos_hint = {"center_x": .45, "center_y": .15}
                self.ids.id_button_push_game_1.md_bg_color == (4/255, 216/255, 157/255, .5)





            else:
                toast("erreur lors du traitement de la procédure...")
                self.get_eror_push_game()
                self.ids.id_button_push_game_1.active = False
                self.ids.id_button_push_game_1.opacity = 0




    def start_game_lvl_1(self):
        obj_start_game = MyGameStart()
        self.push_sound_effect_click_2()
        toast("lancement du niveau 1...")

        obj_start_game.start_level()






    def get_eror_push_game(self):
        toast("Veuillez d'abord creer un compte avant de lancer la partie")



    def start_game_lvl_2(self):
        toast("Debut de la partie 2")


    def start_game_lvl_3(self):
        toast("Debut de la partie 3")


    def remove_account(self):
        self.push_sound_effect_click_2()
        self.ids.screen_drop_account.opacity = 1


    def close_drop_account_screen(self):
        self.push_sound_effect_click()
        self.ids.screen_drop_account.opacity = 0
        self.ids.screen_drop_account.active = False
        self.ids.screen_drop_account.pos = (-1000, -1000)
        self.ids.id_valide_drop_operation.text_color = (1, 0, 0, 1)


    def delete_account(self):
        self.push_sound_effect_click_2()
        pattern_space = re.compile("\s+")
        if pattern_space.match(self.ids.id_account_to_drop.text) or self.ids.id_account_to_drop.text == "":
            toast("Veuillez mentionner un nom valide...")

        elif not pattern_space.match(self.ids.id_account_to_drop.text):
            self.ids.id_valide_drop_operation.text_color = (0, 1, 1, 1)
            obj_db = MyGamePlayer()
            list_ = []
            list_account = obj_db.get_account_data()
            for row in list_account:
                list_.append(row[1])
                if self.ids.id_account_to_drop.text in list_[:]:
                    obj_db.drop_account_data(self.ids.id_account_to_drop.text, "")
                    self.ids.id_get_name_account_db.text = ""
                    self.ids.id_date_creation_date.text = ""
                    self.ids.id_image_avatar.source = ""


                else:
                    toast("Aucune correspondance identifiéé...")

        else:
            toast("Erreur lors du traitement de la procédure...")



    def call_theme(self):
        self.push_sound_effect_click_2()
        t = MDThemePicker()
        t.open()





    def call_about(self):
        self.push_sound_effect_click_2()
        b = MDGridBottomSheet()

        for item in self.data_about.items():
            b.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_item(y),
                icon_src=item[1],
            )
        b.open()




    def callback_for_menu_item(self, item):

        t_info1 = """Démo jeu du 1 2 3 4 soleil du Squid Game.




                    Version: Beta\n
                    contact: Daryl21emani07@gmail.com

                    """
        t_infos2 = "              A propos"

        if item == "code source":
            self.get_url_github()


        elif item == "infos":
            if not self.dialog:
                self.dialog = MDDialog(
                    title=t_infos2,
                    text=t_info1,
                    buttons=[
                        MDIconButton(
                            icon="information",
                            theme_text_color="Custom",
                            text_color=(1, 0, 0, .8),
                            user_font_size="90sp",
                            pos_hint={"center_x": .5, "center_y": .5}
                        ),
                        MDFlatButton(
                            text="                ",

                        ),
                    ],
                   )

            self.dialog.open()



    def get_url_github(self):
        self.push_sound_effect_click()
        path_1 = "https://github.com/ZenDkakukaio/Squid-Game-Demo-detection-pause"
        webbrowser.open_new(path_1)



    def call_instruction_1(self):
        self.ids.screen_call_instruction_1.opacity = 1
        self.ids.screen_call_instruction_1.pos_hint = {"center_x": .5, "center_y": .7}


    def close_screen_instruction_1(self):
        self.ids.screen_call_instruction_1.opacity = 0
        self.ids.screen_call_instruction_1.pos_hint = {"center_x": -100, "center_y": -100}






    def call_instruction_2(self):
        self.ids.screen_call_instruction_2.opacity = 1
        self.ids.screen_call_instruction_2.pos_hint = {"center_x": .5, "center_y": .7}




    def close_screen_instruction_2(self):
        self.ids.screen_call_instruction_2.opacity = 0
        self.ids.screen_call_instruction_2.pos_hint = {"center_x": -100, "center_y": -100}



    def call_instruction_3(self):
        self.ids.screen_call_instruction_3.opacity = 1
        self.ids.screen_call_instruction_3.pos_hint = {"center_x": .5, "center_y": .7}


    def close_screen_instruction_3(self):
        self.ids.screen_call_instruction_3.opacity = 0
        self.ids.screen_call_instruction_3.pos_hint = {"center_x": -100, "center_y": -100}


class MyFirstProgressBar(MDSpinner):
    pass




class Windows_(MDScreen):
    pass