import pygame
import sys
import random
import time
import ctypes

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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌깨기")

# 패들 설정
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# 공 설정
BALL_SIZE = 10
BALL_SPEED = 5
BALL_COUNT = 3

# 벽돌 설정
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_PADDING = 5

# 폰트 설정
font = pygame.font.Font(None, 74)

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

        # 바닥에 닿으면 공을 삭제
        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()

    def bounce(self):
        self.speed_y = -self.speed_y

# 벽돌 클래스
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color, shape):
        super().__init__()
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT], pygame.SRCALPHA)
        self.color = color
        self.shape = shape
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.draw_shape()

    def draw_shape(self):
        if self.shape == "rectangle":
            pygame.draw.rect(self.image, self.color, [0, 0, BRICK_WIDTH, BRICK_HEIGHT])
        elif self.shape == "triangle":
            pygame.draw.polygon(self.image, self.color, [(0, BRICK_HEIGHT), (BRICK_WIDTH / 2, 0), (BRICK_WIDTH, BRICK_HEIGHT)])

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
bricks = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

# 공 3개 생성
for _ in range(BALL_COUNT):
    ball = Ball()
    all_sprites.add(ball)
    balls.add(ball)

# 벽돌 생성
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        color = random.choice(BRICK_COLORS)
        shape = random.choice(["rectangle", "triangle"])
        brick = Brick(
            col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_PADDING,
            row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_PADDING,
            color,
            shape
        )
        all_sprites.add(brick)
        bricks.add(brick)

# 게임 루프
clock = pygame.time.Clock()

# 카운트다운 함수
def countdown(seconds):
    while seconds > 0:
        screen.fill(BLACK)
        countdown_text = font.render(str(seconds), True, WHITE)
        screen.blit(countdown_text, (SCREEN_WIDTH // 2 - countdown_text.get_width() // 2, SCREEN_HEIGHT // 2 - countdown_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        seconds -= 1

countdown(3)  # 3초 카운트다운

# 화면 위치 변경 함수
def move_window_randomly():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    new_x = random.randint(0, screen_width - SCREEN_WIDTH)
    new_y = random.randint(0, screen_height - SCREEN_HEIGHT)

    # Pygame 윈도우 위치를 변경
    user32.SetWindowPos(pygame.display.get_wm_info()['window'], None, new_x, new_y, 0, 0, 0x0001)

# 5초마다 화면 위치 변경 이벤트
MOVE_WINDOW_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_WINDOW_EVENT, 5000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOVE_WINDOW_EVENT:
            move_window_randomly()

    # 업데이트
    all_sprites.update()

    # 공과 패들의 충돌 감지
    for ball in balls:
        if pygame.sprite.collide_rect(ball, paddle):
            ball.bounce()

    # 공과 벽돌의 충돌 감지
    for ball in balls:
        brick_collision_list = pygame.sprite.spritecollide(ball, bricks, True)
        if brick_collision_list:
            ball.bounce()

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    # 남은 공이 없으면 게임 종료
    if len(balls) == 0:
        pygame.quit()
        sys.exit()
