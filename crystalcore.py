import pygame # import pygame and sys
import myFunctions




pygame.init()
background = pygame.image.load('background.png')
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Lucid Crystalline!')
image = pygame.image.load('linky.jpg')
image2 = pygame.image.load('crystal.png')
clock = pygame.time.Clock()

#Resize part
image2 = pygame.transform.scale(image2,(170,150))



#font and where to change the text
font= pygame.font.Font('freesansbold.ttf',15)
text1 = font.render('Crystal Core ',False,(255,255,0))
text2 = font.render('To be continued ',False,(120,255,255))
text3 = font.render ('To be continued',False, (204, 255,0	
))
text4 = font.render('Quick cube',False,(204, 255, 0	
))
font= pygame.font.Font('freesansbold.ttf',15)
text5 = font.render('Welcome to Lucid Crystalline!!!',False,(204, 255, 0	
))
text6 = font.render('Run to any of the crystals to join the mini game',False,(204,255,0))



#Player Variables
xpos = 220
ypos = 220
counter=0
ticker = 0
direction =3

#Transperency
player_img = pygame.image.load('linky.jpg')
player_img.set_colorkey((255,255,255))


xposb = 60
yposb = 30
widthb = 50
heightb = 100



#Parkour unmoving Crystal
xpos2 = 0
ypos2 = 0
width2 = 30
height2 = 30

# unmoving Crystal
xpos3 = 350
ypos3 = 10
width3 = 60
height3 = 60

# unmoving Crystal
xpos4 = 350
ypos4 = 250
width4 = 60
height4 = 60

# unmoving Crystal
xpos5 = 0
ypos5 = 250
width5 = 60
height5 = 60





#imports function
myFunctions.PlayIntro()




while True: #GAME LOOP
    clock.tick(10000)
#input/output section
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :

            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        direction =0
        xpos-=2
        ticker += 1
        if ticker >5:
          ticker = 0
          counter+=1
        if counter>7: #i have 8 images in my row (first is 0)
            counter = 0

    if keys[pygame.K_RIGHT]:
        direction = 1
        xpos+=2  
        ticker += 1
        if ticker>5:
          ticker = 0
          counter+= 1
          if counter>7:#how many images are in spritesheet
            counter = 0

   #up position         
    if keys[pygame.K_UP]:
      direction = 2
      ypos-= 2
      ticker += 1
      if ticker>5:
        ticker = 0
        counter+= 1
        if counter >7:
          counter = 0

    if keys[pygame.K_DOWN]:
      direction = 3  
      ypos+= 2
      ticker += 1
      if ticker>5:
        ticker = 0
        counter+= 1
        if counter >7:
          counter = 0

    else:
      couter=0    


    
   

#render section
    screen.blit(background,(0,0))

    #collision    
    if xpos+20 > xposb and ypos+20 >yposb and xpos+20<ypos:
      import CrystalJump
      CrystalJump.game()

    if direction == 0:
        screen.blit(image, (xpos,ypos), (0+counter*32,0,32,48))
    if direction == 1:
        screen.blit(image, (xpos,ypos), (0+counter*32,48,32,48))
    if direction == 2:
        screen.blit(image, (xpos,ypos), (0+counter*32,96,32,48))    
    if direction == 3:
        screen.blit(image, (xpos,ypos), (0+counter*32,144,32,48))     
        
      
   #draw the crystals square
    screen.blit(image2,(xpos2, ypos2, width2, height2))

    screen.blit(image2,(xpos3, ypos3, width3, height3))


    screen.blit(image2,(xpos4, ypos4, width4, height4))
    screen.blit(image2,(xpos5, ypos5, width5, height5))

  

    #Draws text to the screen
    screen.blit(text1,(50,50))

    screen.blit(text2,(395,60))


    screen.blit(text6,(90,20))

    

    
   
    
    pygame.display.flip() 

#end game loop-----------------------------------------------------------------------------
pygame.quit()
    
    
