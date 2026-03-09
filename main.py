import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill("black")

        for p in drawable:
            p.draw(screen)

        updatable.update(dt)
        pygame.display.update()


if __name__ == "__main__":
    main()
