from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
#from kivymd.uix.screen import Screen 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDRaisedButton,MDRoundFlatButton, MDFillRoundFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem, OneLineAvatarListItem, TwoLineIconListItem
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivy.clock import Clock

global stored_data

stored_data = JsonStore('profile.json')
rate_data = JsonStore('rate_data.json')

welcome = """
#:import partial functools.partial
#:import OneLineListItem kivymd.uix.list.OneLineListItem

MyLayout:
    scr_mngr: scr_mngr
    orientation: 'vertical'
    NavigationLayout:
        
        ScreenManager:
            id: scr_mngr
            homescreen: homescreen

            Screen:
                id: homescreen
                name: 'homescreen'
                BoxLayout:
                    orientation: 'vertical'
        
                    MDToolbar:
                        type: "top"
                        title: "Workout Tool"
                        md_bg_color: app.theme_cls.primary_color
                        background_palette: 'DeepPurple'
                        background_hue: 'A400'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open") ]]
                        elevation: 5
        
                    Widget:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.8
                    adaptive_width: True
                    spacing: "30dp"
            
                    
                    MDFillRoundFlatButton:
                        md_bg_color: app.theme_cls.primary_color
                        text: "Go to workouts"
                        custom_color: 1, 1, 1, 1
                        on_press: root.scr_mngr.current = 'workscreen'
                        pos_hint: {"center_x": 0.5}
    
                    ScrollView:
                        pos_hint: {"center_x": .80}
            
                        DrawerList:
                            spacing: "50dp"
            
                            MDCard:
            
                                focus_behavior: True
                                orientation: "vertical"
                                valign: 'top'
            
                                padding: "8dp"
                                size_hint: None, None
                                size: "340dp", "200dp"
                                on_press: root.scr_mngr.current = 'workscreen'
            
                                adaptive_width: True
                        
                                MDLabel:
                                    text: "<WORKOUT STATS GOES HERE>"
                                    font_style: "H6"
                                    halign: 'center'
            
                                    theme_text_color: "Secondary"
                                    size_hint_y: 1
                                    height: self.texture_size[1]
                                    valign: 'top'
                                    markup: True


                        
            Screen:
                id: 'workscreen'
                name: 'workscreen'
    
                BoxLayout:
                    orientation: 'vertical'
        
                    MDToolbar:
                        type: "top"
                        title: "Workout Tool"
                        md_bg_color: app.theme_cls.primary_color
                        background_palette: 'DeepPurple'
                        background_hue: 'A400'
                        left_action_items: [['arrow-left', partial(root.change_screen, 'homescreen') ]]
                        elevation: 5
        
                    Widget:
                BoxLayout:
                    orientation: 'vertical'
                    height: "1000dp"
                    pos_hint: {"center_x": .5, "center_y": .35}
                    
                    ScrollView:            
                        DrawerList:
                            MDList:
                                id: weeks
                                padding: 0
                                   
                                on_parent:
                                    for i in range(6): self.add_widget(OneLineListItem(text = f'week {i+1}', on_release = partial(root.change_screen, 'workout')))

            Screen:
                id: 'workout'
                name: 'workout'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '30dp'
            
                    MDToolbar:
                        id: 'toolie'
                        type: "top"
                        title: "Workout Tool"
                        md_bg_color: app.theme_cls.primary_color
                        background_palette: 'DeepPurple'
                        background_hue: 'A400'
                        left_action_items: [['arrow-left', partial(root.change_screen, 'workscreen') ]]
                        elevation: 5


                    MDFillRoundFlatButton:
                        md_bg_color: app.theme_cls.primary_color
                        text: "Rate"
                        custom_color: 1, 1, 1, 1
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}
                        on_press: app.rate(1)
                    
                    ScrollView:
                        DrawerList:
                            MDList:
                                id: 'routine'
                                name: 'routine'
                                padding: 0   
                                

      
                    
        MDNavigationDrawer:
            id: nav_drawer
            
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                MDLabel:
                    text: 'text'
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                   
                ScrollView:
                    DrawerList:
                        id: md_list
                        
                        MDList:
                            
                            OneLineIconListItem:
                                on_release: app.show_info() 
                                text: "Profile"
                            
                                IconLeftWidget:
                                    icon: "face-profile"
                                    
                            OneLineIconListItem:
                                on_release: app.input_data(1) 
                                text: "Update Details"
                            
                                IconLeftWidget:
                                    icon: "update"
                                                                             
                                                        
                            OneLineIconListItem:
                                text: "<PLACEHOLDER>"
                            
                                IconLeftWidget:
                                    icon: "folder-marker"
                                    
                           
                            OneLineIconListItem:
                                text: "<PLACEHOLDER>"
                            
                                IconLeftWidget:
                                    icon: "folder-marker"
<Workout> 
    id: 'workout'
    BoxLayout:
        orientation: 'vertical'
        spacing: '30dp'

        MDToolbar:
            id: 'toolie'
            type: "top"
            title: "Workout Tool"
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'DeepPurple'
            background_hue: 'A400'
            left_action_items: [['arrow-left', partial(root.change_screen, 'workscreen') ]]
            elevation: 5


        MDFillRoundFlatButton:
            md_bg_color: app.theme_cls.primary_color
            text: "Rate"
            custom_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            on_press: app.rate(1)
        
        ScrollView:
            DrawerList:
                MDList:
                    id: 'routine'
                    padding: 0                 
               
<Content>
    orientation: "vertical"
    spacing: "7dp"
    size_hint_y: None
    height: "260dp"
    
    MDTextField:
        hint_text: "Enter a username"
        id: user
        required: True
        helper_text: "Enter text"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 300

    MDTextField:
        hint_text: "Enter age"
        id: age
        required: True
        helper_text: "Enter a value"
        helper_text_mode: "on_error"
        input_filter: 'float'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 300
    
    MDTextField:
        hint_text: "Enter weight (kg)"
        id: weight
        required: True
        helper_text: "Enter a value"
        helper_text_mode: "on_error"
        input_filter: 'float'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 300
    
    MDTextField:
        hint_text: "Enter height (cm)"
        id: height
        required: True
        helper_text: "Enter a value"
        helper_text_mode: "on_error"
        input_filter: 'float'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 300

<Rate>
    orientation: "vertical"
    spacing: "7dp"
    size_hint_y: None
    height: "200dp"
    
    MDTextField:
        hint_text: "Enter total number of reps"
        id: rate_reps
        required: True
        helper_text: "Enter a value"
        helper_text_mode: "on_error"
        input_filter: 'float'
        pos_hint: {'center_x': 0.45, 'center_y': 0.8}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 280
    
    MDTextField:
        hint_text: "Enter total weight"
        id: rate_weight
        required: True
        helper_text: "Enter a value"
        helper_text_mode: "on_error"
        input_filter: 'float'
        pos_hint: {'center_x': 0.45, 'center_y': 0.8}
        icon_right: 'keyboard-return'
        icon_right_color: app.theme_cls.primary_color
        size_hint_x: None
        width: 280
    
    MDLabel:
        text: "Please rate the intensity of the exercise"
        theme_text_color: "Secondary"

    MDSlider:
        id: rate_intensity
        min: 0
        max: 10
        hint: True
        on_value: rate_intensity.text = str(int(self.value))



"""


