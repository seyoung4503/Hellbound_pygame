import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


TILE_WIDTH = 64
TILE_HEIGHT = 32
MAP_WIDTH = 10
MAP_HEIGHT = 10

map_data = [[(x + y) % 2 for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

def draw_iso_tile(x, y):
    # iso_x = (x - y) * TILE_WIDTH // 2 + 400
    # iso_y = (y + x) * TILE_HEIGHT // 2 + 50
    iso_x = (x + y) * TILE_WIDTH // 2  + 400
    iso_y = 0.5 * (-x + y) * TILE_HEIGHT + 50

    # screen, color, coordinate
    pygame.draw.polygon(screen, (100, 200, 100), [
        # (iso_x, iso_y),
        # (iso_x + TILE_WIDTH // 2, iso_y + TILE_HEIGHT // 2),
        # (iso_x, iso_y + TILE_HEIGHT),
        # (iso_x - TILE_WIDTH //2, iso_y + TILE_HEIGHT // 2)

        
        
        (iso_x + TILE_WIDTH // 2, iso_y + TILE_HEIGHT // 2),
        (iso_x, iso_y + TILE_HEIGHT),
        (iso_x - TILE_WIDTH //2, iso_y + TILE_HEIGHT // 2),
        (iso_x, iso_y)
    ])



while True:
    screen.fill((0, 0, 0))

    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            draw_iso_tile(x, y)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

