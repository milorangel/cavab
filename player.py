import pygame
import math

class Player(pygame.sprite.Sprite):
    positions = []
    def __init__(self, position, color='blue', k_left = pygame.K_q,  k_right = pygame.K_d, k_boost = pygame.K_z):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        Player.positions.append(position)

        self.speed = 1
        self.angle = self.spawn_angle = 0
        self.angle_force = 0.04

        self.k_left = k_left
        self.k_right = k_right
        self.k_boost = k_boost

        self.visible = True
        self.color = color

        self.k_boost_pressed = False
        self.constant_boost_duration = self.boost_duration = 30
        self.constant_boost_cooldown = self.boost_cooldown = 30
        self.boost_on = False
        self.boost_cooldown_done = True





    def draw(self, surface):
        if self.visible:
            color = self.color
        else:
            color = 'white'
        pygame.draw.circle(surface, color, (self.x, self.y), 1)

    def control(self):
        keys = pygame.key.get_pressed()

        if keys[self.k_left]:
            self.angle -= self.angle_force
        if keys[self.k_right]:
            self.angle += self.angle_force


        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)

        self.x += dx
        self.y += dy
        self.position = (self.x, self.y)
        Player.positions.append(self.position)



    def jump(self):
        keys = pygame.key.get_pressed()

        # Si le cooldown du boost est terminé, le joueur peut activer le boost
        if self.boost_cooldown_done:
            if keys[self.k_boost]:
                self.boost_on = True

        # Si le boost est activé, réduire la durée du boost
        if self.boost_on:
            self.visible = False
            self.boost_duration -= 1

        # Si la durée du boost est écoulée, désactiver le boost et démarrer le cooldown
        if self.boost_duration < 0:
            self.boost_on = False
            self.boost_cooldown_done = False  # Le cooldown n'est pas encore terminé
            self.boost_cooldown = self.constant_boost_cooldown  # Réinitialiser le cooldown du boost

        # Si le cooldown du boost est en cours, réduire son temps
        if not self.boost_cooldown_done:
            self.boost_cooldown -= 1
            if self.boost_cooldown <= 0:
                self.boost_cooldown_done = True  # Indiquer que le cooldown est terminé

        # Réinitialiser le déclencheur du boost après que le cooldown soit terminé
        if self.boost_cooldown_done and not keys[self.k_boost]:
            self.boost_on = False

        # Rendre le joueur visible si aucune touche de déplacement n'est enfoncée et que le boost n'est pas activé
        if not any([keys[self.k_left], keys[self.k_right]]) and not self.boost_on:
            self.visible = True

