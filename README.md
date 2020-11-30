# music_project
Projet semestriel 1 efrei paris
Fonctionnalités:
(a) Le codage des notes musicales :
En vrai flemme de les faire à la main, go le faire avec un algorithme simple: input().split la chaîne puis prendre la dernière lettre de chaque qui est la durée et tester, puis prendre [:-1] de chaque note pour en extraire la note puis tester pour donner un tableau de notes et un tableau de durées puis après concaténer le tout dans un string qu’on print puis à coller dans les fichiers textes des partitions
	Transposer les notes en valeures numériques : plus pratique pour la transposition
(b) L’attribution de fréquences et des durées aux notes ; 
-créer un dictionnaire avec toutes les différentes notes et leur fréquence
-créer un dictionnaire avec toutes les différentes durées de notes
(c) L’application de transformations mathématiques telles que la transposition ou l’inversion pour la création de nouvelles partitions musicales ; 
	-Transposition :prendre la liste des notes et demander la valeur k(de combien on va transposer) faire liste[i]=(liste[i]+k)%nombre de notes dans une boucle for in range(len(liste)) 
	-inversion : prendre les deux tableaux contenant les notes/durées et avec une boucle for i in range(len(liste)) append la valeur liste[-1-i] dans des listes nouvelles contenant les partitions inversées
(d) L’utilisation des chaînes de Markov (2 versions) pour la création de nouvelles partitions à partir d’une ou plusieurs mélodie (s) ;
	Demander à partir de quelles partitions on veut créer une nouvelle partition
	lire sur le doc et transposer la version 2:
	lire toutes les partitions et relever tous les tableaux
	tirer au hasard la première note et tirer au hasard parmi les notes qui l’ont déjà suivies avec les probabilités équivalentes puis répéter l’opération avec la note tirée jusqu’à fin.


Ajouter les fonctionnalités dans le menu et créer le fichier  main dans lequel on va faire toutes les interactions/menu ect...

créer l’interface Turtle contenant le menu/animation
Le menu ne nécessite pas l’utilisation d’interface graphique mais c’est quand meme 2000* plus classe qu’un vieux menu par console.
Je viens de regarder mais enfaite Turtle c’est du dessin pour enfant ptdr je l’utilisais en maths en 3eme dans un logiciel appelé géotortue c’est claqué au sol je vais apprendre Tkinter en entier pour les menus mais on fera quand même les animations via Turtle histoire de pas leur dire que leur sujet pue trop

Reste plus qu’à se répartir les taches
