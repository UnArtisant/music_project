from src.Service.MusicService import musicService
import numpy as np
import simpleaudio as sa

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

    def sound(self,freq, duration ):
        sample_rate = 44100
        t = np.linspace(0,duration,int(duration*sample_rate),False)
        tone = np.sin(freq * t * (6) * np.pi )
        i=0
        byte_array = []
        for b in tone.tobytes():
            if i%4 != 3 :
                byte_array.append(b)
            i+=1
        audio = bytearray(byte_array)
        play_obj = sa.play_buffer(audio,1,3,sample_rate)
        play_obj.wait_done()

    def playMusic(self,numbfile):
        notes,duration = self.music.numericValue(self.getPartitionData(),numbfile)
        for i in range(len(notes)):
            notes[i] = self.frequency[notes[i]]
        for i in range(len(notes)):
            if notes[i] != 0:
                self.sound(notes[i],duration[i])
            else :
                np.sleep(duration[i])
