"""
L'harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Fichier main
"""
from src.Service.InterfaceService import interfaceService

if __name__ == "__main__":
    file = input("De quel fichier voulez-vous vous traiter les partitions ?\n ")
    interface = interfaceService(file)
    interface.interface()
