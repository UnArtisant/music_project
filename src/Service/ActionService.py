"""
L'harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Ficher listant les differentes fonctions principales liées aux fonctionalités
"""
from src.Service.MusicService import musicService
import time
import random
import turtle as tr

class actionService() :
    def __init__(self):
        self.music = musicService()
        self.frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:495,0:-1}

    def playMusic(self, notes, duration):
        """
        Joue les notes une par une et gère l'annimation Turtle
        :param notes: liste de notes en valeurs numériques
        :param duration: liste de durées en secondes
        :return: rien car joue simplement la musique, fonction finale
        """
        for i in range(len(notes)):
            notes[i] = self.frequency[notes[i]]
        x = 0
        tr.bgcolor("purple")
        tr.color("red","blue")
        color = ["red","orange","yellow"]
        tr.up()
        tr.begin_fill()
        tr.backward(100)
        tr.down()
        tr.speed(0)
        tr.hideturtle()
        for i in range(len(notes)):
            tr.color(color[i%3],"blue")
            if notes[i] != -1:
                self.music.sound(notes[i],duration[i])
            else :
                time.sleep(duration[i])
            tr.forward(200)
            tr.left(180+(360/len(notes)))
        tr.end_fill()
        tr.exitonclick()

    def writeAndPlay(self):
        """
        Demande à l'utiisateur de rentrer une musique qui va être jouée sans la rentrer dans la base de donnée
        :return: rien joue simplement la musique rentrée
        """
        name = input("Entrez le nom du fichier : \n")
        partition = input("Entrez la partition : \n")
        notes,duration = self.music.numericValue({1: [name, partition]}, 1)
        self.playMusic(notes,duration)

    def transpose(self, partition, numb):
        """
        transpose la partition et l'écrit dans le fichier "partitions.txt"
        :param partition: numéro de la partition à jouer
        :param numb: nombre de fois que l'on doit transposer la musique
        :return: rien, écrit dans le fichier partition la nouvele partition générée
        """
        notes,duration = self.music.numericValue(self.music.getPartitionData(),partition)
        dicnote = {1:"DO", 2:"RE", 3:"MI", 4:"FA", 5:"SOL", 6:"LA", 7:"SI"}
        dicduration = {1:"r ", 0.5:"b ", 0.25:"n ", 0.125:"c ", 0.1875:"c p ", 0.375:"n p ", 0.75:"b p ", 1.5:"b p "}
        with open("src/Partition/partitions.txt", "r") as file:
            d = file.readlines()
        for i in range(len(notes)):
            notes[i] = dicnote[(notes[i]+numb-1)%7+1]
            duration[i] = dicduration[duration[i]]
        title = " ".join(d[(partition-1)*2].split()[1:])
        title = f"{title} transpose {numb} fois"
        lignenotes = ""
        for i in range(len(notes)):
            lignenotes += notes[i] + duration[i]
        self.music.write(title,lignenotes)

    def reverse(self, partition):
        """
        inverse la partition et l'écrit dans le fichier "partitions.txt"
        :param partition: numéro de la partition à inverser
        :return: rien, écrit dans le fichier "partitions.txt" la partition inversée
        """
        notes, duration = self.music.numericValue(self.music.getPartitionData(), partition)
        dicnote = {1: "DO", 2: "RE", 3: "MI", 4: "FA", 5: "SOL", 6: "LA", 7: "SI"}
        dicduration = {1: "r ", 0.5: "b ", 0.25: "n ", 0.125: "c ", 0.1875: "c p ", 0.375: "n p ", 0.75: "b p ",1.5: "b p "}
        with open("src/Partition/partitions.txt", "r") as file:
            d = file.readlines()
        title = " ".join(d[(partition - 1) * 2].split()[1:])
        title = f"#{len(d) // 2 + 1} {title} inversée"
        for i in range(len(notes)):
            if notes[i] != 0:
                notes[i] = dicnote[notes[i]]
            else:
                notes[i] = "Z"
            duration[i]=dicduration[duration[i]]
        noteligne = ""
        for i in range(len(notes)):
            noteligne += notes[-1-i]+duration[-1-i]
        self.music.write(title,noteligne)

    def markov1(self, partitions, title):
        """
        Applique la première version de la chaine de markov à une liste de partition et rentre la musique crée dans le fichier "partitions.txt"
        :param partitions: tableau des numéros de partitions avec lesquels on veut créer une nouvelle partition
        :param title: Titre de la partition crée
        :return: rien, écrit dans "partitions.txt" la nouvelle partition
        """
        notes,durations = [],[]
        dicnote = {1: "DO", 2: "RE", 3: "MI", 4: "FA", 5: "SOL", 6: "LA", 7: "SI"}
        dicduration = {1: "r ", 0.5: "b ", 0.25: "n ", 0.125: "c ", 0.1875: "c p ", 0.375: "n p ", 0.75: "b p ",1.5: "b p "}
        for i in partitions:
            partionData = self.music.getPartitionData()
            note, duration = self.music.numericValue(partionData, i)
            notes.append(note)
            durations.append(duration)
        tabsuccess = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        i = 0
        for note in range(len(notes)):
            z = 1
            while i < (len(notes[note-1])-2):
                if notes[note-1][i] != 0:
                    try :
                        if notes[note-1][i+1] != 0:
                            tabsuccess[notes[note-1][i]-1][notes[note-1][i+1]-1] += 1
                        else :
                            while notes[note-1][i+z] == 0:
                                z+=1
                            tabsuccess[notes[note - 1][i]-1][notes[note - 1][i + z]-1] += 1
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
        for i in range(lentot-1):
            try :
                tab = []
                for j in range(len(tabsuccess[newtab[-1]-1])):
                    tab += [j+1]*tabsuccess[newtab[-1]-1][j]
                newtab.append(tab[random.randint(0,len(tab)-1)])
            except:
                pass
        tabdura = []
        while len(tabdura)!= len(newtab):
            tabdura.append([1,0.5,0.25,0.125,0.1875,0.375,0.75,1.5][random.randint(0,7)])
        tabdura = tabdura[:len(newtab)]
        newnotes = ""
        for i in range(len(newtab)):
            newtab[i] = dicnote[newtab[i]]
            tabdura[i] = dicduration[tabdura[i]]
        for i in range(len(tabdura)):
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
        dicnote = {1: "DO", 2: "RE", 3: "MI", 4: "FA", 5: "SOL", 6: "LA", 7: "SI"}
        dicduration = {1: "r ", 0.5: "b ", 0.25: "n ", 0.125: "c ", 0.1875: "c p ", 0.375: "n p ", 0.75: "b p ",1.5: "r p "}
        for i in partitions:
            partionData = self.music.getPartitionData()
            note, duration = self.music.numericValue(partionData, i)
            notes.append(note)
            durations.append(duration)
        tabsuccess = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        i = 0
        for note in range(len(notes)):
            z = 1
            while i < (len(notes[note-1])-2):
                if notes[note-1][i] != 0:
                    try :
                        if notes[note-1][i+1] != 0:
                            tabsuccess[notes[note-1][i]-1][notes[note-1][i+1]-1] += 1
                        else :
                            while notes[note-1][i+z] == 0:
                                z+=1
                            tabsuccess[notes[note - 1][i]-1][notes[note - 1][i + z]-1] += 1
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
        while len(newtab) < lentot or i<lentot *2:
            try:
                tab = []
                for j in range(len(tabsuccess[newtab[-1]-1])):
                    tab += [j+1]*tabsuccess[newtab[-1]-1][j]
                nextnote = tab[random.randint(0,len(tab)-1)]
                newtab.append(nextnote)
                tabsuccess[newtab[-1]-1][nextnote-1] -= 1
            except:
                pass
            finally:
                i+=1
        tabdura = []
        while len(tabdura)!= len(newtab):
            tabdura.append([1,0.5,0.25,0.125,0.1875,0.375,0.75,1.5][random.randint(0,7)])
        tabdura = tabdura[:len(newtab)]
        newnotes = ""
        for i in range(len(newtab)):
            newtab[i] = dicnote[newtab[i]]
            tabdura[i] = dicduration[tabdura[i]]
        for i in range(len(tabdura)):
            newnotes += str(newtab[i])+str(tabdura[i])
        self.music.write(title,newnotes)
