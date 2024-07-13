import pygame
import random

# 게임 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슈팅 게임")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 플레이어 설정
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# 적 설정
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(0, screen_height // 2)
enemy_speed = 3

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 화면 경계 처리
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    elif player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # 적 이동
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_y = random.randint(-100, -40)
        enemy_x = random.randint(0, screen_width - enemy_width)

    # 화면 업데이트
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.flip()

    # FPS 설정
    pygame.time.Clock().tick(60)

pygame.quit()
