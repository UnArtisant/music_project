#Fonctions secondaires nécessaires à l'executions des fonctions primaires du fichier Action
import numpy as np
import simpleaudio as sa

class musicService() :
    def __init__(self):
        pass

    def getPartitionData(self):
        dict = {}
        d = []
        with open("src/Partition/partitions.txt","r") as file:
            d = file.readlines()
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)

    def isValid(self, accepted, str_action) :
        Invalid = True
        valueAccepted = accepted
        while Invalid :
            try :
                action = int(input(str_action))
                assert action in valueAccepted
                Invalid = False
            except ValueError:
                print("Vous n'avez pas rentré de nombre.\n")
            except AssertionError:
                print("Veuillez entrer une valeur parmis celles proposées\n")
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

    def getPlayedMusic(self, partition):
        print("Listes des partitions : ")
        for key in partition :
            print(key, " ", partition[key][0][:-1])
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
        return(notes,durations)

    def write(self,title,notes):
        with open("src/Partition/partitions.txt", "r") as file:
            longueur = len(file.readlines())//2+1
        title = f"#{longueur} {title}"
        t = True
        for i in range(len(notes.split())):
            if notes.split()[i][:-1] not in "DOREMIFASOLLASIDO" or notes.split()[i][-1] not in "nbrcp":
                t = False
        if t :
            with open("src/Partition/partitions.txt", "a") as file:
                file.write(f"{title}\n{notes}\n")
        else:
            print("La partition rentrée n'est pas sous le bon format\n")
