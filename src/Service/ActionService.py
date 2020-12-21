from src.Service.MusicService import musicService
import numpy as np
import time
import random

class actionService() :
    def __init__(self):
        self.music = musicService()
        self.frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:495,0:-1}
    
    def getPartitionData(self):
        dict = {}
        d = []
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)

    def playMusic(self,notes,duration):
        for i in range(len(notes)):
            notes[i] = self.frequency[notes[i]]
        for i in range(len(notes)):
            if notes[i] != -1:
                self.music.sound(notes[i],duration[i])
            else :
                time.sleep(duration[i])

    def writeAndPlay(self):
        name = input("Entrez le nom du fichier : \n")
        partition = input("Entrez la partition : \n")
        notes,duration = self.music.numericValue({1: [name, partition]}, 1)
        self.playMusic(notes,duration)

    def transpose(self,partition,numb):
        notes,duration = self.music.numericValue(self.getPartitionData(),partition)
        dicnote = {1:"DO", 2:"RE", 3:"MI", 4:"FA", 5:"SOL", 6:"LA", 7:"SI"}
        dicduration = {1:"r ", 0.5:"b ", 0.25:"n ", 0.125:"c ", 0.1875:"c p ", 0.375:"n p ", 0.75:"b p ", 1.5:"b p "}
        with open("src/Partition/partitions.txt", "r") as file:
            d = file.readlines()
        for i in range(len(notes)):
            notes[i] = dicnote[(notes[i]+numb-1)%7+1]
            duration[i] = dicduration[duration[i]]
        title = " ".join(d[(partition-1)*2].split()[1:])
        title = f"#{len(d)//2+1} {title} transpose {numb} fois"
        lignenotes = ""
        for i in range(len(notes)):
            lignenotes += notes[i] + duration[i]
        self.music.write(title,lignenotes)

    def inverse(self,partition):
        notes, duration = self.music.numericValue(self.getPartitionData(), partition)
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

    def markov1(self,partitions,title):
        notes,durations = [],[]
        dicnote = {1: "DO", 2: "RE", 3: "MI", 4: "FA", 5: "SOL", 6: "LA", 7: "SI"}
        dicduration = {1: "r ", 0.5: "b ", 0.25: "n ", 0.125: "c ", 0.1875: "c p ", 0.375: "n p ", 0.75: "b p ",1.5: "b p "}
        for i in partitions:
            partionData = self.getPartitionData()
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
                            print(notes[note-1][i])
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
        with open("src/Partition/partitions.txt", "r") as file:
            d = file.readlines()
        title = f"#{len(d) // 2 + 1} {title}"
        self.music.write(title,newnotes)





