import pygame
import shape
import random

pygame.init()  # Khởi tạo

width = 360
rows = 30
columns = 15
size = width // columns  # Chia lấy nguyên
height = size * rows
screen = pygame.display.set_mode((width, height))
grid = [0]*columns*rows

picture = []  # Danh sách ảnh
for i in range(8):
    picture.append(pygame.transform.scale(
        pygame.image.load(f'./game/T_{i}.gif'), (size, size)))


def drawGrid(screen):
    WHITE = (255, 255, 255)
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*size, y*size,
                               size, size)
            pygame.draw.rect(screen, WHITE, rect, 1)


grid[20] = 4
# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((125, 125, 125))
    drawGrid(screen)
    for n, color in enumerate(shape.shapes[random.randint(0, 1)]):
        if color > 0:
            x = n % columns * size
            y = n // columns * size
            screen.blit(picture[color], (x, y))
    pygame.display.update()
