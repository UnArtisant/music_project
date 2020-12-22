from src.Service.ActionService import actionService
from src.Service.MusicService import musicService

class interfaceService() :
    def __init__(self) :
        self.action = actionService()
        self.music = musicService()
    
    def interface(self) :
        action = self.music.isValid([1,2,3,4,0], "Rentrer l'action à effectuer : \n 1) Jouer une partition \n 2) Ecrire une partition \n 3) Modifier une partition \n 4) Créer une partition à partir de celles dans la base de donnée \n 0) Quitter le programme \n")

        if action == 1 :
            self.play()
        elif action == 2 :
            self.write()
        elif action == 3 :
            self.update()
        elif action == 4 :
            self.create()
        if action != 0:
            self.interface()

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
        action = self.music.isValid([1,2],"Voulez vous créer une partition avec : \n 1) La Version 1 de la chaîne de Markov \n 2) La Version 2 de la chaîne de Markov \n")
        if action == 1:
            n = int(input("A partir de combien de partitions voulez-vous composer une musique ? \n"))
            partition = []
            partionData = self.action.getPartitionData()
            for _ in range(n):
                partition.append(self.music.getPlayedMusic(partionData))
            title = input("Donnez un titre à la musique générée : \n")
            self.action.markov1(partition,title)
        elif action == 2:
            n = int(input("A partir de combien de partitions voulez-vous composer une musique ? \n"))
            partition = []
            partionData = self.action.getPartitionData()
            for _ in range(n):
                partition.append(self.music.getPlayedMusic(partionData))
            title = input("Donnez un titre à la musique générée : \n")
            self.action.markov2(partition, title)