"""
L'harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Fichier Interface servant de menu.
"""
from src.Service.ActionService import actionService
from src.Service.MusicService import musicService

class interfaceService() :
    def __init__(self,file):
        self.action = actionService(file)
        self.music = musicService(file)
        self.file = file

    def interface(self):
        """
        Menu principal, sert à rediger l'utilisateur vers un second menu correspondant à la fonctionnalité qu'il a choisi
        :return: rien, redirige juste l'utilsateur vers la fonction associée à son choix
        """
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
        """
        Sous menu de la fonctionalité modifier : permet à l'utilisateur de faire le choix entre transposer une musique ou l'inverser
        :return: rien, redirige l'utilisateur vers la fonction associée à son choix
        """
        action = self.music.isValid(([1,2]),"Rentrer l'action à effectuer : \n 1) Transposer une partition \n 2) Inverser une Partiton\n")
        if action == 1:
            partitionData = self.music.getPartitionData()
            partition = self.music.getPlayedMusic(partitionData)
            transposeNumb = int(input("De combien voulez vous transposer la partition ?\n"))
            self.action.transpose(partition,transposeNumb)
        elif action == 2:
            partitionData = self.music.getPartitionData()
            partition = self.music.getPlayedMusic(partitionData)
            self.action.reverse(partition)

    def write(self):
        """
        Sous menu de la fonctionalité ecrire : Permet à l'utilisateur de faire le choix entre rentrer une partition dans le fichier "partitions.txt" ou jouer la partition qu'il est entrain d'ecrire
        :return: rien, redirige l'utilisateur vers la fonction associée à son choix
        """
        action = self.music.isValid([1,2],"Rentrer l'action à effectuer : \n 1) Ecrire et jouer la musique\n 2) Ecrire dans la base de donnée\n")
        if action == 1:
            self.action.writeAndPlay()
        elif action == 2:
            title = input("Entrez le nom de votre musique : \n")
            notes = input("Entrez votre partition : \n")
            self.music.write(title, notes)

    def play(self):
        """
        Demande à l'utilisateur la musique qu'il veut jouer et la joue
        :return: rien, permet de récupérer les données pour jouer la musique choisie
        """
        partionData = self.music.getPartitionData()
        partition = self.music.getPlayedMusic(partionData)
        notes,duration = self.music.numericValue(partionData,partition)
        title = partionData[partition][0]
        self.action.playMusic(notes,duration,title)

    def create(self):
        """
        Sous menu des chaines de markov : permet à l'utilisateur de choisir entre créer une musique à partir de la version 1 ou de la version 2 de la chaîne de Markov
        :return: rien, redirige l'utilisateur vers la fonction associée à son choix
        """
        action = self.music.isValid([1,2],"Voulez vous créer une partition avec : \n 1) La Version 1 de la chaîne de Markov \n 2) La Version 2 de la chaîne de Markov \n")
        action2 = self.music.isValid([1,2]," Voulez vous appliquer les chaînes de markov :\n 1) A une seule partition \n 2) la base de donnée ?\n")
        partition = []
        partionData = self.music.getPartitionData()
        if action2 == 1:
            partition.append(self.music.getPlayedMusic(partionData))
        elif action2 == 2:
            for i in range(len(partionData.keys())):
                partition.append(i+1)
        title = input("Donnez un titre à la musique générée : \n")
        if action == 1:
            self.action.markov1(partition,title)
        elif action == 2:
            self.action.markov2(partition, title)

