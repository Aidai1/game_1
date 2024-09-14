import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Гонки")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# Машина игрока
player_width = 50
player_height = 100
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 7

# Вражеские машины
enemy_width = 50
enemy_height = 100
enemy_speed = 10
enemies = []

# Таймер появления врагов
spawn_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy_event, 1500)

# Счет
score = 0
font = pygame.font.Font(None, 36)

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Создание новых врагов
        if event.type == spawn_enemy_event:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemies.append([enemy_x, -enemy_height])

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Движение вражеских машин
    enemies = [[x, y + enemy_speed] for x, y in enemies if y < screen_height]

    # Проверка на столкновения
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        if player_rect.colliderect(enemy_rect):
            running = False  # Игра заканчивается при столкновении

    # Отрисовка экрана
    screen.fill(GRAY)

    # Отрисовка игрока
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Отрисовка врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Подсчет очков
    score += 1
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
