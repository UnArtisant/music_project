"""
L'harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Fichier main
"""
from src.Service.InterfaceService import interfaceService

if __name__ == "__main__":
    interface = interfaceService("partitions.txt")
    interface.interface()
