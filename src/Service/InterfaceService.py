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
            self.add()
        if action == 3 :
            self.update()    

    def update(self):
        print("update")

<<<<<<< HEAD
    def write(self):
        """condition : écrire une partition ou écrire et jouer une partition"""

=======
>>>>>>> 44e50c658d5c4924b338277e15c896743ea2cb6c

    def add(self) :
        print("add")
    

    '''Retourne numéro de la partition'''

    def play(self) :
        partionData = self.action.getPartitionData()
        partition = self.music.getPlayedMusic(partionData)
        self.action.playMusic(partition)

