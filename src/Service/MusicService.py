from src.Service.ActionService import actionService
class musicService() :
    def __init__(self):
        pass

    def numericValue(self,numb):
        d = actionService.getTitle()[numb]
        partition = d.split()
        notes = []
        duration = []
        for i in partition:
            if i[-1]=="p":
                duration[-1] = duration[-1]*1.5
            else:
                notes.append(i[:-1])
                duration.append(i[-1])
        for i in range(len(notes)):
            if notes[i] == "DO":
                notes[i] = 1
            elif notes[i] =="RE":
                notes[i] = 2
            elif notes[i] =="MI":
                notes[i] = 3
            elif notes[i] =="FA":
                notes[i] = 4
            elif notes[i] =="SOL":
                notes[i] = 5
            elif notes[i] =="LA":
                notes[i] = 6
            elif notes[i] =="SI":
                notes[i] = 7
            elif notes[i] == "Z":
                notes[i] = 0
        for i in range(len(duration)):
            if duration[i]== "c":
                duration[i] = 0.125
            if duration[i]== "n":
                duration[i] = 0.250
            if duration[i]== "b":
                duration[i] = 0.500
            if duration[i]== "r":
                duration[i] = 1