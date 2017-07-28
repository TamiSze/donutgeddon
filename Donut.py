import Tkinter as Tk
import pygame
from random import randint

background = pygame.image.load('lard_lad_donuts_new.png')
#quelle http://theawesomedaily.com/homer-simpson-famous-donut-recipe/
game_on_background = pygame.image.load('game_on_background.png')
#other background, trashcan: http://vignette2.wikia.nocookie.net/simpsonstappedout/images/b/b4/Garbage_Can_Pack_Menu.png/revision/latest?cb=20160707213053
doh = pygame.image.load('Homer_Doh.png')
width = 640
height = 480
running = True
game_on = False
checker_active = 1
path_taken = 0
points = 0
lives = 3
speed = 3
counter = 0
difficulty = 9
difficulty_text = 'easy'
ball_x = (width/10)*2
ball_y = (height/7)*3
catcher_image = pygame.image.load('Catcher.png')
# Tami hat hier was geaendert
#checker = False
catcher_mouth_open_image = pygame.image.load('Catcher_mouth_open.png')
#
donut_image = pygame.image.load('Donut.png')
heart_image = pygame.image.load('Heart.png')
thrower_image = pygame.image.load('Thrower.png')
# Tami hat hier was geaendert
thrower_count = 0
donut_fly1 = pygame.image.load('Donut_fly1.png')
donut_fly2 = pygame.image.load('Donut_fly2.png')
donut_fly3 = pygame.image.load('Donut_fly3.png')
donut_fly4 = pygame.image.load('Donut_fly4.png')
donut_fly5 = pygame.image.load('Donut_fly5.png')
donut_fly_list =[donut_fly1,donut_fly2,donut_fly3,donut_fly4,donut_fly5]
fly_count=0
homer_eats_imgs = ['Catcher_mouth_open.png','Catcher_eating.png']
homer_eats = {}
for img in homer_eats_imgs:
	homer_eats[img] = pygame.image.load(img)
thrower_images = ['Thrower_breath_in.png','Thrower_shooting.png']
thrower_list = {}
for img in thrower_images:
	thrower_list[img] = pygame.image.load(img)
##
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init

	
def engine():
	pygame.init
	screen.fill((game_on_background))
	draw_objects()

def draw_objects(): 
	draw_points()
	if game_on==True:
		if path_taken == 0:
			thrower_new_image = pygame.transform.rotate(thrower_image,20)
		if path_taken == 1:
			thrower_new_image = thrower_image
		if path_taken == 2:
			thrower_new_image = pygame.transform.rotate(thrower_image,340)
		screen.blit(thrower_new_image,((width/13)*2,((height/8)*3)))
		#tami: rotation ist nur hier moeglich
		global fly_count
        screen.blit(donut_fly_list[fly_count],(ball_x,ball_y))
        if fly_count == 4:
        	fly_count = 0
        else:
        	fly_count = fly_count + 1
        if checker_active == 0:
			screen.blit(catcher_image,((width/10)*8,((height/7))))
       	if checker_active == 1:
       		screen.blit(catcher_image,((width/10)*8,((height/7)*3)))	
       	if checker_active == 2:
       		screen.blit(catcher_image,((width/10)*8,((height/7*5))))
       		
	if game_on == False:
		text = myfont.render('Press Space to start', False, (255, 255, 255))
		diff = myfont.render('difficulty:  ' + difficulty_text, False, (255,255,255))
		screen.blit(diff,(width/4, height/4))
		screen.blit(text,(width/4, height/2))			
    

def on_ball_reset():
	global ball_x
	global ball_y
	global counter
	global speed
	if (counter == difficulty):
		speed = speed + 1
		counter = 0
	print speed
	ball_x = (width/10)*2
	ball_y = (height/7)*3
	random_number()
	pygame.display.flip()
	#kanone feuert ab
	for img in thrower_images:
		if path_taken == 0:
			thrower_new_image = pygame.transform.rotate(thrower_list[img],20)
		if path_taken == 1:
			thrower_new_image = thrower_list[img]
		if path_taken == 2:
			thrower_new_image = pygame.transform.rotate(thrower_list[img],340)
		screen.blit(thrower_new_image,((width/13)*2,((height/8)*3)))
		pygame.display.flip()
		clock.tick(5)
	####
def draw_points(): 
	screen.blit(donut_image,((width/10),((height/10))))
	text_donut = myfont.render(("" + str(points)), False, (255, 255, 255))
	screen.blit(text_donut,((width/20)*1,((height/10)-10)))
	screen.blit(heart_image,((width/10),((height/10)*2)))
	text_heart = myfont.render(('' + str(lives)), False, (255, 255, 255))
	screen.blit(text_heart,((width/20)*1,(((height/10)*2)-10)))
		
def random_number():
	global path_taken
	path_taken = randint(0,2)
		
def setup_game():
	global points
	global lives
	points = 0
	lives = 3
	on_ball_reset()

def life_loss():
	global lives
	global ball_x
	global game_on
	if game_on:
		#Hier wird Doh Bild (und evtl. Ton) eingefuegt
		screen.blit(doh,(width/10,0))
		pygame.display.flip()
		clock.tick(2)
		######
		if lives == 0:
			on_ball_reset()
			game_on = False
		else:
			lives = lives -1 
			on_ball_reset()

def ball_move():
	global ball_x
	global ball_y
	if ball_x >= width:
		life_loss()
	else:
		ball_x = ball_x+speed
	if path_taken == 0:
		ball_y = ball_y-(speed/3)
	if path_taken == 2:	
		ball_y = ball_y+(speed/3)

		
def check_caught():
	global points
	global counter
	if (ball_x >= (width/20)*15):
		if (ball_x <= (width/20)*17):
			if (path_taken == checker_active):	
				points = points + 1
				counter = counter + 1
				# Homer Ess Animation
				for img in homer_eats_imgs:
					if checker_active == 0:
						screen.blit(homer_eats[img],((width/10)*8,((height/7))))
					if checker_active == 1:
						screen.blit(homer_eats[img],((width/10)*8,((height/7)*3)))	
					if checker_active == 2:
						screen.blit(homer_eats[img],((width/10)*8,((height/7)*5)))
					pygame.display.flip()
					clock.tick(7)
				####
				on_ball_reset()
	
	
def change_difficulty():
	global difficulty
	global difficulty_text
	if difficulty == 9:
		difficulty = 6
		difficulty_text = 'medium'
	else:
		if difficulty == 6:
			difficulty = 3
			difficulty_text = 'hard'
		else:
			if difficulty == 3:
				difficulty = 9
				difficulty_text = 'easy'	
		
		
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			if game_on == False:
				setup_game()
				game_on = True
			else:
				check_caught()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			if game_on == True:
				if checker_active > 0:
					checker_active = checker_active-1
		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			if game_on == True:
				if checker_active < 2:
					checker_active = checker_active+1
	
		if event.type == pygame.MOUSEBUTTONUP:
			mpos = pygame.mouse.get_pos()
			change_difficulty()
					
	ball_move()
	if game_on == False:
		screen.blit(background,(0,0))
	else:
		screen.blit(game_on_background,(0,0))
	#screen.fill((background))
	draw_objects()
	pygame.display.flip()
	clock.tick(60)
