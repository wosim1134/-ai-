import pygame
import sys

# --- 설정값 ------------------------------------------------
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)

# 게임 요소
WALL = '#'
BOX = '$'
TARGET = '.'
PLAYER = '@'
FLOOR = ' '
BOX_ON_TARGET = '*'
PLAYER_ON_TARGET = '+'

# 레벨 1
LEVEL_1 = [
    "########",
    "#      #",
    "#  .$  #",
    "#  @   #",
    "#  .$  #",
    "#      #",
    "########"
]

class Sokoban:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Sokoban')
        self.clock = pygame.time.Clock()
        self.level = [list(row) for row in LEVEL_1]
        self.player_pos = self.find_player()
        self.targets = self.find_targets()
        self.moves = 0
        self.font = pygame.font.SysFont(None, 36)

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
        self.screen.fill(WHITE)
        
        # 게임 보드 그리기
        for y, row in enumerate(self.level):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                
                if cell == WALL:
                    pygame.draw.rect(self.screen, GRAY, rect)
                elif cell in [TARGET, PLAYER_ON_TARGET]:
                    pygame.draw.rect(self.screen, GREEN, rect)
                    pygame.draw.circle(self.screen, BLACK, 
                                     (x * TILE_SIZE + TILE_SIZE//2, 
                                      y * TILE_SIZE + TILE_SIZE//2), 
                                     TILE_SIZE//4)
                elif cell in [BOX, BOX_ON_TARGET]:
                    pygame.draw.rect(self.screen, BROWN, rect)
                elif cell in [PLAYER, PLAYER_ON_TARGET]:
                    pygame.draw.rect(self.screen, BLUE, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)
                
                pygame.draw.rect(self.screen, BLACK, rect, 1)

        # 이동 횟수 표시
        moves_text = self.font.render(f'Moves: {self.moves}', True, BLACK)
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

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    elif event.key == pygame.K_UP:
                        self.move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    elif event.key == pygame.K_r:  # 재시작
                        self.__init__()

            self.draw()
            
            if self.check_win():
                win_text = self.font.render('You Win! Press R to restart', True, RED)
                self.screen.blit(win_text, (WIDTH//2 - 150, HEIGHT//2))
                pygame.display.flip()

            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Sokoban()
    game.run() 