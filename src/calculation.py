import math
import pygame

# Угол вращения названия
def angle_round(turn_side, angle):
    max_angle = 15
    rotation = 0.8
    if turn_side == 'left':
        angle += rotation
        if angle > max_angle:
            turn_side = 'right'
    elif turn_side == 'right':
        angle -= rotation
        if angle < -max_angle:
            turn_side = 'left'
    return turn_side, angle

# Множитель изменения размера инструкции
def scale_img(x, command):
    step = 0.0065
    max_size = 1.1
    min_size = 0.9
    if command == 'increase':
        x += step
        if x > max_size:
            command = 'decrease'
    elif command == 'decrease':
        x -= step
        if x < min_size:
            command = 'increase'
    return x, command


# Вычисление угла выстрела
def corner_fire(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

# Вычисление дистанции выстрела:
def distance_fire(p1, p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

def attack(line_attack, power):
    angel = corner_fire(*line_attack)
    force = distance_fire(*line_attack) * power * 50
    fx = math.cos(angel) * force
    fy = math.sin(angel) * force
    return fx, fy

def radians_to_degrees(x):
    return math.degrees(x)

def percentage(part, full):
    return (100 * part / full) / 100



