import numpy as np
import simpleaudio as sa
class musicService() :
    def __init__(self):
        pass

    def isValid(self, accepted, str_action) :
        Invalid = True
        valueAccepted = accepted
        while Invalid :
            action = int(input(str_action))
            if(action in valueAccepted) :
                Invalid = False
        return action

    def sound(self,freq, duration ):
        sample_rate = 44100
        t = np.linspace(0,duration,int(duration*sample_rate), False)
        tone = np.sin(freq * t * (6) * np.pi )
        tone *= 8388607/np.max(np.abs(tone))
        tone = tone.astype(np.int32)
        i = 0
        byte_array = []
        for b in tone.tobytes():
            if i%4 != 3 :
                byte_array.append(b)
            i+=1
        audio = bytearray(byte_array)
        play_obj = sa.play_buffer(audio,1,3,sample_rate)
        play_obj.wait_done()


    def getPlayedMusic(self, partition) :
        print("Listes des partitions : ")
        for key in partition :
            print(key, " ", partition[key][0])
        return (int(input("Veuillez rentrez votre choix : \n ")))

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
        print(durations)
        return(notes,durations)

    def upload(self) :
        title = input("Rentrer un titre")
        print('Rentrer la partition que vous voulez enregistrer : ')
        add = True
        dataset = ""
        while add :
            value = input("Rentrer une note ou faites espace pour quitter le programme : ")
            dataset += " " + value
            if value == "" :
                add = False
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
            self.length = len(d)//2
        final = "#" + str(self.length) + " " + title +"\n" + dataset
        with open("src/Partition/partitions.txt","a") as file :
            file.write(final)



