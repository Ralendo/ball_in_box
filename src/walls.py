import pymunk
import pygame

class Walls:
    def __init__(self, screen, space, resolution):
        width, height = resolution
        self.width_screen = width
        self.height_screen = height
        thickness = 15
        self.thickness = thickness
        elasticity = 1
        friction = 1
        color = (0, 0, 0, 0)

        self.screen = screen
        self.up_square = pymunk.Poly(space.static_body, [(0, 0), (0, thickness), (width, 0), (width, thickness)])
        self.down_square = pymunk.Poly(space.static_body,
                                  [(0, height), (0, height - thickness), (width, height - thickness), (width, height)])
        self.left_square = pymunk.Poly(space.static_body, [(0, 0), (0, height), (thickness, 0), (thickness, height)])
        self.right_square = pymunk.Poly(space.static_body,
                                   [(width - thickness, 0), (width, 0), (width - thickness, height), (width, height)])
        self.objects = [self.right_square, self.up_square, self.left_square, self.down_square]
        for obj in self.objects:
            obj.color = color
            obj.elasticity = elasticity
            obj.friction = friction
            space.add(obj)
        print('Walls has been created..')

    def show_on_screen(self):
        # Left side
        pygame.draw.line(self.screen, 'Black', (0, 0), (0, self.height_screen), self.thickness)
        # Upside
        pygame.draw.line(self.screen, 'Black', (0, 0), (self.width_screen, 0), self.thickness)
        # Right side
        pygame.draw.line(self.screen, 'Black', (self.width_screen, 0), (self.width_screen, self.height_screen), self.thickness)
        # Downside
        pygame.draw.line(self.screen, 'Black', (0, self.height_screen), (self.width_screen, self.height_screen), self.thickness)