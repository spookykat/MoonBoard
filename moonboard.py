import json
import pygame
board = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0]
]
def resetBoard():
    global board
    board = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0]
    ]
colors = [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0)]

problem = 0

def printBoard(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(f"{board[row][col]} ", end="")
        print()

def getProblem(problem1):
    resetBoard()
    problem = json.loads(problem1.replace('\'', '\"').replace('None','null').replace('False','false').replace('True','true'))
    for hold in problem['moves']:
        row = 18 - int(hold['description'][1:3])
        col = ord(hold['description'][0].lower()) - 96 - 1

        if hold['isStart']:
            hold_type = 2
        elif hold['isEnd']:
            hold_type = 3
        else:
            hold_type = 1
        board[row][col] = hold_type

def displayProblem(problem):
    pygame.init()

    screen = pygame.display.set_mode([500, 500])

    running = True

    getProblem(problem)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for row in range(len(board)):
            for col in range(len(board[0])):
                pygame.draw.circle(screen, colors[board[row][col]], (10 + (15 * col), 10 + (15 * row)), 5)
        pygame.display.flip()

    pygame.quit()