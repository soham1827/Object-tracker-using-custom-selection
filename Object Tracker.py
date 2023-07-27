import cv2

cap = cv2.VideoCapture("project_video_Trim.mp4")
#cv2.VideoCapture(0)

#tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerBoosting()
success, frame = cap.read()
bb = cv2.selectROI("Tracking",frame,False)
tracker.init(frame,bb)



def drawbox(frame,bb):
	x, y , w, h = int(bb[0]),int(bb[1]),int(bb[2]),int(bb[3])
	cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,255),3,1)
	cv2.putText(frame,"Tracking",(75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2)



while True:
	timer = cv2.getTickCount()
	success, frame = cap.read()

	success,bb = tracker.update(frame)
	if success:
		drawbox(frame,bb)
	else:
		cv2.putText(frame,"LOST",(75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)


	fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

	cv2.putText(frame,str(int(fps)),(75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)

	cv2.imshow("Tracking",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()