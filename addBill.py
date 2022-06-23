#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from asyncio.windows_events import NULL
from datetime import datetime
from mailbox import NotEmptyError
from operator import contains, ge
from pydoc import text
from turtle import onclick
from xml.dom.minidom import Childless

import kivy
kivy.require('1.8.0')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout

import uuid

from kivymd.uix.list import ThreeLineListItem


#global contas
#contas = list(Bill('Conta', ''))



Builder.load_file("meuprograma.kv")




class Gerenciador(ScreenManager):
    pass



# class NumMembros(Screen):
#     inputNumeroDeMembros = ObjectProperty()
#     inputNumeroDeMembrosInicial = ObjectProperty()
#     listaValores= ObjectProperty()

    
#     def __init__(self, **kwargs):
#         super(NumMembros, self).__init__(**kwargs)
#         self.inputNumeroDeMembrosInicial = "2"
#         self.listaValores= ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
 

#     def on_inputNumeroDeMembros(self, value):
#         print(value)
#         print("aa")
#         #for i in range( int(value) ):
#         #    AddConta.ids.container.add_widget( ThreeLineListItem( text=f"Membro {i}",on_release= lambda x:print("click"), secondary_text="Peso 10", tertiary_text="R$ 10,00"))


# name : str, members : dict, value : float, day : int, month : int, year : int





class Content(BoxLayout):
    inputNome = ObjectProperty()
    inputPart = ObjectProperty()
    inputContr = ObjectProperty()
    inputNomeIni = StringProperty()
    inputPartIni = StringProperty()
    inputContrIni = StringProperty()

    #def __init__(self, **kwargs):
        #super(Content, self).__init__(**kwargs)
        #self.inputNomeIni = self.nome
        #self.inputPartIni = self.part
        #self.inputContrIni = self.contr


    dialog = None
    def show_confirmation_dialog(self, addscreen):
        if not self.dialog:
            self.dialog = MDDialog(
                title=" ",
                type="custom",
                content_cls= Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=[0, 0, 0, 1],
                        on_release=lambda x: self.dialog.dismiss(),

                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=[0, 0, 0, 1],
                        on_release=lambda x: self.on_click_button(self.dialog.content_cls, addscreen),
                    ),
                ],
            )
        self.dialog.open()

    def on_click_button(self, addscreen):
        
        print(self.inputNome.text)
        print(self.inputPart.text)
        print(self.inputContr.text)
        self.dialog.dismiss()
        AddConta.add_member(addscreen, self.inputNome.text, self.inputPart.text, self.inputContr.text)


    





class AddConta(Screen):
    inputNomeBill = StringProperty()
    inputDateBill = ObjectProperty()
    ListaMembros = ListProperty()
    listaValores= ObjectProperty()
    valorInicial= StringProperty()



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inputNomeBill = datetime.today().strftime('%d de %B')
        self.inputDateBill = datetime.today().strftime('%Y-%m-%d')
        self.listaValores= ["Opção A", "Opção B", "Opção C", "Opção D"]
        self.valorInicial= datetime.today().strftime('%d of %B')
        
        
        
        #self.ids.container.add_widget( ThreeLineListItem( text=f"Membro {i}",on_release= lambda x:print("click"), secondary_text="Peso 10", tertiary_text="R$ 10,00"))



    def print_txt(self, value, **kwargs):
        self.inputNomeBill = value

        listaMembers = list()
        for membro in self.manager.get_screen('addConta').ids.container.children:
            listaMembers.append( (membro.text ,membro.secondary_text ,membro.tertiary_text ) )
        

        print(self.inputNomeBill)
        print(self.inputDateBill)
        print(listaMembers)

        Home.add_conta(self, self.inputNomeBill, self.inputDateBill)



    def show_dialog(self):
        print(self)
        Content.show_confirmation_dialog(Content, self)


    def on_return(self):
        print(1)
        self.manager.get_screen('addConta').ids.container.clear_widgets()



    def add_member(self, Nome='Membro', Part='10', Contrib='10'):
        self.manager.get_screen('addConta').ids.container.add_widget( 
            ThreeLineListItem( 
                #TODO on_release= lambda x: AddConta.show_dialog(self), 
                text= Nome,
                secondary_text= f'{Part}', 
                tertiary_text= f'{Contrib}'))





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

    def add_conta(self, nome, data):
        self.manager.get_screen('home').ids.contas.add_widget( 
                ThreeLineListItem( 
                    #TODO on_release= lambda x: AddConta.show_dialog(self), 
                    text= nome,
                    secondary_text= f'{data}'))
    


class MeuProgramaApp(MDApp):
    def build(self):

        return Gerenciador()



        #for i in range(3):
        #    self.root.get_screen('addConta').ids.container.add_widget( ThreeLineListItem( text=f"Membro {i}",on_release= lambda x:print("click"), secondary_text="Peso 10", tertiary_text="R$ 10,00"))
        #    print(f"1:  {self.root.get_screen('addConta').ids.container.children}")
            
            





 
if __name__ == '__main__':
    Window.size = (360, 640)
    MeuProgramaApp().run()