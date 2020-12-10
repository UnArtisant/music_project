from src.Service.MusicService import musicService
import numpy as np
import simpleaudio as sp

class actionService() :
    def __init__(self):
        self.music = musicService()
        self.frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:497,0:-1}

    def message(self) :
        print("hello word")

    def getTitle(self):
        pass
    
    def getPartitionData(self):
        dict = {}
        d = []
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)


    def playMusic(self):
        notes,duration = self.music.numericValue(self.getPartitionData())
        for i in range(len(notes)):
            notes[i] = self.frequency(notes[i])

