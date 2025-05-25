import pygame as pg
import random


GRID_HEIGHT = 80
GRID_WIDTH = 100
CELL_SIZE = 10
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
INITIAL_CELLS = 500

def next_generation(matrix):
    new_matrix = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            neighbours = get_neighbours(matrix, i, j)
            cell = matrix[i][j]
            if cell == 1:
    # Any live cell with fewer than two living neighbors dies
                if neighbours.count(1) < 2:
                    new_matrix[i][j] = 0
    # Any live cell with two or three neighbours live on
                elif 2 <= neighbours.count(1) <= 3:
                    new_matrix[i][j] = 1
    # Any live cell with more than three neighbors die by overpopulation
                elif neighbours.count(1) > 3:
                    new_matrix[i][j] = 0
    # Any dead cell with exactly three neighbors becomes alive by reproduction
            elif neighbours.count(1) == 3:
                new_matrix[i][j] = 1
        
    return new_matrix

def get_neighbours(matrix: list[list], i: int, j: int) -> list[int]:
    neighbours = []
    
    if i - 1 >= 0:
        neighbours.append(matrix[i-1][j])
        if j - 1 >= 0:
            neighbours.append(matrix[i-1][j-1])
            neighbours.append(matrix[i][j-1])
        if j + 1 < len(matrix[i]):
            neighbours.append(matrix[i-1][j+1])
            neighbours.append(matrix[i][j+1])

    if i + 1 < len(matrix):
        neighbours.append(matrix[i+1][j])
        if j - 1 >= 0:
            neighbours.append(matrix[i+1][j-1])
        if j + 1 < len(matrix[i]):
            neighbours.append(matrix[i+1][j+1])

    return neighbours

def draw(matrix: list[list], screen: pg.Surface):
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    cell_rect = pg.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pg.draw.rect(screen, pg.Color(random.randint(100,255),random.randint(100,255),random.randint(100,255)), cell_rect)

def main():
    matrix = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for _ in range(INITIAL_CELLS):
        y = random.randint(0,GRID_HEIGHT - 1)
        x = random.randint(0,GRID_WIDTH - 1)
        matrix[y][x] = 1


    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        matrix = next_generation(matrix)

        screen.fill(pg.Color(0,0,0))

        draw(matrix, screen)
        

        pg.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()