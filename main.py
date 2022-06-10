from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.metrics import dp

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
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
class inputAdd(Screen):
    pass



###############################################################################

# APP
class TestApp(MDApp):
    def build(self):
        return Builder.load_file('screens/screenManager.kv')




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

    #Table of Members

    def show_tabela(self):
        print("aaaaa")
        layout = MDFloatLayout()  # root layout
        # Creating control buttons.
        button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )

        for button_text in ["Add row", "Remove row"]:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )

        # Create a table.
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(40)),
                ("Column 2", dp(40)),
                ("Column 3", dp(40)),
            ],
            row_data=[("1", "1", "2", "3")],
        )
        # Adding a table and buttons to the toot layout.
        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)
        

        return layout

    def on_button_press(self, instance_button: MDRaisedButton) -> None:
        '''Called when a control button is clicked.'''

        try:
            {
                "Add row": self.add_row,
                "Remove row": self.remove_row,
            }[instance_button.text]()
        except KeyError:
            pass

    def add_row(self) -> None:
        last_num_row = int(self.data_tables.row_data[-1][0])
        self.data_tables.add_row((str(last_num_row + 1), "1", "2", "3"))

    def remove_row(self) -> None:
        if len(self.data_tables.row_data) > 1:
            self.data_tables.remove_row(self.data_tables.row_data[-1])


###############################################################################



if __name__ == '__main__':
    TestApp().run()