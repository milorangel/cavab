import pygame
import math
import pygame.time
from random import randint


class Player(pygame.sprite.Sprite):
    pre_positions = []
    positions = []
    instances = []
    spawn_rect = 100

    def __init__(self, surface, color=(0, 0, 254), k_left=pygame.K_q,  k_right=pygame.K_d, k_boost=pygame.K_z, k_speedup=pygame.K_s):
        super().__init__()
        Player.instances.append(self)
        self.instance_number = len(Player.instances)
        print('Player instance:', self.instance_number, '-> init...' )

        self.surface = surface

        self.x = randint(Player.spawn_rect, self.surface.get_size()[0] - Player.spawn_rect)
        self.y = randint(Player.spawn_rect, self.surface.get_size()[1] - Player.spawn_rect)

        self.x_collision = self.x
        self.y_collision = self.y

        self.pixel_nb_for_move = self.speedup = 1
        self.angle = randint(0, 359)
        self.angle_force = 0.04

        self.k_left = k_left
        self.k_right = k_right
        self.k_boost = k_boost
        self.k_speedup = k_speedup

        self.jumping = False
        self.color = color

        self.boost_duration = 1000
        self.boost_delay = self.boost_duration + 1000
        self.last_speedup_time = self.last_boost_time = -self.boost_delay

        self.jump_positions = []

    def draw(self):
        if self.jumping:
            color = pygame.Color(self.color[0]//2, self.color[1]//2, self.color[2]//2)
        else:
            color = pygame.Color(self.color)
        pygame.draw.circle(self.surface, color, (int(self.x), int(self.y)), 2)

    def control(self, keys):
        if pygame.time.get_ticks() - self.last_speedup_time >= self.boost_duration:
            self.speedup = 1
        if keys[self.k_speedup] and pygame.time.get_ticks() - self.last_speedup_time >= self.boost_delay:
            self.last_speedup_time = pygame.time.get_ticks()
            self.speedup = 2

        if keys[self.k_left]:
            self.angle -= self.angle_force
        if keys[self.k_right]:
            self.angle += self.angle_force

        for _ in range(self.speedup):
            dx = self.pixel_nb_for_move * math.cos(self.angle)
            dy = self.pixel_nb_for_move * math.sin(self.angle)

            self.x += dx
            self.y += dy

            self.x_collision = round(self.x, 0)
            self.y_collision = round(self.y, 0)
            if self.jumping:
                self.jump_positions.append((self.x, self.y))
            else:
                if any((self.x_collision, self.y_collision) == pos for pos in Player.positions):
                    return True
                else:
                    Player.pre_positions.append((self.x_collision, self.y_collision))
                    if len(Player.pre_positions) > 10:
                        Player.positions.append(Player.pre_positions[0])
                        Player.pre_positions.remove(Player.pre_positions[0])

    def wall_collisions(self):
        if self.x < 0 or self.y < 0:
            return True
        if self.x > self.surface.get_size()[0] or self.y > self.surface.get_size()[1]:
            return True

    def jump(self, keys):
        if pygame.time.get_ticks() - self.last_boost_time >= self.boost_duration:
            self.jumping = False
        if not self.jumping and self.jump_positions != []:
            center = (int(self.jump_positions[0][0]), int(self.jump_positions[0][1]))
            pygame.draw.circle(self.surface, pygame.Color(0, 0, 0), center, 2)
            self.jump_positions.pop(0)
        if keys[self.k_boost] and pygame.time.get_ticks() - self.last_boost_time >= self.boost_delay:
            self.last_boost_time = pygame.time.get_ticks()
            self.jumping = True
