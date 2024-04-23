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

    players =[player.Player(sc_center), (player.Player((sc_center[0]-50, sc_center[1]-50), 'pink', pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP))]


    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i, p in enumerate(players):
            p.control()
            # p.jump()  # Maybe you commented this out intentionally?
            p.draw(sc)
            if i > 0:
                prev_player = players[i - 1]
                for pos in p.positions:
                    if prev_player.position == pos:
                        running = False

        pygame.display.flip()

    pygame.quit()


main()
