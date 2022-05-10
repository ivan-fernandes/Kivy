from tempfile import mkdtemp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
#from kivymd.uix.textinput import MDTextInput
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

login = {"ivan": "123456", "admin": 'password'}

Window.size = (450, 550)

kv = """
Screen:
    in_class: 'text'
    MDLabel:
        text: 'Autenticação'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y': 0.9}
    MDIcon:
        icon: 'account-circle'
        icon_color: (0, 0, 0, 1)
        pos_hint: {'center_y': 0.65}
        halign: 'center'
        font_size: 180
    MDTextFieldRound:
        id: usuario
        hint_text: 'Usuario'
        helper_text: 'Digite seu usuario'
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        icon_left: "account-check"
        size_hint_x: None
        width: 300
        required: True
    MDTextFieldRound:
        id: password
        hint_text: 'Digite sua senha'
        helper_text: 'Esqueceu sua senha?'
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        icon_left: "key-variant"
        size_hint_x: None
        width: 300
        password: True
        required: True
    MDRectangleFlatButton:
        text: 'Log in'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            app.auth()

    MDLabel:
        id: show
        text: ''
        pos_hint: {'center_y': 0.1}
        halign: 'center'


    MDFloatingActionButtonSpeedDial:
        data: app.speeddial
        rotation_root_button: True
    """

class Auth(MDApp):
    in_class = ObjectProperty(None)
    dialog = None

    speeddial = {
    'language-python': 'Python',
    'language-php': 'PHP',
    'language-cpp': 'C++',
    }

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "500"
        return Builder.load_string(kv)

    def auth(self):
        lower_keys = {k.lower(): v for k, v in login.items()}
        if self.root.ids.usuario.text.lower() in lower_keys.keys() and self.root.ids.password.text == lower_keys[self.root.ids.usuario.text.lower()]:
    #        if not self.dialog: # use this when login is made only once, otherwise it will keep the wrong username in the dialog
                #create dialog
            self.dialog = MDDialog(
                title="Log in",
                text = f"Bem-vindo {self.root.ids.usuario.text.capitalize()}!",
                buttons = [MDFlatButton(text="OK",
                                        text_color=self.theme_cls.primary_color,
                                        on_release=self.close_dialog),],)
            self.dialog.open()
            label = self.root.ids.show
            label.color = (0.2, 0.2, 1, 1)
            label.text = "Usuario autenticado"
        else:
            label = self.root.ids.show
            label.color = (1, 0.2, 0.2, 1)
            label.text = "Senha incorreta. Tente novamente"

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def on_start(self):
        self.root.ids.usuario.text = "Usuario"
        self.root.ids.password.text = "XXXXXX"
        self.root.ids.show.text = ""

Auth().run()
