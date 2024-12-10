import pygame as pg
import random

def next_generation(matrix):
    new_matrix = [[0 for _ in range(25)] for _ in range(25)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            neighbours = []
            if i - 1 >= 0:
                neighbours.append(matrix[i-1][j])
                if j - 1 >= 0:
                    neighbours.append(matrix[i-1][j-1])
                if j + 1 < len(matrix[i]):
                    neighbours.append(matrix[i-1][j+1])

            if i + 1 < len(matrix):
                neighbours.append(matrix[i+1][j])
                if j - 1 >= 0:
                    neighbours.append(matrix[i+1][j-1])
                if j + 1 < len(matrix[i]):
                    neighbours.append(matrix[i+1][j+1])
            if j - 1 >= 0:
                neighbours.append(matrix[i][j-1])
            if j + 1 < len(matrix[i]):
                neighbours.append(matrix[i][j+1])
            
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

def main():
    matrix = [[0 for _ in range(25)] for _ in range(25)]

    for i in range(100):
        y = random.randint(0,24)
        x = random.randint(0,24)
        matrix[y][x] = 1


    pg.init()
    screen = pg.display.set_mode((500, 500))
    clock = pg.time.Clock()

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        matrix = next_generation(matrix)

        screen.fill(pg.Color(0,0,0))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    pg.draw.rect(screen, pg.Color(255,255,255), pg.Rect(j*20, i*20, 20, 20))

        pg.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()