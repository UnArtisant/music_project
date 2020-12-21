from src.Service.ActionService import actionService
from src.Service.MusicService import musicService

class interfaceService() :
    def __init__(self) :
        self.action = actionService()
        self.music = musicService()
    
    def interface(self) :
        action = self.music.isValid([1,2,3,4], "Rentrer l'action à effectuer : \n 1) Jouer une partition \n 2) Ecrire une partition \n 3) Modifier une partition \n 4) Créer une partition à partir de celles dans la base de donnée")

        if action == 1 :
            self.play()
        if action == 2 :
            self.write()
        if action == 3 :
            self.update()
        if action == 4 :
            self.create()

    def update(self):
        action = self.music.isValid(([1,2]),"Rentrer l'action à effectuer : \n 1)Transposer une partition \n 2)Inverser une Partiton\n")
        if action == 1:
            partitionData = self.action.getPartitionData()
            partition = self.music.getPlayedMusic(partitionData)
            transposeNumb = int(input("De combien voulez vous transposer la partition ?\n"))
            self.action.transpose(partition,transposeNumb)
        elif action == 2:
            partitionData = self.action.getPartitionData()
            partition = self.music.getPlayedMusic(partitionData)
            self.action.inverse(partition)

    def write(self):
        action = self.music.isValid([1,2],"Rentrer l'action à effectuer : \n 1)Ecrire et jouer la musique\n 2) Ecrire dans la base de donnée\n")
        if action == 1:
            self.action.writeAndPlay()
        elif action == 2:
            self.music.upload()

    def play(self) :
        partionData = self.action.getPartitionData()
        partition = self.music.getPlayedMusic(partionData)
        notes,duration = self.music.numericValue(partionData,partition)
        self.action.playMusic(notes,duration)

    def create(self):
        n = int(input("A partir de combien de partitions voulez-vous composer une musique ?"))
        partition = []
        partionData = self.action.getPartitionData()
        for _ in range(n):
            partition.append(self.music.getPlayedMusic(partionData))
        title = input("Donnez un titre à la musique générée")
        self.action.markov(partition,title)
