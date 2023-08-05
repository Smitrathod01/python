import pygame
import random
import os

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

white=(255,255,255) #rgb form
black=(0,0,0)
red=(255,0,0)
blue=(0,255,0)
green=(0,0,255)

wn=pygame.display.set_mode((800,600))
pygame.display.set_caption("Smit's snake game")
pygame.display.update()

bg=pygame.image.load("c.jpg")
bg=pygame.transform.scale(bg,(800,600)).convert_alpha()

pg=pygame.image.load("s.jpg")
pg=pygame.transform.scale(pg,(800,600)).convert_alpha()

font = pygame.font.SysFont(None,20)
def write(text,color,x,y):
    write = font.render(text,True,color)#use to display text .true is for anti aliasing
    wn.blit(write,[x,y])#used to write text on another surface

def welcome():
    pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(loops=-1)
    exit_game=False
    while not exit_game:
        #wn.fill(black)
        wn.blit(bg,(0,0))
        write("Its Smit Rathod's Creation",black,300,520)
        write("Press Spacebar to play",black,320,540)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('alan.mp3')
                    pygame.mixer.music.play(loops=-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game=False
    game_over=False
    snake_x =50
    snake_y=60
    snake_size=20
    velocity_x=0
    velocity_y=0
    food_x=random.randint(0,700)
    food_y=random.randint(0,500)
    fps=60
    score=0

    if(not os.path.exists("Shiscore.txt")):
        with open("Shiscore.txt","w") as f:
            f.write("0")

    with open("Shiscore.txt","r") as f:
        hiscore=f.read()
    
    while not exit_game:

        if game_over:

            with open("Shiscore.txt","w") as f:
                f.write(str(hiscore))

            wn.fill(white)
            #write(f"Game over!! Press Enter if you want to play again...Your Current score is {score}",green,150,300)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                    #snake_x = snake_x+10 by this line we can play by taptap but with automation it wont work
                        velocity_x=10
                        velocity_y=0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #snake_x = snake_x-10
                        velocity_x=-10
                        velocity_y=0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #snake_y = snake_y-10
                        velocity_y=-10
                        velocity_x=0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        #snake_y = snake_y+10
                        velocity_y=10
                        velocity_x=0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                #pygame.mixer.music.load('eat.mp3')
                #pygame.mixer.music.play()
                score+=5
                if score>int(hiscore):
                    hiscore=score
                food_x=random.randint(0,700)
                food_y=random.randint(0,500)

                

            if snake_x<0 or snake_x==800 or snake_y<0 or snake_y==600:
                game_over = True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()

            #wn.fill(black) 
            wn.blit(pg,(0,0))
            write("Score : "+str(score) + "  Highscore: "+str(hiscore),blue,5,5)
            pygame.draw.rect(wn,red,[food_x,food_y,snake_size-5,snake_size-5])
            pygame.draw.rect(wn,white,[snake_x,snake_y,snake_size,snake_size])

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()

welcome()
