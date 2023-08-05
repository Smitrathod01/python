import pygame

#module initialization
x=pygame.init()

#screen initialization
wn=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Welcome")

#game variables
exit_game = False
game_over = False

#game loop
while not exit_game:#help to steady the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True  #this line will help to exit the window by cross button to get out of game loop

        if event.type == pygame.KEYDOWN:#this is to notify key pressed or not
            if event.key == pygame.K_RIGHT:
                print("You have pressed right key")


pygame.quit()
quit()
