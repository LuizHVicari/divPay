from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.metrics import dp

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDDatePicker

Window.size = (360, 640)


###############################################################################
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

#Builder.load_file('components/helpers.kv')


###############################################################################

# ScreenManager
class MyScreenManager(ScreenManager):
    pass

###############################################################################

# Declare both screens
class SplashScreen(Screen):
    pass

class MenuScreen(Screen):
    primary_color = [ 141/255, 141/255, 141/255, 1]

    def toAddBill(self):
        self.manager.current = 'add'


    pass

class AddScreen(Screen):
    pass

class AddBillScreen(Screen):
    pass
class AddMemberScreen(Screen):
    
    pass

###############################################################################

# utils
class Bill(BoxLayout):
    name_bill = ObjectProperty(None)
    date_bill = ObjectProperty(None)
    member_list = ObjectProperty(None)

    def submit_bill(self):
        pass

    def delete_bill(self):
        pass

    def edit_bill(self):
        pass



    pass



###############################################################################

# APP
class TestApp(MDApp):



    #Build the app
    def build(self):
        print("aaaaa")
        ScreenManager = Builder.load_file('screens/screenManager.kv')



        return ScreenManager



    def show_table_menu(self) -> None:
        '''Called when a table is clicked.'''

        
        layout = MDFloatLayout()  # root layout
        # Creating control buttons.
        button_box = MDBoxLayout(
            pos_hint={"center_y": 0.3, "center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )


        button_box.add_widget(
            MDRaisedButton(
                text="Adicionar"#, on_release=self.
            )
        )
        button_box.add_widget(
            MDRaisedButton(
                text="Remover"#, on_release=self.
            )
        )


        # Create a table.
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.7, "center_x": 0.5},
            size_hint=(0.9, 0.7),
            use_pagination=False,
            column_data=[
                ("Membro", dp(30)),
                ("Participação", dp(20)),
                ("Contribuição", dp(20)),
            ],
            row_data=[("1", "1", "2"), ("2", "2", "3"), ("3", "3", "4")],
        )



        # Adding a table and buttons to the toot layout.
        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)

        return layout







###############################################################################
    #date picker

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        print(instance, value, date_range)
        print(value.day)
        print(value.month)
        print(value.year)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()



###############################################################################
    #Table of Members






###############################################################################



if __name__ == '__main__':
    TestApp().run()