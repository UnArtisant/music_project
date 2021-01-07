"""
L’harmonie est numérique
Raphaël BARRIET, Pierre-Marie HERRBURGER--PIETRI
Fonctions secondaires nécessaires à l'executions des fonctions primaires du fichier Action
"""
import numpy as np
import simpleaudio as sa

class musicService() :
    def __init__(self,file):
        self.file = file
        self.dicnotenum = {"DO": 1, "RE": 2, "MI": 3, "FA": 4, "SOL": 5, "LA": 6, "SI": 7, "Z": 0}
        self.dicduranum = {"c": 0.125, "n": 0.25, "b": 0.5, "r": 1}

    def getPartitionData(self):
        """
        Permet d'obtenir les partitions du fichier "partitions.txt" de manière utilisable
        :return: dictionaire associant leur numéro à chaque partition, chaque partition étant un tableau de la forme[titre,notes]
        """
        dict = {}
        d = []
        #récupère une liste de toutes les lignes du fichier
        with open(f"src/Partition/{self.file}","r") as file:
            d = file.readlines()
        #Crée un dictionnaire avec comme clé le numéro de partition et comme valeur un tableau [titre,partition]
        for i in range(len(d)//2):
            dict[i+1] = [d[i*2],d[i*2+1]]
        return(dict)

    def isValid(self, accepted, str_action):
        """
        Permet d'obtenir une valeur lors d'un choix de l'utilisateur de manière sécurisée (En gérant les mauvaises entrées)
        :param accepted: valeurs acceptées lors de la saisie
        :param str_action: Texte étant affiché lors du choix de l'utilisateur
        :return: le chiffre correspondant à l'action voulue par l'utilisateur dans le cas ou elle est valide
        """
        Invalid = True
        valueAccepted = accepted
        while Invalid :
            try :
                action = int(input(str_action))
                assert action in valueAccepted
                Invalid = False
            except ValueError: #S'effectue que si l'erreur de type de valeur apparait
                print("Vous n'avez pas entré de nombre mais une chaîne  caractère.\n")
            except AssertionError:  # S'effectue que si le assert n'est pas vérifié
                print("Veuillez entrer une valeur parmis celles proposées.\n")
        return action

    def sound(self, freq, duration):
        """
        Permet de jouer une note
        :param freq: fréquence de la note jouée
        :param duration: durée de la note jouée
        :return: rien, joue simplement le son de la note
        """
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
        """
        Permet d'obtenir le choix de partition de l'utilisateur
        :param partition: dictionnaire des partitions obtenu avec getPartitionData
        :return: Le choix de l'utilisateur
        """
        Invalid = True
        while Invalid:
            try:
                #Affiche tous les titres de partitions
                print("Listes des partitions : ")
                for key in partition :
                    print(partition[key][0][:-1])
                #Demande le choix de l'utilisateur
                choice =int(input("Veuillez rentrez votre choix : \n "))
                assert 0<choice<=len(partition)
                Invalid = False
            except AssertionError: #Si le chiffre entré ne correspond a aucune partition
                print("Le numéro de partition n'existe pas")
            except ValueError: #Si l'entrée de l'utilisateur n'est pas un nombre
                print("Vous devez entrer un numéro")
        return(choice)

    def numericValue(self, dico, numb):
        """
        Permet d'obtenir des listes de notes et durées utilisables plus facilement dans les autres fonctions
        :param dico: dictionnaire des partitions obtenu avec getPartitionData
        :param numb: le numéro de la partition choisie par l'utilisateur
        :return: deux tableaux : un de notes en valeurs numériques, chaque valeur correspondant à une note (1,2,3,4,5,6,7...)
                                 un de durées en secondes (0.125,0.25,0.5,1,...)
        """
        #Récupère la partition comme un tableau des notes
        partition = dico[numb][1].split()
        notes = []
        durations = []
        for i in partition:
            if i[-1] == "p":
                #Si la durée est "p" alors on doit multiplier la derniere durée par 1.5
                durations[-1] = durations[-1]*1.5
            else:
                #Sinon affecter a chaque note sa valeur numerique et a chaque duree sa valeur en secondes
                note = i[:-1]
                duration = i[-1]
                note = self.dicnotenum[note]
                duration = self.dicduranum[duration]
                #Et ajouter ces nouvelles valeurs dans les tableaux de notes et durées
                notes.append(note)
                durations.append(duration)
        return(notes,durations)

    def write(self, title, notes):
        """
        Permet d'écrire une partition de manière sécurisée, verifiant les entrées pour ne pas rentrer de partition inutilisable
        :param title: Titre de la musique à écrire
        :param notes: notes de la partition
        :return: rien, écrit la partition dans le fichier "partitions.txt"
        """
        #Ouvre le fichier pour savoir quel numéro afficher à la partition entrée
        with open(f"src/Partition/{self.file}", "r") as file:
            longueur = len(file.readlines())//2+1
        #Ajoute le nouveau numéro de partition au titre
        title = f"#{longueur} {title}"
        t = True
        #Vérifie le format de la partition
        for i in range(len(notes.split())):
            if notes.split()[i] != "p":
                if notes.split()[i][:-1] not in "DOREMIFASOLLASIDOZ" or notes.split()[i][-1] not in "nbrcp":
                    t = False
        #Si le format est bien vérifié, écrire la partition dans le fichier
        if t :
            with open("src/Partition/partitions.txt", "a") as file:
                file.write(f"{title}\n{notes}\n")
        #Sinon Afficher un message d'erreur à l'utilisateur
        else:
            print("La partition rentrée n'est pas sous le bon format\n")
