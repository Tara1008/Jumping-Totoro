import pygame
from sys import exit
import random from randit

def display_score():
   current_time = int(pygame.time.get_ticks() / 1000) - start_time #dividing by 1000 to get numbers in 1 2 3
   score_surf = font.render(f'{current_time}',False,(1,50,25))#we have to put it in f string becuase it doest accept integers
   score_rect = score_surf.get_rect(center= (475,50))
   screen.blit(score_surf,score_rect)
   return current_time

def obstacle_movement(obstacle_list):
   if obstacle_list:
      for obstacle_rect in obstacle_list:
         obstacle_rect.x-= 5
         if obstacle_rect.bottom == 300:
            screen.blit(bush,obstacle_rect)
         screen.blit(bush,obstacle_rect)
      obstacle_list= [obstacle for obstacle in obstacle_list if obstacle.x>-100]
      return obstacle_list
   else: return []

def collisions(player,obstacles)
if obstacles:
   for obstacle_rect in obstacles:
      if player.colliderect(obstacle_rect):
         return False
      return True
      


pygame.init()
screen = pygame.display.set_mode((1000,400))
color = (173,216,230)
screen.fill(color)



#the input is a tuple, and this will work for only 1 sec
#this is a display surface that shows up for a sec and then the code terminates
#a way to keep the code to keep running is to use a while loop
pygame.display.set_caption('jumpjump')
clock = pygame.time.Clock() #clock object
font = pygame.font.Font('RobotoMono.ttf',30) #need to add font style here
game_active = False #change it to true later 
start_time = 0
score = 0


sky_surface = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\disneyback.png').convert()
ground_surface = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\groundf.jpg').convert()
#convert converts the image to a format pygame can easily work with -> making it faster

#   score = font.render('My Game', False, (64,64,64))#rgb
#   score_rect = score.get_rect(center = (500,40))

# obstacles
obstacle_rect_list= []




#for black and white stuff apparently?
figure = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\totoro_drawing-removebg-preview (1).png').convert_alpha()
figure_rect = figure.get_rect(midbottom = (80,364))
figure_gravity = 0

#game intro
figure_stand = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\standing_totoro-removebg-preview.png').convert_alpha()
figure_stand_rect = figure_stand.get_rect(center = (475,200))



game_name = font.render('Totoro Jump',False,(80,75,90))
game_name_rect = game_name.get_rect(center = (485,50))

game_message = font.render('Press space to run',False,(80,75,90))
game_message_rect = game_message.get_rect(center = (485,350))



bush = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\soot2-removebg-preview.png').convert_alpha() 
bush_rect = bush.get_rect(bottomright = (800,333))


#test_surface = pygame.Surface((600,100))
#test_surface.fill('Red')
#timer
obstacle_timer= pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
   for event in pygame.event.get():#gets events happening

      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

      if game_active:
         if event.type == pygame.MOUSEBUTTONDOWN:
            if figure_rect.collidepoint(event.pos) and figure_rect.bottom >= 365: 
               figure_gravity = -20
            
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and figure_rect.bottom >= 365:
               figure_gravity = -25    #########
      else:
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            bush_rect.left = 800
            start_time = int(pygame.time.get_ticks() / 1000)  
      if event.type == obstacle_timer and game_active:
         obstacle_rect_list.append(bush.get_rect(bottomright = (randint(1100,1300),333)))

   


   if game_active:
      screen.blit(sky_surface,(0,0))
      screen.blit(ground_surface,(0,330))#blit = block image transfer
      #pygame.draw.rect(screen,(24,64,26),score_rect,10)
      #screen.blit(score,score_rect)  
      score = display_score()

      bush_rect.left -= 5 ########
      if (bush_rect.left <- 100): 
         bush_rect.left = 800
      figure_rect.left += 3 ##########
      screen.blit(bush, bush_rect)

      #figure
      figure_gravity += 1
      figure_rect.y += figure_gravity
      if figure_rect.bottom >= 365:
         figure_rect.bottom = 365
      screen.blit(figure,figure_rect)

      #obstacle movement
      obstacle_movement(obstacle_rect_list)

      game_active=vcollisions(player_rect,obstacle_rect_list)

      if bush_rect.colliderect(figure_rect) and figure_rect.bottom == 365:
         game_active = False


   else:
      screen.fill((144,163,161)) #(12,38,27) optional
      screen.blit(figure_stand,figure_stand_rect)
      obstacle_rect_list.clear()

      score_message = font.render(f'Your Score: {score}',False,(80,75,90))
      score_message_rect = score_message.get_rect(center = (480,355))
      screen.blit(game_name, game_name_rect)

      if score == 0:
         screen.blit(game_message,game_message_rect)
      else:
         screen.blit(score_message, score_message_rect)   



   #keys = pygame.key.get_pressed() #like a dictonary
   #if keys[pygame.K_SPACE]:
      #print('jump')



   #if figure_rect.colliderect(bush_rect):
    #  print('collision')

   #mouse = pygame.mouse.get_pos()
   #if figure_rect.collidepoint(mouse):
    #  print(pygame.mouse.get_pressed())
      


   pygame.display.update()#this updates the display
   #don't really have to think about it after you run it
   #we get an error of video system not initialised since quit method/function and hte first one can't work together.
   # one initialises, and the other uninitiliases it
   clock.tick(60)#while loop shouldn't run faster than 60 times per second so game doesn't go too fast
   #min frame rate isn't imp for us now since we're doing a simple game
   

   ####################################################

   #frame rate can fluctuate. depends on computer and game. 
   #fps talks abt speeed. we want the frame rate to be constant so that the speed is constant
   # 60 fps is nice. hard to tell the floor tho
