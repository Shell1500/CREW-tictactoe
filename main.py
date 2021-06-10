import pygame, time

display_width = 600
display_height = 600


pygame.init()
screen = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.Font('C:\\Windows\\Fonts\CALIBRI.TTF', 60)
cross_image = pygame.image.load("cross.png")
circle_image = pygame.image.load("circle.png")

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
## box center positions
box0 = (100, 100)
box1 = (300, 300)
box3 = (400, 400)

def get_pos(x, y):
    if x < 200:
        col = 0
    elif x > 200 and x < 400:
        col = 1 
    else:
        col = 2
    
    if y < 200:
        row = 0
    elif y > 200 and y < 400:
        row = 1 
    else:
        row = 2
        
    return (row, col)


def get_box(coordinate):
    if coordinate == (0, 0):
        return (0, 0)
    elif coordinate == (0, 1):
        return (210, 0)
    elif coordinate == (0, 2):
        return (410, 0)
    
    elif coordinate == (1, 0):
        return (0, 210)
    elif coordinate == (1, 1):
        return (210, 210)
    elif coordinate == (1, 2):
        return (410, 210)
    
    elif coordinate == (2, 0):
        return (0, 410)
    elif coordinate == (2, 1):
        return (210, 410)
    else:
        return (410, 410)


def board_check(board):
    
    ## horizontal and vertical
    
    for i in range(2):    
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
        
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]

    ## diagnal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    

def text_objects(text, color):
    textSurface=font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width/2), (display_height/2)
    screen.blit(textSurf, textRect)


def game_over(winner):
    while True:
        screen.fill((173, 216, 230))
        message_screen(winner, (5, 5, 5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


done = False

box_status = []

current_turn = 'cross'

occupied_boxes = []

while not done:
    
    # Background RGB - Red, Green, Blue
    screen.fill((173, 216, 230))

    pygame.draw.rect(screen, (32, 32, 32), (display_width/3, 0, 20, display_height))
    pygame.draw.rect(screen, (32, 32, 32), ((display_width*2)/3, 0, 20, display_height))
    
    pygame.draw.rect(screen, (32, 32, 32), ((0, display_height/3, display_width, 20)))
    pygame.draw.rect(screen, (32, 32, 32), ((0, (display_height*2)/3, display_width, 20)))
    
    
        
    if pygame.mouse.get_pressed()[0] == True:
        cords = pygame.mouse.get_pos()
        mouse_position = get_pos(cords[0], cords[1])
        box_coordinate = get_box(mouse_position)
        
        if box_coordinate not in occupied_boxes:
            if current_turn == 'cross':
                box_status.append([cross_image, box_coordinate])
                current_turn = 'circle'
                board[mouse_position[0]][mouse_position[1]] = 1
            else:
                box_status.append([circle_image, box_coordinate])
                current_turn = 'cross'
                board[mouse_position[0]][mouse_position[1]] = 2

        occupied_boxes.append(box_coordinate)
        
    for boxes in box_status:
        screen.blit(boxes[0], boxes[1])

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    if board_check(board) == 1:
        game_over('Cross Wins')
        done = True
    if board_check(board) == 2:
        game_over('Circle Wins')
        done = True
    
    if len(box_status) == 9:
        game_over('Game DRAW')
        done = True 
    pygame.display.update()
    time.sleep(0.05)








    
    