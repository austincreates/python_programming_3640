import pygame

pygame.init()

display_width = 800
display_height = 600

#RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)   

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car_green_3.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

""" Should be noted that
top left is origin. Adding x 
makes goes right. Adding y
makes goes down. 

"""

def game_loop():
    

    x = (display_width * 0.45)
    y = (display_height * .75)

    x_change = 0
    crashed = False

    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 

        x += x_change            

            #print(event)
        gameDisplay.fill(white)
        car(x,y)
        pygame.display.update()
        #pygame.display.flip() #provides update for whole screen (takes longer)

        clock.tick(30)

    game_loop()
    pygame.quit()
    quit()


