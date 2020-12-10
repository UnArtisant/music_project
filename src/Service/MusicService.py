class musicService() :
    def __init__(self):
        pass


    def numericValue(self,dico):
        d = dico[2][1]

    def getPlayedMusic(self, partition) :
        print("Listes des partitions : ")
        for key in partition :
            print(key, " ", partition[key][0])
        return int(input("Veuillez rentrez votre choix : \n "))

    def numericValue(self,dico,numb):
        d = dico[numb][1]
        partition = d.split()
        notes = []
        durations = []
        for i in partition:
            if i[-1]=="p":
                durations[-1] = durations[-1]*1.5
            else:
                note = i[:-1]
                duration = i[-1]
                dicnote = {"DO":1,"RE":2,"MI":3,"FA":4,"SOL":5,"LA":6,"SI":7,"Z":0}
                note = dicnote[note]
                dicdura = {"c":0.125,"n":0.25,"b":0.5,"r":1}
                duration = dicdura[duration]
                notes.append(note)
                durations.append(duration)
        return(notes,durations)

