import pygame
import src.controls as controls
import src.main_menu as mainmenu
from src.background_music import start_play_music, play_music
from src.ball import Ball
from src.walls import Walls
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False


size_screen = width, height = (1200, 600)
pygame.mixer.pre_init(44100, -16, 2, 512)
FPS = 60


def launch():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Ball in Box')
    icon = pygame.image.load('img/service/icon.png')
    pygame.display.set_icon(icon)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('img/service/clicks.png')
    cursor_img = pygame.transform.scale(cursor_img, (32,32))

    # Загрузка изображений
    bg_img = pygame.image.load('img/service/back.jpg')
    bg_img = pygame.transform.scale(bg_img, size_screen)

    name_img = pygame.image.load('img/service/name.png')
    # name_img = pygame.transform.scale(name_img, name_img.get)

    instruction_img = pygame.image.load('img/service/instruction.png')
    # instruction_img = pygame.transform.scale(instruction_img, (height * 0.3, width * 0.3))

    text_font = pygame.font.SysFont('Comic Sams MS', 45)
    restart_text = text_font.render('R - Рестарт', False, (0, 0, 0))

    images = (restart_text, bg_img, name_img, instruction_img, cursor_img)

    # Запуск музыки фоновой
    current_tracklist, tracklist, MUSIC_END = start_play_music()
    music_option = (tracklist, MUSIC_END)

    # Настройка Pymunk
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    space = pymunk.Space()
    space.gravity = 0, 500

    # Создаём границы экрана
    walls = Walls(screen, space, size_screen)
    objects = [walls]

    backback = (screen, space)
    game_options = (images, music_option, objects, draw_options, backback)
    return game_options, current_tracklist


def main_menu(options, current_tracklist):
    images, music_option, objects, draw_options, backback = options
    _, bg_img, name_img, instruction_img, cursor_img = images
    tracklist, MUSIC_END = music_option
    screen, space = backback

    cursor_img_rect = cursor_img.get_rect()
    cursor = [cursor_img, cursor_img_rect]
    ball = None
    # Main menu
    start_begin = False
    while not start_begin:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pos_mouse = pygame.mouse.get_pos()
                    ball = Ball(screen, space, pos_mouse)
                    objects.append(ball)
                    return ball, current_tracklist
            if event.type == pygame.QUIT:
                print('Program finished..')
                pygame.mixer_music.stop()
                start_begin = True
                pygame.quit()

        current_tracklist = play_music(current_tracklist, tracklist, MUSIC_END)
        mainmenu.update(screen, FPS, bg_img, name_img, instruction_img, cursor)


def game_start(options, ball, current_tracklist):
    images, music_option, objects, draw_options, backback = options
    restart_text, bg_img, name_img, instruction_img, cursor_img = images
    tracklist, MUSIC_END = music_option
    screen, space = backback

    cursor_img_rect = cursor_img.get_rect()
    cursor = [cursor_img, cursor_img_rect]
    # Game
    while True:
        current_tracklist = play_music(current_tracklist, tracklist, MUSIC_END)
        controls.update(bg_img, screen, objects, FPS, space, draw_options, restart_text, cursor)
        check, ball = controls.events(screen, ball, cursor)
        if not check:
            break


options, tracklist = launch()
ball, tracklist = main_menu(options, tracklist)
game_start(options, ball, tracklist)

