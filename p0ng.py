import pygame
import random
pygame.init()
display_x=1000
display_y=500
win=pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('p0ng')
rect_x=20
rect_y=220
second_rect_x=display_x-40
second_rect_y=220
width=20
height=60
vel=10
white=(225,225,225)
daimeter=10
centre_x=display_x//2
centre_y=random.randint(1,50)*10
is_shoot=False
shoot_vel=10
shoot_vel_x=10
L_0r_R=random.randint(0,1)
line_x=display_x//2
line_y=display_y
run=True
while run:
	pygame.time.delay(40)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	key=pygame.key.get_pressed()
	if key[pygame.K_w] and rect_y>0:
		rect_y-=vel
	if key[pygame.K_s] and rect_y+height<500:
		rect_y+=vel
	if key[pygame.K_UP] and second_rect_y>0:
		second_rect_y-=vel
	if key[pygame.K_DOWN] and second_rect_y+height<500:
		second_rect_y+=vel
	if key[pygame.K_SPACE]:
		is_shoot=True
	if is_shoot:
		if L_0r_R:
			shoot_vel_x*=-1
			L_0r_R=0
		centre_y+=shoot_vel
		centre_x+=shoot_vel_x
		if centre_y+daimeter==500:
			shoot_vel*=-1
		if centre_y-daimeter==0:
			shoot_vel*=-1
		if rect_x+width==centre_x-daimeter and centre_y>rect_y-5 and centre_y<rect_y+height:
			shoot_vel_x*=-1
		if second_rect_x==centre_x+daimeter and centre_y>second_rect_y-5 and centre_y<second_rect_y+height:
			shoot_vel_x*=-1
	pygame.draw.rect(win,white,(rect_x,rect_y,width,height))
	pygame.draw.rect(win,white,(second_rect_x,second_rect_y,width,height))
	if is_shoot:
		pygame.draw.circle(win,white,(centre_x,centre_y),(daimeter))
	pygame.draw.line(win,white,(line_x,0),(line_x,line_y))
	pygame.display.update()
	win.fill(0)