class MyLayout(BoxLayout):
    scr_mngr = ObjectProperty(None)
            


    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

   
    def on_enter(self, *args):
        """Event fired when the screen is displayed: the entering animation is
        complete."""


        #def on_enter(self,interval):
        


        #Clock.schedule_once(self.on_enter)


class Content(BoxLayout):
    pass

class Workout(Screen):

    pass

sm = ScreenManager()
sm.add_widget(Workout(name='workout'))

class Panels(BoxLayout):
    pass

class Rate(BoxLayout):
    pass

class Item(OneLineAvatarListItem):
    source = StringProperty()

class DemoApp(MDApp):
    stored_data = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)
        self.store = JsonStore("bco.json")
        
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass
    
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        #self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        self.screen = Builder.load_string(welcome)
        
        return self.screen

    def rout(self):
        self.ids.workout.ids.routine.add_widget(MDList(text = 'hi'))
        
    def input_data(self,obj):
        
        self.input_dialog = MDDialog(
            title="Input Personal Details:",
            type="custom",
            content_cls=Content(),size_hint = (0.7,1),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                ),
                MDFlatButton(
                    text="NEXT", text_color=self.theme_cls.primary_color, on_release =self.show_data
                ),
            ],
        )
        self.input_dialog.open()
    
    def rate(self,obj):
        
        self.rate_dialog = MDDialog(
            title="[color=ffffff]Week 1, Day 1, Set 1[/color]",
            type="custom",
            content_cls=Rate(),size_hint = (0.45,1),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_rate_dialog
                ),
                MDFlatButton(
                    text="SAVE", text_color=self.theme_cls.primary_color, on_release =self.rate_logic
                ),
            ],
        )
        self.rate_dialog.open()
    
    #Saved information logic
    def saved_info(self, obj):
        #if self.input_dialog.content_cls.ids.user.text != "":
        self.summary_dialog.dismiss()
        self.input_dialog.dismiss()
        self.a = self.input_dialog.content_cls.ids.user.text
        self.b = self.input_dialog.content_cls.ids.age.text
        self.c = self.input_dialog.content_cls.ids.weight.text
        self.d = self.input_dialog.content_cls.ids.height.text
        stored_data.put('user', user=self.a)
        stored_data.put('age', age=self.b)
        stored_data.put('weight', weight=self.c)
        stored_data.put('height', height=self.d)
    
    def rate_logic(self,obj):
        if self.rate_dialog.content_cls.ids.rate_reps.text == "":
            ratereps_chk = 'Please enter a a value'
            self.ratereps_dialog = MDDialog(title = 'Error', text = ratereps_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_ratereps_dialog)])
            self.ratereps_dialog.open()
            
        elif float(self.rate_dialog.content_cls.ids.rate_reps.text) < 0:
            ratereps_chk = 'Please enter a valid rep value'
            self.ratereps_dialog = MDDialog(title = 'Error', text = ratereps_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_ratereps_dialog)])
            self.ratereps_dialog.open()
        
        elif self.rate_dialog.content_cls.ids.rate_weight.text == "":
            rateweight_chk = 'Please enter a valid weight value'
            self.rateweight_dialog = MDDialog(title = 'Error', text = rateweight_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_rateweight_dialog)])
            self.rateweight_dialog.open()
            
        elif float(self.rate_dialog.content_cls.ids.rate_weight.text) < 0:
            rateweight_chk = 'Please enter a valid weight value'
            self.rateweight_dialog = MDDialog(title = 'Error', text = rateweight_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_rateweight_dialog)])
            self.rateweight_dialog.open()
        
        else:
            self.rate_dialog.dismiss()
            self.w1d1s1_reps = self.rate_dialog.content_cls.ids.rate_reps.text
            self.w1d1s1_weight = self.rate_dialog.content_cls.ids.rate_weight.text
            self.w1d1s1_rpe = self.rate_dialog.content_cls.ids.rate_intensity.text
            rate_data.put('rated_reps', rated_reps=self.w1d1s1_reps)
            rate_data.put('rated_weight', rated_weight=self.w1d1s1_weight)
            rate_data.put('rated_intensity', rated_intensity=self.w1d1s1_rpe)          


    def show_data(self, obj):

        if self.input_dialog.content_cls.ids.user.text == "":
            user_chk = 'Please enter a username'
            self.user_dialog = MDDialog(title = 'Error', text = user_chk, 
                                         size_hint = (0.7,1),
                                         buttons = [MDFlatButton(text = 'Close', on_release = self.close_user_dialog)])
            self.user_dialog.open()
        
        elif self.input_dialog.content_cls.ids.age.text == "":
            age_chk = 'Please enter a value'
            self.age_dialog = MDDialog(title = 'Error', text = age_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_age_dialog)])
            self.age_dialog.open()
        
        elif float(self.input_dialog.content_cls.ids.age.text) > 100:
            age_chk = 'Please enter a valid age value'
            self.age_dialog = MDDialog(title = 'Error', text = age_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_age_dialog)])
            self.age_dialog.open()
        
        elif float(self.input_dialog.content_cls.ids.age.text) < 0:
            age_chk = 'Please enter a valid age value'
            self.age_dialog = MDDialog(title = 'Error', text = age_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_age_dialog)])
            self.age_dialog.open()
            
        elif self.input_dialog.content_cls.ids.height.text == "":
            height_chk = 'Please enter a value'
            self.height_dialog = MDDialog(title = 'Error', text = height_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_height_dialog)])
            self.height_dialog.open()
        
        elif float(self.input_dialog.content_cls.ids.height.text) > 250:
            height_chk = 'Please enter a valid height value'
            self.height_dialog = MDDialog(title = 'Error', text = height_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_height_dialog)])
            self.height_dialog.open()
        
        elif float(self.input_dialog.content_cls.ids.height.text) < 140:
            height_chk = 'Please enter a valid height value'
            self.height_dialog = MDDialog(title = 'Error', text = height_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_height_dialog)])
            self.height_dialog.open()

        elif self.input_dialog.content_cls.ids.weight.text == "":
            weight_chk = 'Please enter a value'
            self.weight_dialog = MDDialog(title = 'Error', text = weight_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_weight_dialog)])
            self.weight_dialog.open()
        
       
        elif float(self.input_dialog.content_cls.ids.weight.text) > 300:
            weight_chk = 'Please enter a valid weight value'
            self.weight_dialog = MDDialog(title = 'Error', text = weight_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_weight_dialog)])
            self.weight_dialog.open()

        elif float(self.input_dialog.content_cls.ids.weight.text) < 35:
            weight_chk = 'Please enter a valid weight value'
            self.weight_dialog = MDDialog(title = 'Error', text = weight_chk, 
                               size_hint = (0.7,1),
                               buttons = [MDFlatButton(text = 'Close', on_release = self.close_weight_dialog)])
            self.weight_dialog.open()
                
        else:
            self.summary_dialog = MDDialog(title="Review your personal details",type="simple", 
                                   items=[Item(text = 'You can change them later'),
                                       Item(text="username: " + self.input_dialog.content_cls.ids.user.text), 
                                       Item(text="age: " + self.input_dialog.content_cls.ids.age.text),    
                                       Item(text="weight: " + self.input_dialog.content_cls.ids.weight.text + "kg"),    
                                       Item(text="height: " + self.input_dialog.content_cls.ids.height.text + "cm"),                                                                                                             
                                       ],size_hint = (0.7,1),
                                        buttons = [MDFlatButton(text = 'SAVE', on_release = self.saved_info)])        
            self.summary_dialog.open() 
            
    def close_dialog(self, obj):
        #self.dialog.dismiss()
        self.input_dialog.dismiss()

    def close_user_dialog(self, obj):
        #self.dialog.dismiss()
        self.user_dialog.dismiss()
    
    def close_height_dialog(self, obj):
        self.height_dialog.dismiss()

    def close_weight_dialog(self, obj):
        self.weight_dialog.dismiss()

    def close_age_dialog(self, obj):
        self.age_dialog.dismiss()

    def close_rate_dialog(self,obj):
        self.rate_dialog.dismiss()
    
    def close_ratereps_dialog(self,obj):
        self.ratereps_dialog.dismiss()

    def close_rateweight_dialog(self,obj):
        self.rateweight_dialog.dismiss()
    
    def close_personal_error_dialog(self,obj):
        self.personal_error_dialog.dismiss()

    def show_info(self):
        if not stored_data:
                self.personal_error_dialog = MDDialog(title="[color=ffffff]Error[/color]",
                                            text = "No details recorded. Please provide your personal details.",size_hint = (0.7,1),
                                            buttons = [MDFlatButton(text = 'CLOSE', on_release = self.close_personal_error_dialog), MDFlatButton(text = 'UPDATE', on_release = self.input_data)])
                self.personal_error_dialog.open()
            
        else:
            self.show_dialog = MDDialog(title="[color=ffffff]Here are your personal details[/color]",type="simple", 
                           items=[Item(text="username: " + stored_data.get('user')['user']), 
                               Item(text="age: " + stored_data.get('age')['age']),    
                               Item(text="weight: " + stored_data.get('weight')['weight'] + "kg"),    
                               Item(text="height: " + stored_data.get('height')['height'] + "cm"),                                                                                                             
                               ],size_hint = (0.7,1),
                                buttons = [MDFlatButton(text = 'CLOSE', on_release = self.close_showdialog), MDFlatButton(text = 'UPDATE', on_release = self.input_data)])
            self.show_dialog.open()

        
    def close_showdialog (self,obj):
        self.show_dialog.dismiss()
    

                                    



    
    def chest_press(self,obj):
        
            self.dialog = MDDialog(title = "[color=ffffff]<Chest press description goes here>[/color]",
                    text="The quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogs>",
                            
                )
            self.dialog.open()
    
    def bicep_curl(self,obj):
        
            self.dialog = MDDialog(title = "[color=ffffff]<Bicep curl description goes here>[/color]",
                    text="The quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogs>",
                            
                )
            self.dialog.open()

    def arm_raises(self,obj):
        
            self.dialog = MDDialog(title = "[color=ffffff]<arm_raises description goes here>[/color]",
                    text="The quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogsThe quick brown fox jumped over the lazy dogs>",
                            
                )
            self.dialog.open()
    

        

               

DemoApp().run()
