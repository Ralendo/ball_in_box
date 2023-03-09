import pygame
import src.calculation as calculation

clock = pygame.time.Clock()
angle = 0
turn_side = 'left'
step = 1
step_command = 'increase'

# Рисуем название
def draw_start_name(screen, img, angle):
    w, h = img.get_size()
    w, h = w/2, h/2
    pos = (screen.get_width()/2, (screen.get_height()/2) - (screen.get_height() * 0.3))
    image_rect = img.get_rect(topleft=(pos[0] - w, pos[1] - h))
    offset_center = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(img, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    screen.blit(rotated_image, rotated_image_rect)

# Рисуем инструкцию
def draw_start_instruction(screen, img, step):
    # Анимация увеличения/уменьшения
    img_size = img.get_size()
    img_scale = pygame.transform.scale(img, ((img_size[0] * step), (img_size[1] * step)))

    # Ставим местоположение
    screen_size = screen.get_size()
    img_rect = img_scale.get_rect(center=(screen_size[0] / 2, screen_size[1] - 200))

    screen.blit(img_scale, img_rect)


def update(screen, FPS, bg, name_img, instruction_img, cursor):
    global angle, turn_side, step, step_command
    screen.blit(bg, (0, 0))

    cursor_img, cursor_img_rect = cursor[0], cursor[1]
    cursor_img_rect.center = pygame.mouse.get_pos()
    screen.blit(cursor_img, cursor_img_rect)
    # Рисуем текст главного меню c анимацией
    turn_side, angle = calculation.angle_round(turn_side, angle)
    draw_start_name(screen, name_img, angle)
    step, step_command = calculation.scale_img(step, step_command)
    draw_start_instruction(screen, instruction_img, step)
    #
    clock.tick(FPS)
    pygame.display.flip()

