"""
L'harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Ficher listant les differentes fonctions principales liées aux fonctionalités
"""
from src.Service.MusicService import musicService
import random
import turtle as tr

class actionService() :
    def __init__(self,file):
        self.music = musicService(file)
        self.frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:495,0:-1}
        self.file = file
        self.dicnotefile = {1: "DO", 2: "RE", 3: "MI", 4: "FA", 5: "SOL", 6: "LA", 7: "SI"}
        self.dicdurationfile = {1: "r ", 0.5: "b ", 0.25: "n ", 0.125: "c ", 0.1875: "c p ", 0.375: "n p ", 0.75: "b p ",1.5: "r p "}

    def playMusic(self, notes, duration,title):
        """
        Joue les notes une par une et gère l'annimation Turtle
        :param notes: liste de notes en valeurs numériques
        :param duration: liste de durées en secondes
        :param title: titre de la musique jouée
        :return: rien car joue simplement la musique, fonction finale
        """
        for i in range(len(notes)):
            notes[i] = self.frequency[notes[i]]
        try:
            x = 0
            tr.TurtleScreen._RUNNING = True
            tr.bgcolor("purple")
            tr.speed(0)
            tr.up()
            tr.setpos(0, -150)
            tr.down()
            tr.color("white")
            tr.write(title,False,align="center", font=("Arial", 10, "normal"))
            tr.color("red","blue")
            color = ["red","orange","yellow"]
            tr.up()
            tr.setpos(0,0)
            tr.begin_fill()
            tr.backward(100)
            tr.down()
            tr.hideturtle()
            for i in range(len(notes)):
                tr.color(color[i%3],"blue")
                tr.forward(200)
                tr.left(180 + (360 / len(notes)))
                self.music.sound(notes[i], duration[i])
            tr.end_fill()
            tr.exitonclick()
        except tr.Terminator:
            print("\nMusique fermée\n")

    def writeAndPlay(self):
        """
        Demande à l'utiisateur de rentrer une musique qui va être jouée sans la rentrer dans la base de donnée
        :return: rien joue simplement la musique rentrée
        """
        name = input("Entrez le nom de la partition : \n")
        partition = input("Entrez la partition : \n")
        notes,duration = self.music.numericValue({1: [name, partition]}, 1)
        self.playMusic(notes,duration,name)

    def transpose(self, partition, numb):
        """
        transpose la partition et l'écrit dans le fichier "partitions.txt"
        :param partition: numéro de la partition à jouer
        :param numb: nombre de fois que l'on doit transposer la musique
        :return: rien, écrit dans le fichier partition la nouvele partition générée
        """
        notes,duration = self.music.numericValue(self.music.getPartitionData(),partition)
        with open(f"src/Partition/{self.file}", "r") as file:
            d = file.readlines()
        for i in range(len(notes)):
            notes[i] = self.dicnotefile[(notes[i]+numb-1)%7+1]
            duration[i] = self.dicdurationfile[duration[i]]
        title = " ".join(d[(partition-1)*2][:-1].split()[1:])
        title = f"{title} transpose {numb} fois"
        lignenotes = ""
        for i in range(len(notes)):
            lignenotes += notes[i] + duration[i]
        self.music.write(title,lignenotes)
        print("\n La partition a bien été ajoutée")

    def reverse(self, partition):
        """
        inverse la partition et l'écrit dans le fichier "partitions.txt"
        :param partition: numéro de la partition à inverser
        :return: rien, écrit dans le fichier "partitions.txt" la partition inversée
        """
        notes, duration = self.music.numericValue(self.music.getPartitionData(), partition)
        with open(f"src/Partition/{self.file}", "r") as file:
            d = file.readlines()
        title = " ".join(d[(partition-1)*2][:-1].split()[1:])
        title = f"{title} inversée"
        noteligne = ""
        for i in range(len(notes)):
            if notes[i]!=0:
                notes[i]= 8-notes[i]
            noteligne+=self.dicnotefile[notes[i]] + self.dicdurationfile[duration[i]]
        self.music.write(title,noteligne)
        print("\n La partition a bien été ajoutée")

    def markov1(self, partitions, title):
        """
        Applique la première version de la chaine de markov à une liste de partition et rentre la musique crée dans le fichier "partitions.txt"
        :param partitions: tableau des numéros de partitions avec lesquels on veut créer une nouvelle partition
        :param title: Titre de la partition crée
        :return: rien, écrit dans "partitions.txt" la nouvelle partition
        """
        notes,durations = [],[]
        for i in partitions:
            partionData = self.music.getPartitionData()
            note, duration = self.music.numericValue(partionData, i)
            notes.append(note)
            durations.append(duration)
        tabdatadurations = []
        tabsuccess = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        for duration in range(len(durations)):
            for i in range(len(durations[duration])):
                tabdatadurations.append(durations[duration][i])
        for note in notes:
            z = 1
            i = 0
            while i < (len(note) - 2):
                if note[i] != 0:
                    try:
                        if note[i + 1] != 0:
                            tabsuccess[note[i] - 1][note[i + 1] - 1] += 1
                        else:
                            while note[i + z] == 0:
                                z += 1
                            tabsuccess[note[i] - 1][note[i + z] - 1] += 1
                            i += 1
                    except:
                        pass
                else:
                    i += 1
                i += 1
        lentot = 0
        print(f"tabsuccess {tabsuccess}")
        for i in notes:
            lentot+=len(i)
        newtab = [random.randint(1,7)]
        for i in range(lentot-1):
            try :
                tab = []
                for j in range(len(tabsuccess[newtab[-1]-1])):
                    tab += [j+1]*tabsuccess[newtab[-1]-1][j]
                newtab.append(tab[random.randint(0,len(tab)-1)])
            except:
                pass
        tabdura = []
        for _ in range(len(newtab)):
            tabdura.append(tabdatadurations[random.randint(0, len(tabdatadurations) - 1)])
        tabdura = tabdura[:len(newtab)]
        newnotes = ""
        for i in range(len(newtab)):
            newtab[i] = self.dicnotefile[newtab[i]]
            tabdura[i] = self.dicdurationfile[tabdura[i]]
        for i in range(len(newtab)):
            newnotes += str(newtab[i])+str(tabdura[i])
        self.music.write(title,newnotes)

    def markov2(self, partitions, title):
        """
        Applique la deuxième version de la chaine de markov à une liste de partition et rentre la musique crée dans le fichier "partitions.txt"
        :param partitions: tableau des numéros de partitions avec lesquels on veut créer une nouvelle partition
        :param title: Titre de la partition crée
        :return: rien, écrit dans "partitions.txt" la nouvelle partition
        """
        notes,durations = [],[]
        for i in partitions:
            partionData = self.music.getPartitionData()
            note, duration = self.music.numericValue(partionData, i)
            notes.append(note)
            durations.append(duration)
        tabsuccess = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        tabdatadurations = []
        for duration in range(len(durations)):
            for i in range(len(durations[duration])):
                tabdatadurations.append(durations[duration][i])
        for note in notes:
            z = 1
            i=0
            while i < (len(note)-2):
                if note[i] != 0:
                    try :
                        if note[i+1] != 0:
                            tabsuccess[note[i]-1][note[i+1]-1] += 1
                        else :
                            while note[i+z] == 0:
                                z+=1
                            tabsuccess[note[i]-1][note[i + z]-1] += 1
                            i+=1
                    except:
                        pass
                else :
                    i+=1
                i+=1
        lentot = 0
        for i in notes:
            lentot+=len(i)
        newtab = [random.randint(1,7)]
        i = 0
        while len(newtab) < lentot and i<lentot **2:
            try:
                tab = []
                for j in range(len(tabsuccess[newtab[-1]-1])):
                    tab += [j+1]*tabsuccess[newtab[-1]-1][j]
                nextnote = tab[random.randint(0,len(tab)-1)]
                newtab.append(nextnote)
                tabsuccess[newtab[-1]-1][nextnote-1] -= 1
            except:
                pass
            i+=1
        tabdura = []
        for _ in range(len(newtab)):
            duration = tabdatadurations[random.randint(0, len(tabdatadurations) - 1)]
            tabdura.append(duration)
            tabdatadurations.remove(duration)
        tabdura = tabdura[:len(newtab)]
        tabdura = tabdura[:len(newtab)]
        newnotes = ""
        for i in range(len(newtab)):
            newtab[i] = self.dicnotefile[newtab[i]]
            tabdura[i] = self.dicdurationfile[tabdura[i]]
        for i in range(len(newtab)):
            newnotes += str(newtab[i])+str(tabdura[i])
        self.music.write(title,newnotes)
