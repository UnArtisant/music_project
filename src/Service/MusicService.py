class musicService() :
    def __init__(self):
        pass

    def numericValue(self,dico):
        d = dico[2][1]
        partition = d.split()
        notes = []
        durations = []
        for i in partition:
            if i[-1]=="p":
                durations[-1] = durations[-1]*1.5
            else:
                note = i[:-1]
                duration = i[-1]
                if note == "DO":
                    note = 1
                elif note == "RE":
                    note = 2
                elif note == "MI":
                    note = 3
                elif note == "FA":
                    note = 4
                elif note == "SOL":
                    note = 5
                elif note == "LA":
                    note = 6
                elif note == "SI":
                    note = 7
                elif note == "Z":
                    note = 0
                if duration == "c":
                    duration = 0.125
                if duration == "n":
                    duration = 0.250
                if duration == "b":
                    duration = 0.500
                if duration == "r":
                    duration = 1
                notes.append(note)
                durations.append(duration)
        return(notes,durations)