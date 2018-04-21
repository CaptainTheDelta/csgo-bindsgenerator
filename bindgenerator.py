#!/usr/bin/env python3
# coding: utf-8

#----------------------------------- import -----------------------------------

import os

import tkinter as tk
import tkinter.messagebox as msgbox

from tkinter.filedialog import askopenfilename,asksaveasfilename

from BindsFrame import *
from fcts import *

#---------------------------------- fenêtre -----------------------------------

def hello():
    print("Hello World !")

class Application:

    def __init__(self,fenetre):
        self.parent = fenetre
        self.parent.title("Binds Generator")
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)
        
        self.menu()
        self.binds_frame = BindsFrame(self.parent)

        self.filepath = ''
        self.binds = []


    def run(self):
        self.parent.mainloop()

    def menu(self):
        self.menubar = tk.Menu(self.parent)

        self.m_fichier = tk.Menu(self.menubar,tearoff=0)
        self.m_fichier.add_command(label="Nouvelle config",command=hello)
        self.m_fichier.add_command(label="Ouvrir",command=self.open_cfg)
        self.m_fichier.add_command(label="Enregistrer",command=self.save_cfg)
        self.m_fichier.add_command(label="Enregistrer sous",command=self.save_cfg_under)
        self.m_fichier.add_separator()
        self.m_fichier.add_command(label="Quitter",command=self.quit)
        self.menubar.add_cascade(label="Fichier",menu=self.m_fichier)

        self.parent.config(menu=self.menubar)

    def open_cfg(self):
        filepath = askopenfilename(title="Ouvrir un fichier de config",
                filetypes=[("Fichier de configuration",".cfg"),("Tous les fichiers",".*")])

        if(filepath != ()):
            self.filepath = filepath
            self.binds = load(filepath)

            self.binds_frame.destroy()
            self.binds_frame = BindsFrame(self.parent,self.binds)

    def save_cfg(self,binds=[]):
        if binds == []:
            binds = self.binds_frame.get_binds()

        if binds == []:
            msgbox.showerror("Erreur","Pas de binds à enregistrer !")
            return

        if self.filepath == '':
            self.save_cfg_under(binds)

        save(binds,self.filepath)
        self.binds = binds

    def save_cfg_under(self,binds=[]):
        if binds == []:
            binds = self.binds_frame.get_binds()

        if binds == []:
            msgbox.showerror("Erreur","Pas de binds à enregistrer !")
            return

        filepath = asksaveasfilename(title="Enregistrer sous",
                filetypes=[("Fichier de configuration",".cfg"),("Tous les fichiers",".*")])

        if(filepath != ()):
            self.filepath = filepath
            self.save_cfg(binds)

    def quit(self):
        binds = self.binds_frame.get_binds()
        if self.binds != binds and msgbox.askyesno('Travail non enregistré', 'Enregistrer ?'):
            self.save_cfg(binds)

        self.parent.quit()











#------------------------------------ main ------------------------------------

root = tk.Tk()
app = Application(root)
app.run()