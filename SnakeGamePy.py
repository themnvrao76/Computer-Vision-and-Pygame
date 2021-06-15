import pygame
from Pose import HandPose
import random
import time
import cv2
pygame.init()
cam=cv2.VideoCapture(0)

cx=0;cy=0
h=HandPose()

velx=0
vely=0
snakelist=[]
snakelen=1
display_width=640
display_height=480
display=pygame.display.set_mode((display_width,display_height))

x=55;y=55

width=25
height=25
apple_width=25
apple_height=25
gamedelay=10

applex=round(random.randrange(0,display_width-apple_width)/5)*5
appley=round(random.randrange(0,display_height-apple_height)/5)*5
gameover=False
font=pygame.font.SysFont(None,25)
clock=pygame.time.Clock()



def snake(width,snakelist):
    for xny in snakelist:
        pygame.draw.rect(display,(0,255,0) ,(xny[0],xny[1],width,width))


# def message(msg,color):
#     screen_text=font.render(msg,True,color)
#     display.blit(screen_text,[15,15])

while not gameover:
	# OPENCV WORK ->>>>>>>>>>>>>>>
	_,img=cam.read()
	rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	h.coordinate(rgb,img)
	cx,cy=h.position(rgb)
	cv2.imshow("img",img)

	if cv2.waitKey(1)==27:
		break
	# OPENCV WORK ->>>>>>>>>>>>>>>
	pygame.time.delay(gamedelay)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameover=True
	keys=pygame.key.get_pressed()
	mylist=[keys[pygame.K_LEFT]]
	# print(cx,cy)

	if cx>1 and cx<150:
	    velx=-5 
	    vely=0

	if  cx>350 and cx <630 :
	    velx=5
	    vely=0

	if cy>1 and cy<230 :
	    vely=-5
	    velx=0

	if cy>450:
	    vely=5
	    velx=0
	if x>=display_width or x<0  or y>=display_height or y<0:
	    gameover=True
	if x == applex and y ==appley or x == applex+10 and y ==appley+10 or x == applex-10 and y ==appley-10 or  x == applex+10 and y ==appley-10 or  x == applex-10 and y ==appley+10:
	    applex=round(random.randrange(0,display_width-apple_width)/5)*5
	    appley=round(random.randrange(0,display_height-apple_height)/5)*5
	    snakelen=snakelen+5
	# if snakelen>=10:
	#     gamedelay=20
	# if snakelen>=20:
	#     gamedelay=10
	display.fill((0,0,0))
	pygame.draw.rect(display,(255,255,255),(applex+5,appley+5,20,20))

	snakehead=[]
	snakehead.append(x)
	snakehead.append(y)
	snakelist.append(snakehead)
	if len(snakelist) > snakelen:
	    del  snakelist[0]
	if snakehead in snakelist[:-1]:
	    gameover=True
	snake(width,snakelist)
	x=x+velx
	y=y+vely
	print(x,y,applex,appley)
	screen_text=font.render(f"Score {snakelen}",True,(255,255,255))
	display.blit(screen_text,[15,15])

	pygame.display.update()
    # clock.tick(100)
pygame.display.update()
pygame.quit()
quit()
cv2.destroyAllWindows()
cam.release()
