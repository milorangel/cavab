import pygame
import pygame.time
import player
import btn
pygame.init()

sc_size = 1200, 600
sc_center = sc_size[0] / 2, sc_size[1] / 2
sc = pygame.display.set_mode(sc_size)
pygame.display.set_caption("Savab - SIX*4TH")
sc.fill(pygame.Color(0, 0, 0))


def main():
    playing = True

    player.Player(sc)
    player.Player(sc, (254, 50, 50), pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RSHIFT)

    button1 = btn.Button(sc_center, caption='STAR', scale=7)

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            playing = not playing

        if playing:
            for p in player.Player.instances:
                p.jump(keys)
                if p.control(keys) or p.wall_collisions():
                    playing = False
                    break

        else:
            sc.fill(pygame.Color(0, 0, 0))
            for p in player.Player.instances:
                p.new_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()

    pygame.quit()


main()
