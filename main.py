import pygame
import pygame.time
import player
pygame.init()

sc_size = 600, 400
sc_center = sc_size[0]/2, sc_size[1]/2
sc = pygame.display.set_mode(sc_size)
pygame.display.set_caption("ça va b ? ça va bou?")

sc.fill('#000000')

def main():

    players =[player.Player(100, 100, sc), player.Player(0, 0, sc, 'pink', pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)]

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for p in players:
            p.control()


            if not p.players_collisions() :  # Si p.control() renvoie False, la boucle s'arrête
                running = False
                break

            p.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

main()

