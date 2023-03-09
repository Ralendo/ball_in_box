import pygame
import src.calculation as calculation

clock = pygame.time.Clock()

def events(screen, ball, cursor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Program finished..')
            pygame.mixer_music.stop()
            pygame.quit()
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                t = pygame.time.get_ticks()
                charging_bar(cursor, t, ball, screen)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ball = game_restart(screen, ball)
    return True, ball


def update(bg, screen, objects, FPS, space, draw_options, text, cursor):
    screen.blit(bg, (0, 0))
    screen.blit(text, (20, 20))

    cursor_img, cursor_img_rect = cursor[0], cursor[1]
    cursor_img_rect.center = pygame.mouse.get_pos()
    screen.blit(cursor_img, cursor_img_rect)

    clock.tick(FPS)
    for obj in objects:
        obj.show_on_screen()
    space.step(1 / (FPS*2))
    # space.debug_draw(draw_options)
    pygame.display.flip()


# Считаем, сколько заряжается, и производим выстрел мячом
def charging_bar(cursor, t, ball, screen):
    charging = True
    mouse_x, mouse_y = pygame.mouse.get_pos()
    while charging:
        pygame.mouse.set_pos(mouse_x, mouse_y)
        # Время заряда
        time_press = pygame.time.get_ticks()
        power = (time_press - t) * 2 / 3
        if power > 2000:
            power = 1500
        max_power = 15

        # Угол выстрела
        line_attack = [ball.body.position, pygame.mouse.get_pos()]

        # Рисуем индикатор
        percentage = calculation.percentage(power/100, max_power)
        scale_cursor(cursor, percentage, screen)


        # bar.show_on_screen(percentage, -angle)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # Выстрел
                    attack = calculation.attack(line_attack, power)
                    ball.move(*attack)
                    charging = False
        pygame.display.flip()


# Увеличение курсора в соответствии с зарядом
def scale_cursor(cursor, step, screen):
    step = step*4

    cursor_img = cursor[0]
    cursor_img_size = cursor_img.get_size()
    cursor_img = pygame.transform.scale(cursor_img, ((cursor_img_size[0] * step), (cursor_img_size[1] * step)))
    cursor_img_rect = cursor_img.get_rect()
    cursor_img_rect.center = pygame.mouse.get_pos()

    screen.blit(cursor_img, cursor_img_rect)


# Рестарт
def game_restart(screen, ball):
    size_screen = screen.get_size()
    pos = (size_screen[0]/2, size_screen[1]/2)
    ball.stop_forces(pos)
    return ball










