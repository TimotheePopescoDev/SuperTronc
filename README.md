# SuperTronc
Team's project in python. Creation of a multiplayer game on local server with Threads and Pygame library.
Maximilien Menesguen, Timothée Popesco, Anne-Julie Hoye, Romain Theron.

## Informations to play and launch the game : 
First be sure to have python and pygame install on your computer. Then for local access in server's script : 127.0.0.1 in network's script : 127.0.0.1. For "online" access on server's script : 0.0.0.0 in network's script : "IPV4". You can find your ip with ifconfig in your terminal Linux.
Finally you have to launch serveur.py in the terminal and then client.py and client2.py in the terminal.
Then you just have to move with arrow and enjoy.

# EN : 

## Project Stages

### 1. Server Creation and Network Class for Connections 🔗

The server code utilizes the socket library to create a server that listens on IP address "127.0.0.1" and port 5555. When a client connects, the server sends the player's data using "pickle" and creates a new thread to handle communication with that client.

The server creates two `Player` objects to represent the two players in the game. These objects define the initial position, color, size, and other attributes of the players. The server sends these objects to the client for initialization.

The server uses threads to manage connections from the two players concurrently. Each thread is responsible for communication with a specific player. When a player sends their movement data, the server receives it, deserializes it using "pickle," updates the corresponding `Player` object, and then sends the data of the opposing player.

#### Usage of the "pickle" Library in the Project

##### Serialization and Deserialization

The "pickle" library is used in this project for the serialization and deserialization of Python objects. Here's how it works:

- **Serialization:** When a Python object needs to be sent from a client to a server or vice versa, or even when it needs to be stored on disk, it is serialized into a binary representation. "pickle" is used to accomplish this task. For example, in the project, `Player` objects are serialized before being sent to the server for initialization.

    ```python
    # Serializing an object with pickle
    player_data = pickle.dumps(player_object)
    ```

- **Deserialization:** When binary data is received by the other party (e.g., the server), it needs to be deserialized to reconstruct the original Python object. "pickle" is also used for this step. For example, in the project, the server receives binary data and deserializes it to obtain the `Player` object.

    ```python
    # Deserializing an object with pickle
    player_object = pickle.loads(player_data)
    ```

##### Usage in the Network Class

The `Network` class in the project contains methods for the serialization and deserialization of data exchanged between clients and the server. Here's how "pickle" is used in this class:

- The `send` method is used to send data from a client to the server. It serializes the data with "pickle" before sending it.

    ```python
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)
    ```

- The `connect` method is used to receive data from the server. It first receives the data in binary form and then deserializes it with "pickle" to obtain the original object.

    ```python
    def connect(self):
        try:
            self.client connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    ```

##### Security and Limitations

It's important to note that "pickle" can be powerful but should be used with caution as it can execute arbitrary code during deserialization. This means when using "pickle," you should ensure that data comes from trusted sources as malicious data could potentially pose security issues.

Furthermore, "pickle" is not suitable for serializing objects intended to be shared between different versions of Python as serialization formats can vary between versions. In this project, communication is conducted between Python clients and a server, simplifying compatibility.

### 2. Implémentation des clients et des classes joueur 🕹️

Les clients utilisent Pygame pour créer une fenêtre de jeu. Chaque client a son propre objet `Player` qui représente le joueur qu'il contrôle. Le joueur est un carré coloré qui peut être déplacé à l'aide des touches fléchées.

### 2. Implementation of Clients and Player Classes 🕹️

Clients use Pygame to create a game window. Each client has its own `Player` object representing the player they control. The player is a colored square that can be moved using the arrow keys.

Clients also utilize the `Network` class to communicate with the server. When the client starts, it connects to the server, receives initial player data, and stores it in their own `Player` object. The client uses the `Network` class to send their movement data to the server and receive data of the opposing player.

### 3. Creation of Window Borders and Movement in X and Y 🏰

Game windows have a fixed size of 500x500 pixels. Black borders represent the walls in the windows, preventing players from moving through them.

Players move using the arrow keys on the keyboard to navigate left, right, up, and down. Movement is constrained within the window boundaries to prevent players from going off-screen.

### 4. Creation of Traces 🎨

Traces are managed by the `Player` class. With each player's movement, their previous position is recorded in a list called `trail`. The trace's color matches the player's color. The length of the trace is limited to prevent excessive data accumulation.

When the trace is drawn on the screen, the `Player` class iterates through the list of previous positions and draws squares of the trace's color at those positions, creating the trailing effect behind the player.

