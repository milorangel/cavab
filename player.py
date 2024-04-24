import pygame
import math


class Player(pygame.sprite.Sprite):
    pre_positions = []
    positions = []
    instance_len = 0
    def __init__(self, x, y, surface, color='blue', k_left = pygame.K_q,  k_right = pygame.K_d, k_boost = pygame.K_z):
        super().__init__()
        Player.instance_len += 1
        self.instance_number = Player.instance_len
        print('Player instance:', self.instance_number, '-> init...' )
        self.x = x
        self.y = y
        self.surface = surface

        self.speed = 1
        self.angle = self.spawn_angle = 0
        self.angle_force = 0.04

        self.k_left = k_left
        self.k_right = k_right
        self.k_boost = k_boost

        self.visible = True
        self.color = color

        #self.k_boost_pressed = False
        #self.constant_boost_duration = self.boost_duration = 30
        #self.constant_boost_cooldown = self.boost_cooldown = 30
        #self.boost_on = False
        #self.boost_cooldown_done = True

    def draw(self):
        if self.visible:
            color = self.color
        else:
            color = 'white'
        pygame.draw.circle(self.surface, color, (self.x, self.y), 2)

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


    def players_collisions(self):
        self.x = round(self.x, 0)
        self.y = round(self.y, 0)

        if any((self.x, self.y) == pos for pos in Player.positions):
            print(False)
            return False
        else:
            Player.pre_positions.append((self.x, self.y))
            if len(Player.pre_positions) > 10:
                Player.positions.append(Player.pre_positions[0])
                Player.pre_positions.remove(Player.pre_positions[0])
            return True
    def wall_collisions(self):
        if self.x > self.surface.get_size()[0]:
            return False

        # --------------------------------------------------------------------------
        #player_rect = pygame.Rect(self.x, self.y, 1, 1)
        #for pos in Player.positions:
        #    pos_rect = pygame.Rect(pos[0], pos[1], 1, 1)
        #    if player_rect.colliderect(pos_rect):
        #        print("Collision detected!")
        #        return False
        # -------------------------------------------------------------------
        # if surface.get_at((int(self.x), int(self.y))) != '#000000':
        #    return False
        # return True


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

