from src.Service.MusicService import musicService

class actionService() :
    def __init__(self):
        self.music = musicService()

    frequency = {1,}

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
        notes,duration = self.music.numericValue(self.getTitle())


