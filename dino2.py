import pygame
from sys import exit
from random import randint

score = 0
high_score = 0

def display_score():
   current_time = int(pygame.time.get_ticks() / 1000) - start_time #dividing by 1000 to get numbers in 1 2 3
   score_surf = font.render(f'{current_time}',False,(1,50,25))#we have to put it in f string becuase it doest accept integers
   score_rect = score_surf.get_rect(center= (475,50))
   screen.blit(score_surf,score_rect)
   return current_time

def obstacle_movement(bush_list):
   if bush_list:
      for bush_rect in bush_list:
         bush_rect.x -= 5       #########

         screen.blit(bush,bush_rect)
      bush_list = [obstacle for obstacle in bush_list if obstacle.x > -100]
      return bush_list
   else:
      return []

def collisions(figure,obsticles):
   if obsticles:
      for bush_rect in obsticles:
         if figure.colliderect(bush_rect):
            return False
   return True                            

def figure_animation():
   global figure,figure_index

   if figure_rect.bottom < 300:
      figure = figure_jump
   else:
      figure_index += 0.1 #small increments to change walk
      if figure_index >= len(figure_walk):
         figure_index = 0
      figure = figure_walk[int(figure_index)]

def reset_game():
    global game_active, start_time, score, high_score
    # Update high score if current score is greater
    if score > high_score:
        high_score = score
    score = 0
    game_active = False

pygame.init()
screen = pygame.display.set_mode((1000,400))
color = (173,216,230)
screen.fill(color)

jump_sound = pygame.mixer.Sound(r'C:\Users\Satyender B\OneDrive\Desktop\project\jump_sound.mp3')
jump_sound.set_volume(1.0)

pygame.mixer.music.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\totoro_audio.mp3')
pygame.mixer.music.set_volume(1.0)  # Adjust volume as needed
pygame.mixer.music.play(-1)



#the input is a tuple, and this will work for only 1 sec
#this is a display surface that shows up for a sec and then the code terminates
#a way to keep the code to keep running is to use a while loop
pygame.display.set_caption('Totoro jump')
clock = pygame.time.Clock() #clock object
font = pygame.font.Font('RobotoMono.ttf',30) #need to add font style here
game_active = False #change it to true later 
start_time = 0



sky_surface = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\disneyback.png').convert()
ground_surface = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\ground1.jpg').convert()
#convert converts the image to a format pygame can easily work with -> making it faster

#   score = font.render('My Game', False, (64,64,64))#rgb
#   score_rect = score.get_rect(center = (500,40))

bush1 = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\soot1.png').convert_alpha()
bush2 = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\soot2.png').convert_alpha()
bush_frames = [bush1, bush2]
bush_frame_index = 0
bush = bush_frames[bush_frame_index]

#bush_rect = bush.get_rect(bottomright = (800,333))

bush_rect_list = []


#for black and white stuff apparently?
figure_walk_1 = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\totoro left.png').convert_alpha()
figure_walk_2 = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\totoro walk.png').convert_alpha()
figure_walk = [figure_walk_1,figure_walk_2]
figure_index = 0 #to pick walk surface
figure_jump = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\totoro right.png').convert_alpha()

figure = figure_walk[figure_index]
figure_rect = figure.get_rect(midbottom = (80,364))
figure_gravity = 0

#game intro
figure_stand = pygame.image.load(r'C:\Users\Satyender B\OneDrive\Desktop\project\images\standing_totoro.png').convert_alpha()
figure_stand_rect = figure_stand.get_rect(center = (475,200))



game_name = font.render('Totoro Jump',False,(80,75,90))
game_name_rect = game_name.get_rect(center = (485,50))

game_message = font.render('Press space to run',False,(80,75,90))
game_message_rect = game_message.get_rect(center = (485,350))

bush_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bush_timer,2500)       ########

bush_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bush_animation_timer,500)




#test_surface = pygame.Surface((600,100))
#test_surface.fill('Red')

while True:
   for event in pygame.event.get():#gets events happening

      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

      if game_active:
         if event.type == pygame.MOUSEBUTTONDOWN:
            if figure_rect.collidepoint(event.pos) and figure_rect.bottom >= 365: 
               figure_gravity = -25
            
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and figure_rect.bottom >= 365:
               figure_gravity = -30    #########
               jump_sound.play()
      else:
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            start_time = int(pygame.time.get_ticks() / 1000)
            bush_rect_list.clear()

      if game_active: 
         if event.type == bush_timer:
            bush_rect_list.append(bush.get_rect(bottomright = (randint(950,1400),355))) #used to control distance between obstacles 
         
         if event.type == bush_animation_timer:
            bush_frame_index = (bush_frame_index + 1) % len(bush_frames)
            '''if bush_frame_index == 0:
               bush_frame_index = 1
            else:
               bush_frame_index = 0''' 
            bush = bush_frames[bush_frame_index]



   if game_active:
      screen.blit(sky_surface,(0,0))
      screen.blit(ground_surface,(0,340))#blit = block image transfer
      #pygame.draw.rect(screen,(24,64,26),score_rect,10)
      #screen.blit(score,score_rect)  
      score = display_score()

      #bush_rect.left -= 5 ########
      #if (bush_rect.left <- 100): 
      #   bush_rect.left = 800
      #figure_rect.left += 2 ##########
      #screen.blit(bush, bush_rect)
      # Debug: Draw the rectangles to check collision areas
      #pygame.draw.rect(screen, (255, 0, 0), figure_rect, 2)  # Red box around figure
      #for bush_rect in bush_rect_list:
      #   pygame.draw.rect(screen, (0, 255, 0), bush_rect, 2)  # Green box around bushes


      gravity_increment = 1  # How fast the character falls
      jump_strength = -25    # How strong the jump is

      # Update the figure's position
      if game_active:
         figure_gravity += gravity_increment
         figure_rect.y += figure_gravity

         # Prevent the character from falling below the ground
         if figure_rect.bottom >= 365:
            figure_rect.bottom = 365  # Set the bottom to ground level
            figure_gravity = 0
            
         figure_animation()   
         screen.blit(figure,figure_rect)

      bush_rect_list = obstacle_movement(bush_rect_list)
      game_active = collisions(figure_rect,bush_rect_list)

      #if bush_rect.colliderect(figure_rect) and figure_rect.bottom == 365:
      #   game_active = False


   else:
      if score > high_score:
        high_score = score
        
      screen.fill((144,163,161)) #(12,38,27) optional
      screen.blit(figure_stand,figure_stand_rect)
      bush_rect_list.clear()
      figure_rect.midbottom = (80,364)
      figure_gravity = 0

      score_message = font.render(f'Your Score: {score}',False,(80,75,90))
      score_message_rect = score_message.get_rect(center = (480,320))
      high_score_message = font.render(f'High Score: {high_score}', False, (80, 75, 90))
      high_score_message_rect = high_score_message.get_rect(center=(480, 350))
      screen.blit(game_name, game_name_rect)
      

      if score == 0:
         screen.blit(game_message,game_message_rect)
      else:
         screen.blit(score_message, score_message_rect)
         screen.blit(high_score_message, high_score_message_rect)




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
