from src.Service.ActionService import actionService
from src.Service.MusicService import musicService

class interfaceService() :

    def __init__(self) :
        self.action = actionService()
        self.music = musicService()
    
    def interface(self) :
        Invalid = True
        valueAccepted = [1,2,3]
        while Invalid :
            action = int(input("Rentrer l'action à effectuer : \n 1) jouer une partition \n 2) écrire une partition \n 3) modifier une partition \n"))
            if(action in valueAccepted) :
                Invalid = False

        if action == 1 :
            self.play()
        if action == 2 :
            self.add()
        if action == 3 :
            self.update()    

    def update(self):
        print("update")

    def add(self) :
        print("add")
    

    '''Retourne numéro de la partition'''
    def play(self):
        self.action.playMusic()

    def play(self) :
        partionData = self.action.getPartitionData()
        partition = self.music.getPlayedMusic(partionData)
        print(partition)
        

