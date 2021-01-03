import pygame

pygame.init() #초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")

#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #이벤트 발생하였는가
        if event.type == pygame.QUIT: #창이 끝나는 이벤트 발생
            running = False

pygame.quit()
