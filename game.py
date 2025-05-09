import pygame
import sys

# --- 설정값 ------------------------------------------------
WIDTH, HEIGHT = 600, 800
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
LINE_WIDTH = 10

# 원과 X 선 두께 및 여백
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = CELL_SIZE // 4

# 색상
BG_COLOR     = (255, 0, 0)  # 빨간색
LINE_COLOR   = (200, 0, 0)  # 어두운 빨간색
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR  = (66,  66,  66)
TEXT_COLOR   = (255, 255, 255)

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BG_COLOR)
font = pygame.font.SysFont(None, 48)

# 보드 상태: 0=빈칸, 1=X, 2=O
board = [[0] * COLS for _ in range(ROWS)]
current_player = 1  # 1=X, 2=O
game_over = False
winner = 0  # 0=진행중, 1=X, 2=O, 3=무승부

# --- 그리기 함수들 ------------------------------------------
def draw_grid():
    # 수평선
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR,
                         (0, CELL_SIZE * i),
                         (WIDTH, CELL_SIZE * i),
                         LINE_WIDTH)
    # 수직선
    for j in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR,
                         (CELL_SIZE * j, 0),
                         (CELL_SIZE * j, WIDTH),  # 높이는 격자까지만
                         LINE_WIDTH)

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if board[row][col] == 1:
                # X 그리기
                pygame.draw.line(screen, CROSS_COLOR,
                                 (x + SPACE,     y + SPACE),
                                 (x + CELL_SIZE - SPACE, y + CELL_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (x + SPACE,     y + CELL_SIZE - SPACE),
                                 (x + CELL_SIZE - SPACE, y + SPACE),
                                 CROSS_WIDTH)
            elif board[row][col] == 2:
                # O 그리기
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (x + CELL_SIZE//2, y + CELL_SIZE//2),
                                   CELL_SIZE//2 - SPACE,
                                   CIRCLE_WIDTH)

def render_status():
    msg = ''
    if winner == 1:
        msg = 'Player X wins! (R: Restart)'
    elif winner == 2:
        msg = 'Player O wins! (R: Restart)'
    elif winner == 3:
        msg = 'Draw! (R: Restart)'
    else:
        msg = f'Player {"X" if current_player==1 else "O"}\'s turn'
    text = font.render(msg, True, TEXT_COLOR)
    # 하단 중앙에 렌더
    screen.blit(text, ((WIDTH - text.get_width())//2, WIDTH + (HEIGHT - WIDTH - text.get_height())//2))

# --- 게임 로직 --------------------------------------------
def check_winner(player):
    # 행 검사
    for row in board:
        if all(cell == player for cell in row):
            return True
    # 열 검사
    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            return True
    # 대각선 검사
    if all(board[i][i] == player for i in range(ROWS)):
        return True
    if all(board[i][COLS-1-i] == player for i in range(ROWS)):
        return True
    return False

def is_board_full():
    return all(cell != 0 for row in board for cell in row)

def restart_game():
    global board, current_player, game_over, winner
    board = [[0] * COLS for _ in range(ROWS)]
    current_player = 1
    game_over = False
    winner = 0
    screen.fill(BG_COLOR)
    draw_grid()

# 최초 그리기
draw_grid()

# --- 메인 루프 --------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = event.pos
            if my < WIDTH:  # 격자 영역 클릭
                row = my // CELL_SIZE
                col = mx // CELL_SIZE
                if board[row][col] == 0:
                    board[row][col] = current_player
                    # 승리 검사
                    if check_winner(current_player):
                        game_over = True
                        winner = current_player
                    elif is_board_full():
                        game_over = True
                        winner = 3  # 무승부
                    else:
                        current_player = 2 if current_player == 1 else 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    # 화면 갱신
    draw_figures()
    render_status()
    pygame.display.update()
