import pygame
import random

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avoid the Falling Blocks!")

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Переменные для игрока
player_size = 50
player_x = screen_width // 2
player_y = screen_height - 2 * player_size
player_speed = 10

# Переменные для препятствий
block_size = 50
block_speed = 13
block_list = []

# Функция для создания блоков
def create_block():
    x = random.randint(0, screen_width - block_size)
    y = 0 - block_size
    block_list.append([x, y])

# Функция для обновления положения блоков
def update_blocks():
    for block in block_list:
        block[1] += block_speed
        if block[1] > screen_height:
            block_list.remove(block)

# Функция для проверки столкновений
def detect_collision(player_pos, block_pos):
    p_x, p_y = player_pos
    b_x, b_y = block_pos

    if (b_x < p_x < b_x + block_size or b_x < p_x + player_size < b_x + block_size) and \
            (b_y < p_y < b_y + block_size or b_y < p_y + player_size < b_y + block_size):
        return True
    return False

# Главный игровой цикл
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Создание блоков
    if random.randint(1, 20) == 1:
        create_block()

    # Обновление положения блоков
    update_blocks()

    # Проверка на столкновения
    for block in block_list:
        if detect_collision([player_x, player_y], block):
            game_over = True

    # Заливка фона
    screen.fill(WHITE)

    # Отрисовка игрока
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

    # Отрисовка блоков
    for block in block_list:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_size, block_size))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение кадров в секунду
    clock.tick(30)

pygame.quit()
