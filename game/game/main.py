import pygame

from game.settings.settings import WHITE, RECT, Click, FPS, BLACK

pygame.init()

WINDOW = pygame.display.set_mode((800, 600))

rect = pygame.draw.rect(WINDOW, WHITE, RECT)
font = pygame.font.Font('freesansbold.ttf', 32)
click = Click()


def draw_click_text():
    click.increment_value()
    text = font.render(f'Clicks: {click.value}', True, WHITE)
    WINDOW.blit(text, rect)


def draw_screen():
    WINDOW.fill(BLACK)

    draw_click_text()

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    text = font.render('Clicks: 0', True, WHITE)
    WINDOW.blit(text, rect)
    pygame.display.update()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                draw_screen()

            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
