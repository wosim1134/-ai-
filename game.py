import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("얼음 밀기 게임 - 지현우")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
ICE_COLOR = (173, 216, 230)
WALL_COLOR = (100, 100, 100)
TARGET_COLOR = (255, 100, 100)
CLEAR_COLOR = (0, 128, 0)

# 폰트
font = pygame.font.SysFont(None, 48)

# 게임 맵 정의 (여러 레벨)
levels = [
    [
        "########",
        "#   X  #",
        "#      #",
        "#  O   #",
        "#      #",
        "########"
    ],
    [
        "##########",
        "#   X    #",
        "#        #",
        "#    #   #",
        "#   O    #",
        "#        #",
        "##########"
    ]
]

current_level = 0
TILE_SIZE = 60

# 전역 변수 초기화
grid = []
ice_pos = [0, 0]
ice_pixel_pos = [0, 0]
target_pos = [0, 0]
moving = False
move_dir = (0, 0)
move_end = (0, 0)
start_pixel = (0, 0)
speed = 300  # 픽셀/초

# 맵 파싱 함수
def load_map(level):
    global grid, ice_pos, ice_pixel_pos, target_pos
    grid = []
    for y, row in enumerate(level):
        row_list = []
        for x, tile in enumerate(row):
            if tile == 'O':
                ice_pos[:] = [x, y]
                ice_pixel_pos[:] = [x * TILE_SIZE, y * TILE_SIZE]
                row_list.append(' ')
            elif tile == 'X':
                target_pos[:] = [x, y]
                row_list.append(' ')
            else:
                row_list.append(tile)
        grid.append(row_list)

# 그리기 함수
def draw():
    screen.fill(WHITE)
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == '#':
                pygame.draw.rect(screen, WALL_COLOR, rect)
            if [x, y] == target_pos:
                pygame.draw.rect(screen, TARGET_COLOR, rect)
    ice_rect = pygame.Rect(ice_pixel_pos[0], ice_pixel_pos[1], TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, ICE_COLOR, ice_rect)
    if ice_pos == target_pos and not moving:
        text = font.render("클리어!", True, CLEAR_COLOR)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()

# 이동 애니메이션 시작 (벽 앞에서 정확히 멈춤)
def start_move(dx, dy):
    global moving, move_dir, move_end, start_pixel
    rows, cols = len(grid), len(grid[0])
    x0, y0 = ice_pos
    nx, ny = x0 + dx, y0 + dy
    if not (0 <= nx < cols and 0 <= ny < rows) or grid[ny][nx] == '#':
        return
    # 미끄러질 최종 위치 계산
    fx, fy = nx, ny
    while True:
        tx, ty = fx + dx, fy + dy
        if not (0 <= tx < cols and 0 <= ty < rows) or grid[ty][tx] == '#':
            break
        fx, fy = tx, ty
        if [fx, fy] == target_pos:
            break
    # 애니메이션 시작 정보
    start_pixel = (ice_pixel_pos[0], ice_pixel_pos[1])
    move_end = (fx * TILE_SIZE, fy * TILE_SIZE)
    # 방향 벡터 (단위)
    delta_x = move_end[0] - start_pixel[0]
    delta_y = move_end[1] - start_pixel[1]
    dir_x = delta_x / abs(delta_x) if delta_x != 0 else 0
    dir_y = delta_y / abs(delta_y) if delta_y != 0 else 0
    move_dir = (dir_x, dir_y)
    moving = True
    ice_pos[:] = [fx, fy]

# 초기화
load_map(levels[current_level])

# 메인 루프
running = True
level_cleared = False
while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not moving:
            if ice_pos == target_pos:
                level_cleared = True
            if level_cleared:
                if event.key == pygame.K_SPACE:
                    current_level += 1
                    if current_level >= len(levels):
                        running = False
                    else:
                        level_cleared = False
                        load_map(levels[current_level])
            else:
                if event.key == pygame.K_LEFT:
                    start_move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    start_move(1, 0)
                elif event.key == pygame.K_UP:
                    start_move(0, -1)
                elif event.key == pygame.K_DOWN:
                    start_move(0, 1)

    # 애니메이션 업데이트
    if moving:
        ice_pixel_pos[0] += move_dir[0] * speed * dt
        ice_pixel_pos[1] += move_dir[1] * speed * dt
        # 도착 여부 판단
        reached_x = (move_dir[0] > 0 and ice_pixel_pos[0] >= move_end[0]) or (move_dir[0] < 0 and ice_pixel_pos[0] <= move_end[0])
        reached_y = (move_dir[1] > 0 and ice_pixel_pos[1] >= move_end[1]) or (move_dir[1] < 0 and ice_pixel_pos[1] <= move_end[1])
        if reached_x and reached_y:
            ice_pixel_pos[:] = list(move_end)
            moving = False

    draw()

pygame.quit()
sys.exit()
