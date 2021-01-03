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




#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #이벤트 발생하였는가
        if event.type == pygame.QUIT: #창이 끝나는 이벤트 발생
            running = False
    #screen.fill((0, 0, 255)) #색으로 채운다.
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #게임화면을 다시 그리기


pygame.quit()
