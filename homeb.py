import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("탄막 피하기")

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 플레이어 설정
player_width = 50
player_height = 50
player = pygame.Rect(SCREEN_WIDTH // 2 - player_width // 2, SCREEN_HEIGHT - 2 * player_height, player_width, player_height)
player_speed = 5  # 플레이어 이동 속도

# 총알 설정
bullet_width = 5
bullet_height = 15
bullets = []

# 초록색 탄막 설정
green_bullet_width = 10
green_bullet_height = 20
green_bullets = []

# 체력 및 점수 설정
health = 5
score = 0
level = 1
score_font = pygame.font.SysFont(None, 36)

# 시간 설정
elapsed_time = 0
level_change_time = 5  # 레벨 변경 간격 (초)
level_change_timer = level_change_time

# 스코어 증가 속도 및 레벨 업 속도 조정
score_increase_speed = 1  # 1초에 스코어가 증가하는 양
level_increase_speed = 5  # 5초에 한 번 레벨이 증가

# 게임 루프
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += player_speed

    # 총알 생성
    if random.randint(1, 13) == 1:
        bullet_color = RED
        if random.randint(1, 10) == 1:
            bullet_color = YELLOW
        bullet = pygame.Rect(random.randint(0, SCREEN_WIDTH - bullet_width), 0, bullet_width, bullet_height)
        bullets.append((bullet, bullet_color))

    # 초록색 탄막 생성
    if random.randint(1, 20) == 1:
        green_bullet = pygame.Rect(random.randint(0, SCREEN_WIDTH - green_bullet_width), 0, green_bullet_width, green_bullet_height)
        green_bullets.append(green_bullet)

    # 총알 이동 및 충돌 처리
    for bullet, color in bullets:
        bullet.y += 7
        pygame.draw.rect(screen, color, bullet)
        if bullet.colliderect(player):
            if color == YELLOW:
                score += 10
            else:
                health -= 1
            bullets.remove((bullet, color))
        if bullet.y > SCREEN_HEIGHT:
            bullets.remove((bullet, color))

    # 초록색 탄막 이동 및 충돌 처리
    for green_bullet in green_bullets:
        green_bullet.y += 5
        pygame.draw.rect(screen, GREEN, green_bullet)
        if green_bullet.colliderect(player):
            health -= 2
            green_bullets.remove(green_bullet)
        if green_bullet.y > SCREEN_HEIGHT:
            green_bullets.remove(green_bullet)

    # 점수 증가
    elapsed_time += clock.get_rawtime() / 1000
    if elapsed_time >= 1:  # 1초마다 스코어를 증가시킵니다.
        score += score_increase_speed
        elapsed_time = 0

    # 레벨 변경
    level_change_timer -= clock.get_rawtime() / 1000
    if level_change_timer <= 0:
        level += 1
        level_change_timer = level_change_speed

    # 플레이어 그리기
    pygame.draw.rect(screen, BLUE, player)

    # 체력, 점수 및 레벨 표시
    health_text = score_font.render(f"Health: {health}", True, RED)
    screen.blit(health_text, (10, 10))
    score_text = score_font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 40))
    
    # 레벨 표시 (매 프레임마다 갱신되도록 함)
    level_text = score_font.render(f"Level: {level}", True, RED)
    screen.blit(level_text, (10, 70))

    # 체력이 0이 되면 게임 종료
    if health <= 0:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
