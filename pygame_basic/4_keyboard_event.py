import pygame

pygame.init() #초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")

background = pygame.image.load("C:/Users/kikii/Desktop/PythonWorkspace/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("C:/Users/kikii/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기를 구해줌
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반 위치
character_y_pos = screen_height - character_height #화면 세로 가장 아래

#이동할 좌표
to_x = 0
to_y = 0


#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #이벤트 발생하였는가
        if event.type == pygame.QUIT: #창이 끝나는 이벤트 발생
            running = False


        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #screen.fill((0, 0, 255)) #색으로 채운다.
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #게임화면을 다시 그리기


pygame.quit()
