from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size = (350, 600)

KV = """
ScreenManager:
    SplashScreen:
    LoginScreen:
    RegisterScreen:
    ForgetPasswordScreen:


<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
        md_bg_color: 188/255, 227/255, 217/255, 1
        MDIconButton:
            icon: "chevron-right"
            user_font_size: "35sp"
            pos_hint: {"center_x": .5, "center_y": .12}
            on_press: app.root.current = 'login'


        MDLabel:
            text: "Welcome To Insurance App"
            pos_hint: {"center_x": .5, "center_y": .45}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0
            font_size:"35sp"

        MDLabel:
            text: "Get Started"
            pos_hint: {"center_x": .5, "center_y": .18}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0
            font_size:"13sp"

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 188/255, 227/255, 217/255, 1
        MDLabel:
            text: "WelCome"
            font_size: "28sp"
            pos_hint: {"center_x": .6, "center_y": .73}

        MDLabel:
            text: "Login in"
            font_size: "20sp"
            color: 120/255, 120/255, 120/255, 1
            pos_hint: {"center_x": .6, "center_y": .66}

        MDLabel:
            text: " "
            halign:"center"
            font_size: "14.5sp"
            pos_hint: {"center_x": .5, "center_y": .055}
            id: login

        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .55}
            MDLabel:
                text:"Username"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": .9}
            TextInput:
                id: username
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": .4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                foreground_color: 120/255, 120/255, 120/255, 1
                font_size: "17sp"
                multiline: False
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 0}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1


        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .4}
            MDLabel:
                text:"Password"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": .9}
            TextInput:
                id: password
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": .4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                font_size: "17sp"
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 0}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1

        Button:
            text: "Login"
            background_color: 0, 0, 0, 0
            size_hint: .79, .065
            pos_hint: {"center_x": .5, "center_y": .27}
            on_release:
                root.loga(username.text, password.text)

            canvas.before:
                Color:
                    rgb: 25/255, 38/255, 35/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [2]
        Button:
            text: "Register"
            background_color: 0, 0, 0, 0
            size_hint: .79, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            on_press: app.root.current = 'register'
            canvas.before:
                Color:
                    rgb: 50/255, 66/255, 63/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [2]

        MDTextButton:
            text: "Forget Password"
            font_size: "15sp"
            pos_hint: {"center_x": .5, "center_y": .11}
            halign: "center"
            color: 120/255, 120/255, 120/255, 1
            on_release: app.root.current = 'forget-password'

<RegisterScreen>:
    name: 'register'
    MDFloatLayout:
        md_bg_color: 188/255, 227/255, 217/255, 1
        MDIconButton:
            icon: "chevron-left"
            user_font_size: "35sp"
            pos_hint: {"center_y": .95}
            on_press: app.root.current = 'login'

        MDLabel:
            text: "Back"
            font_size: "18sp"
            pos_hint: {"center_x": .615, "center_y": .949}

        MDLabel:
            text: "Register"
            font_size: "28sp"
            pos_hint: {"center_x": .6, "center_y": .85}

        MDLabel:
            text: " "
            halign:"center"
            font_size: "16sp"
            pos_hint: {"center_x": .5, "center_y": .09}
            id: lbregister

        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Full Name"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": 3.85}
            TextInput:
                id : name
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": 3.4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                foreground_color: 120/255, 120/255, 120/255, 1
                font_size: "17sp"
                multiline: False
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 3}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1


        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .35}
            MDLabel:
                text:"Username"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": 3.3}
            TextInput:
                id: username
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": 2.85}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                font_size: "17sp"
                multiline: False
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 2.55}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1


        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .35}
            MDLabel:
                text:"Password"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": .9}
            TextInput:
                id: password
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": .4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                font_size: "17sp"
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 0}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1

        Button:
            text: "Register"
            background_color: 0, 0, 0, 0
            size_hint: .79, .065
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: root.register(name.text, username.text, password.text)
            canvas.before:
                Color:
                    rgb: 25/255, 38/255, 35/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [2]


<ForgetPasswordScreen>:
    name: 'forget-password'
    MDFloatLayout:
        md_bg_color: 188/255, 227/255, 217/255, 1
        MDIconButton:
            icon: "chevron-left"
            user_font_size: "35sp"
            pos_hint: {"center_y": .95}
            on_press: app.root.current = 'login'

        MDLabel:
            text: "Back"
            font_size: "18sp"
            pos_hint: {"center_x": .615, "center_y": .949}

        MDLabel:
            text: "Forget Password?"
            font_size: "28sp"
            pos_hint: {"center_x": .6, "center_y": .85}

        MDLabel:
            text: " "
            halign:"center"
            font_size: "16sp"
            pos_hint: {"center_x": .5, "center_y": .15}
            id: label

        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Username"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": 3.85}
            TextInput:
                id : username
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": 3.4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                foreground_color: 120/255, 120/255, 120/255, 1
                font_size: "17sp"
                multiline: False
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 3}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1


        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {"center_x": .5, "center_y": .35}
            MDLabel:
                text:"Re-Enter Password"
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": 3.3}
            TextInput:
                id: password
                size_hint_y: .75
                pos_hint: {"center_x": .49, "center_y": 2.85}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "2sp"
                font_size: "17sp"
                multiline: False
            MDFloatLayout:
                pos_hint: {"center_x": .5, "center_y": 2.55}
                size_hint_y: .03
                md_bg_color: 120/255, 120/255, 120/255, 1


        Button:
            text: "Change Password"
            background_color: 0, 0, 0, 0
            size_hint: .79, .065
            pos_hint: {"center_x": .5, "center_y": .35}
            on_release: app.root.current = 'login'#(username.text, password.text)
            canvas.before:
                Color:
                    rgb: 25/255, 38/255, 35/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [2]
"""

class SplashScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class ForgetPasswordScreen(Screen):
    pass


class Main(MDApp):
    def build(self):
        kv = Builder.load_string(KV)
        screen = kv
        return screen


if __name__ == "__main__":
    Main().run()
