import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Стрелялки")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройки игры
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 7

bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullets = []

enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemies = []

score = 0
font = pygame.font.Font(None, 36)

# Таймер появления врагов
spawn_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy_event, 1000)

# Главный игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Создание нового врага
        if event.type == spawn_enemy_event:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemies.append([enemy_x, -enemy_height])

        # Выстрел
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Движение пуль
    bullets = [[x, y - bullet_speed] for x, y in bullets if y > 0]

    # Движение врагов
    enemies = [[x, y + enemy_speed] for x, y in enemies if y < screen_height]

    # Проверка на столкновение пуль и врагов
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Отрисовка экрана
    screen.fill(BLACK)

    # Отрисовка игрока
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Отрисовка пуль
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Отрисовка врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Отрисовка счета
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
