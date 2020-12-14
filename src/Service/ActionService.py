from src.Service.MusicService import musicService
import numpy as np

class actionService() :
    def __init__(self):
        self.music = musicService()
        self.frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:497,0:-1}
    
    def getPartitionData(self):
        dict = {}
        d = []
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)



    def playMusic(self,numbfile):
        notes,duration = self.music.numericValue(self.getPartitionData(),numbfile)
        for i in range(len(notes)):
            notes[i] = self.frequency[notes[i]]
        for i in range(len(notes)):
            if notes[i] != 0:
                self.music.sound(notes[i],duration[i])
            else :
                np.sleep(duration[i])
