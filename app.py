from constants import *

import pygame
from pygame.locals import *
from random import choice

pygame.init()
pygame.font.init()

class App_2048:
    '''2048 App Class'''
    def __init__(self, end: int = None) -> None:
        '''Initializing the 2048 class.
        Accepts an optional int and ends the game as a win once a end number tile is obtained, else keeps continuing'''
        self.end = end
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)

    def init_variables(self):
        self.running = True
        self.score = 0
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.add_block()

    def exit(self) -> None:
        '''Safely exit the program'''
        pygame.quit()
        quit()

    def rot90(self, matrix: list[list]) -> list[list]:
        '''Rotates the given matrix 90 degree and returns it'''
        return [list(reversed(row)) for row in zip(*matrix)]

    def rot180(self, matrix: list[list]) -> list[list]:
        '''Rotates the given matrix 180 degree and returns it'''
        return self.rot90(self.rot90(matrix))

    def rot270(self, matrix: list[list]) -> list[list]:
        '''Rotates the given matrix 270 degree and returns it'''
        return self.rot180(self.rot90(matrix))

    def push_right(self) -> None:
        '''Pushes the tiles in self.matrix to the right'''
        for col in range(len(self.grid[0]) - 2, -1, -1):
            for row in self.grid:
                if row[col + 1] == 0:
                    row[col], row[col + 1] = 0, row[col]
                elif row[col + 1] == row[col]:
                    self.score += row[col] * 2
                    row[col], row[col + 1] = 0, row[col] * 2

    def right(self) -> None:
        '''Performs a right action on self.matrix'''
        self.push_right()
        self.update()

    def left(self) -> None:
        '''Performs a left action on self.matrix'''
        self.grid = self.rot180(self.grid)
        self.push_right()
        self.grid = self.rot180(self.grid)
        self.update()

    def up(self) -> None:
        '''Performs a up action on self.matrix'''
        self.grid = self.rot90(self.grid)
        self.right()
        self.grid = self.rot270(self.grid)
        self.update()

    def down(self) -> None:
        '''Performs a down action on self.matrix'''
        self.grid = self.rot270(self.grid)
        self.push_right()
        self.grid = self.rot90(self.grid)
        self.update()

    def game_state(self) -> str:
        '''Returns the state of the game:
        1) WIN if the game is won.
        2) BLOCK AVAILABLE if a block is still not filled.
        3) CAN MERGE if two tiles can still be merged.
        4) LOSE if the game is lost.'''
        if self.end:
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.grid[row][col] == self.end:
                        return 'WIN'

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    return 'BLOCK AVAILABLE'

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row]) - 1):
                if self.grid[row][col] == self.grid[row][col + 1]:
                    return 'CAN MERGE'

        for row in range(len(self.grid) - 1):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == self.grid[row + 1][col]:
                    return 'CAN MERGE'

        return 'LOSE'

    def add_block(self) -> None:
        '''Adds a random block to self.matrix'''
        free_blocks = [(y, x) for y, row in enumerate(self.grid) for x, num in enumerate(row) if num == 0]
        y, x = choice(free_blocks)
        self.grid[y][x] = 2

    def update(self) -> None:
        '''Updates the game state'''
        state = self.game_state()
        if state == 'WIN':
            self.game_over(True)
        elif state == 'LOSE':
            self.game_over(False)
        elif state == 'BLOCK AVAILABLE':
            self.add_block()

    def game_over(self, win: bool) -> None:
        '''Ends the game'''
        self.draw_win()
        if win:
            label = GAME_OVER_FONT.render(f'You won! You scored {self.score} points.', 1, BLUE)
        else:
            label = GAME_OVER_FONT.render(f'You lost! You scored {self.score} points.', 1, RED)
        self.win.blit(label, (WIDTH//2 - label.get_width()//2,
            HEIGHT//2 - label.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)
        self.running = False

    def draw_win(self) -> None:
        '''Draws onto the self.win'''
        self.win.fill(BLACK)
        self.draw_grid()
        self.draw_stats()

    def draw_grid(self) -> None:
        '''Draws self.matrix onto self.win'''
        pygame.draw.rect(self.win, BG_COLOR,
            (LEFT - GAP, TOP - GAP, len(self.grid[0]) * (BLOCK_WIDTH + GAP) + GAP,
            len(self.grid) * (BLOCK_HEIGHT + GAP) + GAP))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x = LEFT + (col * (BLOCK_WIDTH + GAP))
                y = TOP + (row * (BLOCK_HEIGHT + GAP))
                value = self.grid[row][col]
                bg_color, font_color = COLOR_MAP[value]
                color_rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
                pygame.draw.rect(self.win, bg_color, color_rect)

                if value != 0:
                    label = BLOCK_FONT.render(str(value), 1, font_color)
                    font_rect = label.get_rect()
                    font_rect.center = color_rect.center
                    self.win.blit(label, font_rect)

    def draw_stats(self) -> None:
        '''Draws the stats onto self.win'''
        label = TITLE_FONT.render(f'2048', 1, WHITE)
        self.win.blit(label, (400,5))

        label = STATS_FONT.render(f'Score: {self.score}', 1, WHITE)
        self.win.blit(label, (650, 200))

    def main(self) -> None:
        '''Main function which runs the game'''
        self.init_variables()
        while self.running:
            self.draw_win()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        self.left()
                    if event.key in [K_d, K_RIGHT]:
                        self.right()
                    if event.key in [K_w, K_UP]:
                        self.up()
                    if event.key in [K_s, K_DOWN]:
                        self.down()
        self.main_menu()

    def main_menu(self) -> None:
        '''Runs a main menu'''
        self.win.fill(BLACK)
        label = MAIN_MENU_FONT.render('Press any key to start...', 1, WHITE)
        self.win.blit(label, (WIDTH//2 - label.get_width()//2,
            HEIGHT//2 - label.get_height()//2))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                if event.type in [KEYDOWN, MOUSEBUTTONDOWN]:
                    running = False
        self.main()