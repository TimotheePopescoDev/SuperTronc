import pygame

class Player:
    def __init__(self, x, y, width, height, color, win_width, win_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 5
        self.direction = "right"
        self.win_width = win_width
        self.win_height = win_height

        # Nouveaux attributs pour la traînée
        self.trail = []  # Liste pour stocker les positions précédentes
        self.trail_color = color  # Couleur de la traînée

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        # Enregistre la position précédente
        self.trail.append((self.x, self.y))

        if self.direction == "right":
            self.x += self.vel
        elif self.direction == "left":
            self.x -= self.vel
        elif self.direction == "up":
            self.y -= self.vel
        elif self.direction == "down":
            self.y += self.vel

        # Gère les collisions avec les bords de la fenêtre
        if self.x < 0:
            self.x = 0
        if self.x + self.width > self.win_width:
            self.x = self.win_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > self.win_height:
            self.y = self.win_height - self.height

        # Gère la longueur de la traînée (par exemple, en supprimant les positions plus anciennes)
        max_length_of_trail = 50  # Vous pouvez ajuster cette valeur
        if len(self.trail) > max_length_of_trail:
            del self.trail[0]  # Supprime la position la plus ancienne

        
        self.update()

    def draw_trail(self, win):
        for pos in self.trail:
            pygame.draw.rect(win, self.trail_color, (pos[0], pos[1], self.width, self.height))

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def set_direction(self, direction):
        if (direction == "right" and self.direction != "left") or \
           (direction == "left" and self.direction != "right") or \
           (direction == "up" and self.direction != "down") or \
           (direction == "down" and self.direction != "up"):
            self.direction = direction