### 5. Handling Collisions 💥

Collisions are managed by the `Player` class. The `has_exceeded_boundaries` method checks if the player has gone beyond the window's boundaries. If this happens, the player has lost the game, and the winner is determined based on their color.

The `has_collided_with` method checks for collisions with the other player. It first checks for a collision with the rectangle defined by the other player and then if there is a collision with the trace of the other player. If a collision is detected, the player has lost the game, and the winner is determined.

### 6. Bug Fixes 🐛

The project may have potential bugs, including issues with handling player disconnections, serialization/deserialization errors, or other game-specific problems. Bug fixing typically involves game testing, issue monitoring, code debugging, and making corrections as needed.

***

# FR : 

## Étapes du projet

### 1. Création du serveur et de la classe Network pour les connexions 🔗

Le code du serveur utilise la bibliothèque socket pour créer un serveur qui écoute sur l'adresse IP "127.0.0.1" et le port 5555. Lorsqu'un client se connecte, le serveur envoie les données du joueur à l'aide de "pickle" et crée un nouveau thread pour gérer la communication avec ce client.

Le serveur crée deux objets `Player` pour représenter les deux joueurs dans le jeu. Ces objets définissent la position initiale, la couleur, la taille et d'autres attributs des joueurs. Le serveur envoie ces objets au client pour l'initialisation.

Le serveur utilise des threads pour gérer les connexions des deux joueurs de manière concurrente. Chaque thread est responsable de la communication avec un joueur spécifique. Lorsqu'un joueur envoie ses données de déplacement, le serveur les reçoit, les désérialise à l'aide de "pickle", met à jour l'objet `Player` correspondant, puis renvoie les données du joueur adverse.

Les clients utilisent également la classe `Network` pour communiquer avec le serveur. Lorsque le client démarre, il se connecte au serveur, reçoit les données initiales du joueur et les stocke dans son propre objet `Player`. Le client utilise la classe `Network` pour envoyer ses données de déplacement au serveur et recevoir les données du joueur adverse.

#### Utilisation de la bibliothèque "pickle" dans le projet

##### Sérialisation et Désérialisation

La bibliothèque "pickle" est utilisée dans ce projet pour la sérialisation et la désérialisation des objets Python. Voici comment cela fonctionne :

- **Sérialisation :** Lorsqu'un objet Python doit être envoyé d'un client à un serveur ou vice versa, ou même lorsqu'il doit être stocké sur le disque, il est sérialisé en une représentation binaire. "pickle" est utilisé pour accomplir cette tâche. Par exemple, dans le projet, les objets `Player` sont sérialisés avant d'être envoyés au serveur pour initialisation.

    ```python
    # Sérialisation d'un objet avec pickle
    player_data = pickle.dumps(player_object)
    ```

- **Désérialisation :** Lorsque les données binaires sont reçues par l'autre partie (par exemple, le serveur), elles doivent être désérialisées pour reconstituer l'objet Python d'origine. "pickle" est également utilisé pour cette étape. Par exemple, dans le projet, le serveur reçoit les données binaires et les désérialise pour obtenir l'objet `Player`.

    ```python
    # Désérialisation d'un objet avec pickle
    player_object = pickle.loads(player_data)
    ```

##### Utilisation dans la classe Network

La classe `Network` dans le projet contient des méthodes pour la sérialisation et la désérialisation des données échangées entre les clients et le serveur. Voici comment "pickle" est utilisé dans cette classe :

- La méthode `send` est utilisée pour envoyer des données depuis un client vers le serveur. Elle sérialise les données avec "pickle" avant de les envoyer.

    ```python
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)
    ```

- La méthode `connect` est utilisée pour recevoir des données du serveur. Elle reçoit d'abord les données sous forme binaire, puis les désérialise avec "pickle" pour obtenir l'objet d'origine.

    ```python
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    ```

##### Sécurité et Limitations

Il est important de noter que "pickle" peut être puissant, mais il doit être utilisé avec précaution, car il peut exécuter du code arbitraire lors de la désérialisation. Cela signifie que lors de l'utilisation de "pickle", il faut s'assurer que les données proviennent de sources de confiance, car des données malveillantes pourraient potentiellement causer des problèmes de sécurité.

De plus, "pickle" n'est pas adapté à la sérialisation d'objets destinés à être partagés entre différentes versions de Python, car les formats de sérialisation peuvent varier entre les versions. Dans ce projet, la communication est réalisée entre des clients et un serveur Python, ce qui simplifie la compatibilité.

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

