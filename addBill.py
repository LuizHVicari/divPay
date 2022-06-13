#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from datetime import datetime
from operator import ge
import kivy
kivy.require('1.8.0')
 
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker

from kivymd.uix.list import ThreeLineListItem



class Gerenciador(ScreenManager):
    pass
 
class AddConta(Screen):
    inputNomeBill = StringProperty()
    inputDateBill = ObjectProperty()
    ListaMembros = ListProperty()
    listaValores= ObjectProperty()
    valorInicial= StringProperty()


    def on_start(self):
        Membros = [("Membro 1", "Part 1", "Valor 1"), ("Membro 2", "Part 2", "Valor 2"), ("Membro 3", "Part 3", "Valor 3"), ("Membro 4", "Part 4", "Valor 4")]

        print("aaaaaaaaaaaaaaaaa\naaaaaaaaaaa\n")
        for membro in Membros:
            self.root.ids.container.add_widget( ThreeLineListItem( text=f"{Membros[membro][0]}",on_release= lambda x:print("click"), secondary_text=f"{Membros[membro][1]}", tertiary_text=f"{Membros[membro][2]}"))
        
 
    def __init__(self, **kwargs):
        super(AddConta, self).__init__(**kwargs)
        self.inputNomeBill = datetime.today().strftime('%d de %B')
        self.inputDateBill = datetime.today().strftime('%Y-%m-%d')
        
        self.listaValores= ["Opção A", "Opção B", "Opção C", "Opção D"]
        self.valorInicial= datetime.today().strftime('%d of %B')
        
        





    def atualiza_spinner(self):
        self.listaValores= ["Opção W", "Opção X", "Opção Y", "Opção Z"]
        self.valorInicial= "Opção W"
 
    def print_txt(self):
        print(self.inputNomeBill)
        print(self.inputDateBill)



# DatePicker
    def on_save(self, instance, value, date_range):
        self.inputDateBill = value
        #print(instance, value, date_range)
        #print(value.day)
        #print(value.month)
        #print(value.year)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()




class MeuProgramaApp(MDApp):
    def build(self):



        return Gerenciador()


    





 
if __name__ == '__main__':
    Window.size = (360, 640)
    MeuProgramaApp().run()