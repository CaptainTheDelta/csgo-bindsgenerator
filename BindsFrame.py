# coding: utf-8

import tkinter as tk
from fcts import *


class BindsFrame:
    # Définition du frame
    def __init__(self,fenêtre,binds=[]):
        """Initialise le frame des binds.

        Args:
            fenêtre (tk): Conteneur tkinter.
            [binds (list)]: Liste de binds à afficher.
        """
        self.f = tk.Frame(fenêtre)

        self.n = 0
        self.keys = []
        self.cmds = []
        
        for b in binds:
            self.bind_widget(*b)
        
        if binds == []:
            self.bind_widget()

        # Boutons en bas
        # Sous-frame, plus simple à placer et à détruire.
        self.boutons = tk.Frame(self.f)
        self.bouton_add = tk.Button(self.boutons, text="Ajouter", command=self.add_bind)
        self.bouton_refresh = tk.Button(self.boutons, text="Rafraîchir", command=self.refresh_bind)

        # On place les boutons dans le sous-frame
        self.bouton_add.grid(row=0,column=1)
        self.bouton_refresh.grid(row=0,column=0)

        self.boutons.grid(row=self.n+1,column=1)
        
        self.f.pack()

    def bind_widget(self,k='',c=''):
        """Ajoute une ligne de bind.

        Args:
            [k (str)]: Touche.
            [c (str)]: Commande.
        """
        # On définit du texte format tk.
        key = tk.StringVar()
        key.set(k)
        cmd = tk.StringVar()
        cmd.set(c)

        # On ajoute les deux cases aux listes.
        self.keys.append(tk.Entry(self.f, textvariable=key))
        self.cmds.append(tk.Entry(self.f, textvariable=cmd))

        # On les places en bas.
        n = self.n
        self.keys[n].grid(row=n+1,column=0)
        self.cmds[n].grid(row=n+1,column=1)

        self.n += 1

    def pack(self): # Étudier la possibilité de faire hériter cette classe de tk.Frame
        self.f.pack()

    def destroy(self): # Étudier la possibilité de faire hériter cette classe de tk.Frame
        self.f.destroy()
    
    # Fonctions "événements"
    def add_bind(self):
        """Ajoute une ligne de bind : supprime les boutons, ajoute la ligne,
        puis remet les boutons.
        """
        self.boutons.grid_forget()
        self.bind_widget()
        self.boutons.grid(row=self.n+1,column=1)

    def refresh_bind(self):
        """Supprime les lignes vides."""
        # On commence par virer les boutons.
        self.boutons.grid_forget()

        # On récupère toutes les lignes où au moins l'une des deux cases n'est
        # pas vide.
        binds = []
        for k,c in zip(self.keys,self.cmds):
            k,c = k.get(),c.get()
            if k != '' or c != '':
                binds.append((k,c))

        # On détruit toutes les lignes, et on les vire des tableaux
        for i in range(self.n-1,-1,-1):
            self.keys[i].destroy()
            self.cmds[i].destroy()
            self.keys.pop()
            self.cmds.pop()

        # On remet les bons binds.
        self.n = 0
        for b in binds:
            self.bind_widget(*b)

        # S'il n'y en avait pas on met au moins une ligne.
        if self.n == 0:
            self.bind_widget()

        self.boutons.grid(row=self.n+1,column=1)

    # Autres fonctions
    def get_binds(self):
        """Renvoie les binds complets disponibles.

        Return:
            (list): Liste des binds.
        """
        binds = []

        for k,c in zip(self.keys,self.cmds):
            k,c = k.get(),c.get()
            if k != '' and c != '':
                binds.append((k,c))

        return binds