import pygame
import player

pygame.init()

def home(n):
    pygame.init()  # Initialisez la bibliothèque Pygame
    p = n.getP()
    width, height = 500, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Home Page")
    
    # Chargement de l'image d'arrière-plan
    background = pygame.image.load('Tron.jpg')
    background = pygame.transform.scale(background, (width, height))

    # Paramètres du bouton
    font = pygame.font.Font(None, 48)  # Agrandissez la police
    btn_width, btn_height = 200, 60  # Nouvelle taille
    btn_x = (width - btn_width) // 2  # Centre le bouton horizontalement
    btn_y = int(height * 0.75)  # Positionne le bouton un peu plus bas
    btn_rect = pygame.Rect(btn_x, btn_y, btn_width, btn_height)

    run = True
    clicked = False

    while run:
        win.blit(background, (0, 0))  # Affichage de l'arrière-plan

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_rect.collidepoint(event.pos) and not clicked:
                    clicked = True
                    p.ready = True  # Mettre à jour l'état de prêt du joueur
                    other_player_ready = n.send(p)  # Envoyer l'état actuel du joueur au serveur et attendre la réponse

                    # Vérifiez si l'autre joueur est prêt
                    if other_player_ready:
                        run = False

        if clicked:
            message_font = pygame.font.Font(None, 32)
            message = message_font.render("Attendez que l'autre joueur soit prêt...", True, (255, 255, 255))
            win.blit(message, (width // 2 - message.get_width() // 2, height // 2 - message.get_height() // 2))
            # Vérification périodique pour voir si l'autre joueur est prêt
            other_player_ready = n.send(p)
            if other_player_ready:
                run = False


        else:
            #pygame.draw.rect(win, (0, 0, 0), btn_rect)
            btn_text = font.render("PLAY", True, (255, 255, 255))
            text_width, text_height = font.size("PLAY")
            text_x = (width - text_width) // 2
            text_y = btn_y + (btn_height - text_height) // 2
            win.blit(btn_text, (text_x, text_y))
        
        pygame.display.update()

    
    return clicked

if __name__ == "__main__":
    home()
