import pygame
import math
import pygame.time
from random import randint

class Player(pygame.sprite.Sprite):
    pre_positions = []
    positions = []
    instances = []
    spawn_rect = 100

    def __init__(self, surface, color=(0, 0, 254), k_left=pygame.K_q,  k_right=pygame.K_d, k_boost=pygame.K_z, k_speedup=pygame.K_s, k_double=pygame.K_f):
        super().__init__()
        Player.instances.append(self)
        self.instance_number = len(Player.instances)
        print('Player instance:', self.instance_number, '-> init...')

        self.surface = surface

        self.new_pos()

        self.x_collision = self.x
        self.y_collision = self.y

        self.pixel_nb_for_move = self.speedup = 1
        self.angle = randint(0, 359)
        self.angle_force = 0.04

        self.k_left = k_left
        self.k_right = k_right
        self.k_boost = k_boost
        self.k_speedup = k_speedup
        self.k_double = k_double

        self.double = False
        self.double_x = self.x
        self.double_y = self.y
        self.double_positions = 

        self.jumping = False
        self.color = color

        self.boost_duration = 1000
        self.boost_delay = self.boost_duration + 1000
        self.last_speedup_time = self.last_boost_time = -self.boost_delay

        self.jump_positions = []

    def new_pos(self):
        self.x = randint(Player.spawn_rect, self.surface.get_size()[0] - Player.spawn_rect)
        self.y = randint(Player.spawn_rect, self.surface.get_size()[1] - Player.spawn_rect)
    def draw(self):

        if self.jumping:
            color = pygame.Color(self.color[0]//2, self.color[1]//2, self.color[2]//2)
        else:
            color = pygame.Color(self.color)
        pygame.draw.circle(self.surface, color, (int(self.x), int(self.y)), 2)
        if self.double:
            pygame.draw.circle(self.surface, color, (int(self.double_x), int(self.double_y)), 2)
    def control(self, keys):

        # speed up control
        if pygame.time.get_ticks() - self.last_speedup_time >= self.boost_duration:
            self.speedup = 1
        if keys[self.k_speedup] and pygame.time.get_ticks() - self.last_speedup_time >= self.boost_delay:
            self.last_speedup_time = pygame.time.get_ticks()
            self.speedup = 2

        # control
        if keys[self.k_left]:
            self.angle -= self.angle_force*self.speedup
        if keys[self.k_right]:
            self.angle += self.angle_force*self.speedup
        if keys[self.k_double]:
            self.double = True

        for _ in range(self.speedup):

            if self.double:
                self.double_angle = 0.2
            else:
                self.double_angle = 0

            dx = self.pixel_nb_for_move * math.cos(self.angle+self.double_angle)
            dy = self.pixel_nb_for_move * math.sin(self.angle+self.double_angle)
            self.x += dx
            self.y += dy

            self.collision(round(self.x, 0), round(self.y, 0), self.positions)

            if self.double:
                double_dx = self.pixel_nb_for_move * math.cos(self.angle - self.double_angle)
                double_dy = self.pixel_nb_for_move * math.sin(self.angle - self.double_angle)
                self.double_x += double_dx
                self.double_y += double_dy

                self.collision(round(self.double_x, 0), round(self.double_y, 0), self.double_positions)
            else:
                self.double_x = self.x
                self.double_y = self.y


    def collision(self, x, y, positions):
        if self.jumping:
            self.jump_positions.append((x, y))
        else:
            if any((x, y) == pos for pos in positions):
                return True
            else:
                Player.pre_positions.append((x, y))
                if len(Player.pre_positions) > 10:
                    Player.positions.append(Player.pre_positions[0])
                    Player.pre_positions.remove(Player.pre_positions[0])
        self.draw()

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
