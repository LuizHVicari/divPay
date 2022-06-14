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



class NumMembros(Screen):
    inputNumeroDeMembros = StringProperty()
    inputNumeroDeMembrosInicial = StringProperty()
    listaValores= ObjectProperty()

    
    def __init__(self, **kwargs):
        super(NumMembros, self).__init__(**kwargs)
        self.inputNumeroDeMembrosInicial = "2"
        self.listaValores= ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
 

    def on_inputNumeroDeMembros(self, value):
        for i in range( value ):
            AddConta.ids.container.add_widget( ThreeLineListItem( text=f"Membro {i}",on_release= lambda x:print("click"), secondary_text="Peso 10", tertiary_text="R$ 10,00"))





class AddConta(Screen):
    inputNomeBill = StringProperty()
    inputDateBill = ObjectProperty()
    ListaMembros = ListProperty()
    listaValores= ObjectProperty()
    valorInicial= StringProperty()



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

        


class Home(Screen):

    pass


class MeuProgramaApp(MDApp):
    def build(self):

        return Gerenciador()

    def on_start(self):
        
        print(self.root.get_screen('addConta'))
        print(self.root)
        print(self)
        print(AddConta) 

        for i in range(3):
            self.root.get_screen('addConta').ids.container.add_widget( ThreeLineListItem( text=f"Membro {i}",on_release= lambda x:print("click"), secondary_text="Peso 10", tertiary_text="R$ 10,00"))
            
            
            print(f"1:  {self.root.get_screen('addConta').ids.container.children}")







 
if __name__ == '__main__':
    Window.size = (360, 640)
    MeuProgramaApp().run()