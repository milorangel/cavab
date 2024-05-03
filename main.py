import pygame
import pygame.time
import player
pygame.init()

sc_size = 600, 400
sc_center = sc_size[0]/2, sc_size[1]/2
sc = pygame.display.set_mode(sc_size)
pygame.display.set_caption("ça va b ? ça va bou?")

sc.fill(pygame.Color(0,0,0))

def main():

    players =[player.Player(100, 100, sc), player.Player(0, 0, sc, pygame.Color(255, 51, 255), pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)]

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        keys = pygame.key.get_pressed()
        for p in players:
            p.control(keys)
            #p.jump(keys)


            if p.players_collisions() or p.wall_collisions():  # Si p.control() renvoie False, la boucle s'arrête
                running = False
                break

            p.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

main()