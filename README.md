# SuperTronc
Team's project in python. Creation of a multiplayer game on local server with Threads and Pygame library.

# FR : 

***

## Étapes du projet

### 1. Création du serveur et de la classe Network pour les connexions 🔗

Le code du serveur utilise la bibliothèque socket pour créer un serveur qui écoute sur l'adresse IP "127.0.0.1" et le port 5555. Lorsqu'un client se connecte, le serveur envoie les données du joueur à l'aide de "pickle" et crée un nouveau thread pour gérer la communication avec ce client.

Le serveur crée deux objets `Player` pour représenter les deux joueurs dans le jeu. Ces objets définissent la position initiale, la couleur, la taille et d'autres attributs des joueurs. Le serveur envoie ces objets au client pour l'initialisation.

Le serveur utilise des threads pour gérer les connexions des deux joueurs de manière concurrente. Chaque thread est responsable de la communication avec un joueur spécifique. Lorsqu'un joueur envoie ses données de déplacement, le serveur les reçoit, les désérialise à l'aide de "pickle", met à jour l'objet `Player` correspondant, puis renvoie les données du joueur adverse.

### 2. Implémentation des clients et des classes joueur 🕹️

Les clients utilisent Pygame pour créer une fenêtre de jeu. Chaque client a son propre objet `Player` qui représente le joueur qu'il contrôle. Le joueur est un carré coloré qui peut être déplacé à l'aide des touches fléchées.

Les clients utilisent également la classe `Network` pour communiquer avec le serveur. Lorsque le client démarre, il se connecte au serveur, reçoit les données initiales du joueur et les stocke dans son propre objet `Player`. Le client utilise la classe `Network` pour envoyer ses données de déplacement au serveur et recevoir les données du joueur adverse.

### 3. Création des murs de la fenêtre et déplacement en X et Y 🏰

Les fenêtres de jeu ont une taille fixe de 500x500 pixels. Les murs sont représentés par des bords noirs dans les fenêtres. Les joueurs ne peuvent pas passer à travers ces murs.

Les joueurs se déplacent en utilisant les touches fléchées du clavier pour se déplacer vers la gauche, la droite, le haut et le bas. Les déplacements sont contraints aux limites de la fenêtre, de sorte que les joueurs ne peuvent pas sortir de l'écran.

### 4. Création des traînées 🎨

Les traînées sont gérées par la classe `Player`. À chaque déplacement du joueur, sa position précédente est enregistrée dans une liste appelée `trail`. La couleur de la traînée est la même que la couleur du joueur. La longueur de la traînée est limitée pour éviter une accumulation excessive de données.

Lorsque la traînée est dessinée à l'écran, la classe `Player` parcourt la liste des positions précédentes et dessine des carrés de la couleur de la traînée à ces positions. Cela crée l'effet de traînée derrière le joueur.

### 5. Création des collisions 💥

Les collisions sont gérées par la classe `Player`. La méthode `has_exceeded_boundaries` vérifie si le joueur a dépassé les limites de la fenêtre. Si c'est le cas, le joueur a perdu la partie, et le gagnant est déterminé en fonction de sa couleur.

La méthode `has_collided_with` vérifie s'il y a une collision avec l'autre joueur. Elle vérifie d'abord s'il y a une collision avec le rectangle défini par l'autre joueur, puis si le joueur entre en collision avec la traînée de l'autre joueur. Si une collision est détectée, le joueur a perdu la partie, et le gagnant est déterminé.

### 6. Correction des bugs 🐛

Le projet peut comporter des bugs potentiels, notamment des problèmes de gestion des déconnexions de joueurs, des erreurs de sérialisation/désérialisation, ou d'autres problèmes spécifiques au jeu. La correction des bugs implique généralement de tester le jeu, de surveiller les problèmes, de déboguer le code et de les corriger au fur et à mesure.

