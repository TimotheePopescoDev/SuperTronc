import pygame
from network import Network
from player import Player
from home import home
import sys

pygame.init()  # Initialisez Pygame au début du script
n = Network()
p = n.getP()
home(n)
pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))
    player.draw_trail(win)
    if player2 is not None:
        player2.draw_trail(win)
        player2.draw(win)
    player.draw(win)
    pygame.display.update()

def end_game_screen(win, result, n):
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    restart_btn = pygame.Rect(150, 250, 200, 50)
    quit_btn = pygame.Rect(150, 350, 200, 50)
    restart_text = font.render("Recommencer", True, (255, 255, 255))
    quit_text = font.render("Quitter", True, (255, 255, 255))

    while True:
        win.fill((255, 255, 255))

        if result == "win":
            message = font.render("Vous avez gagné!", True, (255, 255, 255))  
        else:
            message = font.render("Vous avez perdu!", True, (255, 255, 255))  
        # Charger l'image de fond
        background = pygame.image.load('Tron.jpg')
        background = pygame.transform.scale(background, (500, 500))
        win.blit(background, (0, 0))

        win.blit(message, (160, 50))
        pygame.draw.rect(win, (0, 255, 0), restart_btn)
        pygame.draw.rect(win, (255, 0, 0), quit_btn)

        # Centrer le texte dans les boutons
        win.blit(restart_text, (restart_btn.x + restart_btn.width // 2 - restart_text.get_width() // 2, restart_btn.y + restart_btn.height // 2 - restart_text.get_height() // 2))
        win.blit(quit_text, (quit_btn.x + quit_btn.width // 2 - quit_text.get_width() // 2, quit_btn.y + quit_btn.height // 2 - quit_text.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Le joueur a choisi de quitter
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    p.reset_player(50,50)  # Réinitialisez les caractéristiques du joueur local
                    n.send(p)  # Envoyez le joueur réinitialisé au serveur
                    return True  # Le joueur a choisi de recommencer
                if quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    return False  # Le joueur a choisi de quitter
        clock.tick(60)

def main():
    run = True
    
    clock = pygame.time.Clock()
    game_over_font = pygame.font.Font(None, 36)
    game_over_text = ""

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p.set_direction("left")
                elif event.key == pygame.K_RIGHT:
                    p.set_direction("right")
                elif event.key == pygame.K_UP:
                    p.set_direction("up")
                elif event.key == pygame.K_DOWN:
                    p.set_direction("down")

        p.move()

        # Vérification de la fin de partie pour le joueur local
        p.check_game_over(p2)

        if p.game_over:
            n.send(p)
            if end_game_screen(win, "lose", n):
                home(n)  
            else:
                run = False  # Quitter complètement le jeu

        p2.check_game_over(p)

        if p2.game_over:
            if end_game_screen(win, "win", n):
                home(n)  
            else:
                run = False  # Quitter complètement le jeu

        redrawWindow(win, p, p2)

    pygame.quit()

if __name__ == "__main__":
    main()
