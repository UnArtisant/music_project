from src.Service.ActionService import actionService

class interfaceService() :

    def __init__(self) :
        self.action = actionService()
    
    def initInterface(self) :
        action = int(input("Rentrer l'action à effectuer : \n 1) jouer une partition \n 2) écrire une partition \n 3) modifier une partition \n"))
        if(action == 1) :
            self.action.message()
            self.update()

    def update(self):
        print("update")   

    def add(self) :
        print("add")
    
    def play(self) :
        print("play")