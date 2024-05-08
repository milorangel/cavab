import pygame
import pygame.time
import player
pygame.init()

sc_size = 1200, 600
sc_center = sc_size[0]/2, sc_size[1]/2
sc = pygame.display.set_mode(sc_size)
pygame.display.set_caption("ça va b ?")

sc.fill(pygame.Color(0,0,0))

def main():
    players =[player.Player(sc), player.Player(sc, (254, 50, 254), pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)]#, player.Player(sc, (50, 254, 50), pygame.K_b, pygame.K_n, pygame.K_h)]

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        keys = pygame.key.get_pressed()
        for p in players:
            p.jump(keys)
            if p.control(keys) or p.wall_collisions():
                running = False
                break

            p.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


    pygame.quit()

main()