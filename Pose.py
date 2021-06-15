import mediapipe as mp
import cv2

class HandPose():
	def __init__(self):
		self.handmp=mp.solutions.hands
		self.hand=self.handmp.Hands()
		self.mpdraw=mp.solutions.drawing_utils
	def coordinate(self,img,img2):
		result=self.hand.process(img)
		h,w,c=img.shape
		if result.multi_hand_landmarks:
			for handsmarks in result.multi_hand_landmarks:
				for id,land in enumerate(handsmarks.landmark):
					cx,cy=int(land.x*w),int(land.y*h)
					
					if(id==8):
						
						cv2.circle(img2,(cx,cy),25,(255,0,255),cv2.FILLED)
				self.mpdraw.draw_landmarks(img2,handsmarks,self.handmp.HAND_CONNECTIONS)
	def position(self,img):
		result=self.hand.process(img)
		h,w,c=img.shape
		if result.multi_hand_landmarks:
			for handsmarks in result.multi_hand_landmarks:
				for id,land in enumerate(handsmarks.landmark):
					cx,cy=int(land.x*w),int(land.y*h)
					return cx,cy
		else:
			return -1,-1




if __name__ == '__main__':
	main()

