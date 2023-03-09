import pygame
import pymunk


class Ball:
    def __init__(self, screen, space, pos):
        radius = 42
        mass = 5
        self.body = pymunk.Body()
        self.body.type = pymunk.Body.DYNAMIC
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.mass = mass
        self.shape.density = 1
        self.shape.elasticity = 0.8
        space.add(self.body, self.shape)

        self.screen = screen
        self.image = pygame.image.load('img/ball/ball.png')
        resolution = (50, 50)
        self.image = pygame.transform.scale(self.image, resolution)
        print('Ball has been created..')

    def show_on_screen(self):
        # Вывод на экран Шара
        self.screen.blit(self.image, self.body.position)

    def move(self, attack_fx, attack_fy):
        # Передвижение шара
        self.body.apply_impulse_at_local_point((attack_fx, attack_fy), (0, 0))

    def stop_forces(self, pos):
        # Прожата кнопка Рестарта
        self.body.position = pos
        self.body.force = 0, 0
        self.body.torque = 0
        self.body.velocity = 0, 0
        self.body.angular_velocity = 0

