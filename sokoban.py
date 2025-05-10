import pygame
import sys

# --- 설정값 ------------------------------------------------
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40  # 타일 크기를 줄여서 더 많은 공간 활용
FPS = 60

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)  # 진한 녹색 추가

# 게임 요소
WALL = '#'
BOX = '$'
TARGET = '.'
PLAYER = '@'
FLOOR = ' '
BOX_ON_TARGET = '*'
PLAYER_ON_TARGET = '+'

# 레벨들
LEVELS = [
    # 레벨 1
    [
        "#######",
        "#     #",
        "#@  $.#",
        "#     #",
        "#######"
    ],
    # 레벨 2
    [
        "#######",
        "####  #",
        "#     #",
        "#@ $# #",
        "#    .#",
        "#######"
    ],
    # 레벨 3
    [
        "#########",
        "##### ###",
        "####   ##",
        "####$$.##",
        "## $    #",
        "#  ##@  #",
        "## ..  ##",
        "####  ###",
        "#########"
    ],
    # 레벨 4
    [
        "######",
        "# . ##",
        "#    #",
        "# .$ #",
        "###$ #",
        "### @#",
        "######"
    ],
    # 레벨 5
    [
        "#########",
        "###  $@.#",
        "### # ###",
        "#.  $ ###",
        "#########"
    ],

]

