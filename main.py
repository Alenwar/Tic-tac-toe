import pygame
import time


pygame.init()
width = 600
height = 700


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-tak-toe')
pygame.display.set_icon(pygame.image.load('Images/3151552_tac_tic_toe_icon.png'))


white = (255, 255, 255)
black = (0, 0, 0)


myfont = pygame.font.Font('font/Inconsolata_Condensed-Black.ttf', 30)
text_player_x = myfont.render('Player (X)', True, white)
text_player_o = myfont.render('PLayer (O)', True, white)


board = [[0] * 3 for i in range(3)]


def draw_board():
    pygame.draw.line(screen, white, (40, 200), (560, 200), 4)
    pygame.draw.line(screen, white, (40, 400), (560, 400), 4)

    pygame.draw.line(screen, white, (200, 40), (200, 560), 4)
    pygame.draw.line(screen, white, (400, 40), (400, 560), 4)

def draw_x(row, col):
    pygame.draw.line(screen, white, (col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55, row * 200 + 55), 6)
    pygame.draw.line(screen, white, (col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55, row * 200 + 200 - 55), 6)


def draw_o(row, col):
    pygame.draw.circle(screen, white, (col * 200 + 200//2, row * 200 + 200 //2), 50, 6)


def window_access(row, col, player):
     board[row][col] = player


def available_window(row, col):
     if board[row][col] == 0:
         return True
     else:
        return False

def if_full(row, col):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True


def check_for_winner(player):
    winner = None

    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            winner = player
        elif all(board[j][i] == player for j in range(3)):
            winner = player

    if all(board[i][i] == player for i in range(3)):
        winner = player
    elif all(board[i][2 - i] == player for i in range(3)):
        winner = player

    return winner


def restart():

    screen.fill(black)
    draw_board()
    screen.blit(text_player_x, (50, 600))
    screen.blit(text_player_o, (420, 600))
    for row in range(3):
        for col in range(3):
            board[row][col] = 0


def game():
    player = 1
    running = True
    draw_board()
    screen.blit(text_player_x, (50, 600))
    screen.blit(text_player_o, (430, 600))
    while running:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()



            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                row = y // 200
                col = x // 200

                if available_window(row, col):
                    if player == 1:
                        window_access(row, col, 1)
                        player = 2
                        draw_x(row, col)
                    elif player == 2:
                        window_access(row, col, 2)
                        player = 1
                        draw_o(row, col)


                winner = check_for_winner(player)
                if winner is not None:
                    time.sleep(1)
                    restart()

                elif winner is None and if_full(row, col):
                    time.sleep(1)
                    restart()
                    player = 1


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    running = True

game()