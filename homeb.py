import pygame
import sys
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 벽돌 색상 리스트
BRICK_COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (255, 165, 0),  # 주황
    (255, 20, 147)  # 핑크
]

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("벽돌깨기")

# 패들 설정
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# 공 설정
BALL_SIZE = 10
BALL_SPEED = 5

# 벽돌 설정
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_PADDING = 5

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PADDLE_SPEED

        # 화면 경계에서 멈추기
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = BALL_SPEED * random.choice([1, -1])
        self.speed_y = BALL_SPEED * random.choice([1, -1])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 화면 경계에서 반사
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0:
            self.speed_y = -self.speed_y

        # 바닥에 닿으면 게임 오버
        if self.rect.y >= SCREEN_HEIGHT:
            pygame.quit()
            sys.exit()

    def bounce(self):
        self.speed_y = -self.speed_y

# 벽돌 클래스
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

ball = Ball()
all_sprites.add(ball)

# 벽돌 생성
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        color = random.choice(BRICK_COLORS)
        brick = Brick(
            col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_PADDING,
            row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_PADDING,
            color
        )
        all_sprites.add(brick)
        bricks.add(brick)

# 게임 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 업데이트
    all_sprites.update()

    # 공과 패들의 충돌 감지
    if pygame.sprite.collide_rect(ball, paddle):
        ball.bounce()

    # 공과 벽돌의 충돌 감지
    brick_collision_list = pygame.sprite.spritecollide(ball, bricks, True)
    if brick_collision_list:
        ball.bounce()

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