class Sokoban:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Sokoban')
        self.clock = pygame.time.Clock()
        self.current_level = 0
        self.load_level(self.current_level)
        self.moves = 0
        self.font = pygame.font.SysFont(None, 36)
        self.level_completed = False  # 레벨 클리어 상태 추가
        self.bg_img = pygame.image.load('background.png').convert()  # 배경 이미지 불러오기
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))  # 전체 화면 크기로 조정
        self.box_img = pygame.image.load('box.png').convert_alpha()  # 박스 이미지 불러오기
        self.box_img = pygame.transform.scale(self.box_img, (TILE_SIZE, TILE_SIZE))
        self.goal_img = pygame.image.load('goal.png').convert_alpha()  # 도착지 이미지 불러오기
        self.goal_img = pygame.transform.scale(self.goal_img, (TILE_SIZE, TILE_SIZE))
        self.player_img = pygame.image.load('player.png').convert_alpha()  # 플레이어 이미지 불러오기
        self.player_img = pygame.transform.scale(self.player_img, (TILE_SIZE, TILE_SIZE))
        self.wall_img = pygame.image.load('wall.png').convert_alpha()  # 벽 이미지 불러오기
        self.wall_img = pygame.transform.scale(self.wall_img, (TILE_SIZE, TILE_SIZE))

    def load_level(self, level_num):
        self.level = [list(row) for row in LEVELS[level_num]]
        self.player_pos = self.find_player()
        self.targets = self.find_targets()
        self.moves = 0
        self.level_completed = False  # 레벨 로드시 클리어 상태 초기화

    def find_player(self):
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                if cell in [PLAYER, PLAYER_ON_TARGET]:
                    return [x, y]
        return None

    def find_targets(self):
        targets = []
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                if cell in [TARGET, BOX_ON_TARGET, PLAYER_ON_TARGET]:
                    targets.append([x, y])
        return targets

    def draw(self):
        # 배경 이미지를 전체 화면에 한 번만 그리기
        self.screen.blit(self.bg_img, (0, 0))
        
        # 게임 보드 중앙 정렬을 위한 오프셋 계산
        board_width = len(self.level[0]) * TILE_SIZE
        board_height = len(self.level) * TILE_SIZE
        offset_x = (WIDTH - board_width) // 2
        offset_y = (HEIGHT - board_height) // 2
        
        # 게임 보드 그리기
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                rect = pygame.Rect(offset_x + x * TILE_SIZE, 
                                 offset_y + y * TILE_SIZE, 
                                 TILE_SIZE, TILE_SIZE)
                
                if cell == WALL:
                    self.screen.blit(self.wall_img, rect)
                elif cell == TARGET:
                    self.screen.blit(self.goal_img, rect)
                elif cell == BOX:
                    self.screen.blit(self.box_img, rect)
                elif cell == BOX_ON_TARGET:
                    # 골대 먼저 그리고 그 위에 박스 그리기
                    self.screen.blit(self.goal_img, rect)
                    self.screen.blit(self.box_img, rect)
                elif cell == PLAYER:
                    self.screen.blit(self.player_img, rect)
                elif cell == PLAYER_ON_TARGET:
                    self.screen.blit(self.goal_img, rect)
                    self.screen.blit(self.player_img, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)
                
                pygame.draw.rect(self.screen, BLACK, rect, 1)

        # 이동 횟수와 현재 레벨 표시
        moves_text = self.font.render(f'Level: {self.current_level + 1}  Moves: {self.moves}', True, BLACK)
        self.screen.blit(moves_text, (10, HEIGHT - 40))

        pygame.display.flip()

    def move(self, dx, dy):
        x, y = self.player_pos
        new_x, new_y = x + dx, y + dy
        
        # 벽 체크
        if self.level[new_y][new_x] == WALL:
            return
        
        # 상자 이동
        if self.level[new_y][new_x] in [BOX, BOX_ON_TARGET]:
            box_x, box_y = new_x + dx, new_y + dy
            
            # 상자 뒤가 벽이나 다른 상자인 경우
            if self.level[box_y][box_x] in [WALL, BOX, BOX_ON_TARGET]:
                return
            
            # 상자 이동
            self.level[box_y][box_x] = BOX_ON_TARGET if [box_x, box_y] in self.targets else BOX
            self.level[new_y][new_x] = PLAYER_ON_TARGET if [new_x, new_y] in self.targets else PLAYER
        
        # 플레이어 이동
        self.level[y][x] = TARGET if [x, y] in self.targets else FLOOR
        self.level[new_y][new_x] = PLAYER_ON_TARGET if [new_x, new_y] in self.targets else PLAYER
        self.player_pos = [new_x, new_y]
        self.moves += 1

    def check_win(self):
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                if cell == BOX and [x, y] not in self.targets:
                    return False
        return True

    def next_level(self):
        if self.current_level < len(LEVELS) - 1:
            self.current_level += 1
            self.load_level(self.current_level)
            return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if not self.level_completed:  # 레벨이 클리어되지 않았을 때만 이동 가능
                        if event.key == pygame.K_LEFT:
                            self.move(-1, 0)
                        elif event.key == pygame.K_RIGHT:
                            self.move(1, 0)
                        elif event.key == pygame.K_UP:
                            self.move(0, -1)
                        elif event.key == pygame.K_DOWN:
                            self.move(0, 1)
                    
                    if event.key == pygame.K_r:  # 재시작
                        self.load_level(self.current_level)

            self.draw()
            
            if self.check_win():
                self.level_completed = True  # 레벨 클리어 상태 설정
                
                # 클리어 메시지 표시
                clear_text = self.font.render('Level Clear!', True, DARK_GREEN)
                clear_rect = clear_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
                self.screen.blit(clear_text, clear_rect)
                
                if self.current_level < len(LEVELS) - 1:
                    next_text = self.font.render('Next Level...', True, DARK_GREEN)
                    next_rect = next_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 30))
                    self.screen.blit(next_text, next_rect)
                    pygame.display.flip()
                    
                    # 1초 대기 후 다음 레벨로
                    pygame.time.wait(1000)
                    self.next_level()
                else:
                    # 모든 레벨 클리어
                    win_text = self.font.render('Congratulations! You completed all levels!', True, DARK_GREEN)
                    win_rect = win_text.get_rect(center=(WIDTH//2, HEIGHT//2))
                    self.screen.blit(win_text, win_rect)
                    pygame.display.flip()

            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Sokoban()
    game.run() 