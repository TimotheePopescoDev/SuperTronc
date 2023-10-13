import pygame

class Player:
    def __init__(self, x, y, width, height, color, trail_color, win_width, win_height, ready=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 4
        self.direction = "right"
        self.win_width = win_width
        self.win_height = win_height
        self.winner_name = ""
        self.game_over = False
        self.ready = ready
        
        # Nouveaux attributs pour la traînée
        self.trail = []  # Liste pour stocker les positions précédentes
        self.trail_color = trail_color # Couleur de la traînée

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        if not self.game_over:# Enregistre la position précédente
            self.trail.append((self.x, self.y))

            if self.direction == "right":
                self.x += self.vel
            elif self.direction == "left":
                self.x -= self.vel
            elif self.direction == "up":
                self.y -= self.vel
            elif self.direction == "down":
                self.y += self.vel

        # Gère la longueur de la traînée (par exemple, en supprimant les positions plus anciennes)
            max_length_of_trail = 150  # Vous pouvez ajuster cette valeur
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
    
    def has_exceeded_boundaries(self):
        return (
            self.x < 0 or
            self.x + self.width > self.win_width or
            self.y < 0 or
            self.y + self.height > self.win_height
        )
    
    def has_collided_with(self, other_player):
        # Vérifie s'il y a une collision avec l'autre joueur
        if self.rect.colliderect(other_player.rect):
            return True

        # Vérifie s'il y a une collision avec la traînée de l'autre joueur
        for pos in other_player.trail:
            if self.rect.colliderect(pygame.Rect(pos[0], pos[1], self.width, self.height)):
                return True

        return False
    
    def stop_move(self):
        # Arrête le mouvement en mettant la vitesse à 0
        self.vel = 0

    def check_game_over(self, other_player):
        if self.has_exceeded_boundaries() or self.game_over or self.has_collided_with(other_player) or self.check_self_collision():
            self.game_over = True
            return True
        return False

    def reset_player(player, x, y):
        player.x = x
        player.y = y
        player.direction = "right"
        player.game_over = False
        player.ready = False
        player.trail = []  # Réinitialisez la traînée

    def check_self_collision(self):
    # Vérifie la collision avec sa propre traînée
        if len(self.trail) > 40:  # Assurez-vous que la traînée a plus d'une case
            head_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            for pos in self.trail[:-10]:  # Parcourez la traînée à l'exception de la dernière case
                if head_rect.colliderect(pygame.Rect(pos[0], pos[1], self.width, self.height)):
                    self.game_over = True
                    return True
        return False

    


    
