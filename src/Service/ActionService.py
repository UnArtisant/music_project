class actionService() :
    def __init__(self):
        pass

    def message(self) :
        print("hello word")

    def getTitle(self):
        dict = {}
        d = []
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)

    def playMusic(self):

