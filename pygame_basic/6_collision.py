import pygame

pygame.init() #초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")


#FPS
clock = pygame.time.Clock()


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

#이동 속도
character_speed = 0.6

#적 evemy 캐릭터
enemy = pygame.image.load("C:/Users/kikii/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해줌
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로 절반 위치
enemy_y_pos = (screen_height /2) - (enemy_height /2) #화면 세로 가장 아래


#이벤트 루프
running = True #게임이 진행중인가
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

    #print("fps : " + str(clock.get_fps()))



    for event in pygame.event.get(): #이벤트 발생하였는가
        if event.type == pygame.QUIT: #창이 끝나는 이벤트 발생
            running = False


        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x*dt #프레임에 따라 속도 달라지게
    character_y_pos += to_y*dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    #screen.fill((0, 0, 255)) #색으로 채운다.
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    
    pygame.display.update() #게임화면을 다시 그리기


pygame.quit()
