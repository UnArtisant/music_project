from src.Service.ActionService import actionService
from src.Service.MusicService import musicService

class interfaceService() :

    def __init__(self) :
        self.action = actionService()
        self.music = musicService()
    
    def interface(self) :
        action = self.music.isValid([1,2,3], "Rentrer l'action à effectuer : \n 1) Jouer une partition \n 2) Ecrire une partition \n 3) Modifier une partition \n")

        if action == 1 :
            self.play()
        if action == 2 :
            self.write()
        if action == 3 :
            self.update()    

    def update(self):
        print("update")


    def write(self):
        action = self.music.isValid([1,2],"Rentrer l'action à effectuer : \n 1)Ecrire et jouer la musique\n 2) Ecrire dans la base de donnée")
        if action == 1:
            pass
        elif action == 2:
            self.music.upload()
    

    '''Retourne numéro de la partition'''

    def play(self) :
        partionData = self.action.getPartitionData()
        partition = self.music.getPlayedMusic(partionData)
        self.action.playMusic(partition)

