import pygame

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Пианино")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Загрузка звуков нот
notes = {
    'C': pygame.mixer.Sound("C.wav"),
    'D': pygame.mixer.Sound("D.wav"),
    'E': pygame.mixer.Sound("E.wav"),
    'F': pygame.mixer.Sound("F.wav"),
    'G': pygame.mixer.Sound("G.wav"),
    'A': pygame.mixer.Sound("A.wav"),
    'B': pygame.mixer.Sound("B.wav"),
}

# Клавиши пианино
keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
key_width = screen_width // len(keys)
key_height = screen_height

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                notes['C'].play()
            if event.key == pygame.K_s:
                notes['D'].play()
            if event.key == pygame.K_d:
                notes['E'].play()
            if event.key == pygame.K_f:
                notes['F'].play()
            if event.key == pygame.K_g:
                notes['G'].play()
            if event.key == pygame.K_h:
                notes['A'].play()
            if event.key == pygame.K_j:
                notes['B'].play()

    # Отрисовка экрана
    screen.fill(GRAY)

    # Отрисовка клавиш пианино
    for i, key in enumerate(keys):
        pygame.draw.rect(screen, WHITE, (i * key_width, 0, key_width, key_height), 0)
        pygame.draw.rect(screen, BLACK, (i * key_width, 0, key_width, key_height), 2)

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
