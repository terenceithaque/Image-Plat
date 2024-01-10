from tkinter import * 

class Application(Tk):
    "Application"
    def __init__(self):
        super().__init__() # On hérite des attributs de la classe Tk
        self.label_recherche = Label(self, text="Saisissez le nom du plat ou de la recette à rechercher :") # Label pour indiquer à l'utilisateur ce qu'il doit entrer
        self.label_recherche.pack()

        self.entree_recherche = Entry(self) # Entrée pour permettre la saisie du nom du plat ou de la recette par l'utilisateur
        self.entree_recherche.pack(fill="x")

        self.bouton_rechercher = Button(self, text="Rechercher le plat / la recette", command = None) # Bouton sur lequel l'utilisateur doit cliquer pour déclencher la recherche
        self.bouton_rechercher.pack(fill="x")


app = Application()
app.mainloop()
