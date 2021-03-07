from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import time
import pyglet

go = True
first = True

#-----Changeable Variables-----
global thresh
thresh = 0.25
global frame_check
frame_check = 10
#-----Getting Face Models-----
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor(".\shape_predictor_68_face_landmarks.dat")# Dat file is the model used to find the eyes.
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(1)
flag=0
#-----Variables for Data Analysis-----
global eyeAvg
eyeAvg = 0
global frameTen
frameTen = 1
global eyeAvgArray
eyeAvgArray = []
#-----Sound-----
def alarm():
	print("beep")
#-----EAR Calculations-----
def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (C * 2.0)
	return ear
#-----EAR Part 2-----
def getEAR():
	global leftEye
	global rightEye
	shape = predict(gray, subject)
	shape = face_utils.shape_to_np(shape)#converting to NumPy Array
	leftEye = shape[lStart:lEnd]
	rightEye = shape[rStart:rEnd]
	leftEAR = eye_aspect_ratio(leftEye)
	rightEAR = eye_aspect_ratio(rightEye)
	ear = (leftEAR + rightEAR) / 2.0
	return ear
#-----Drawing the lines around the eyes-----
def drawContoursInFrame():
	leftEyeHull = cv2.convexHull(leftEye)
	rightEyeHull = cv2.convexHull(rightEye)
	cv2.drawContours(frame, [leftEyeHull], -1, (40, 49, 222), 1)
	cv2.drawContours(frame, [rightEyeHull], -1, (40, 49, 222), 1)
#-----Display Warnings When Drowsy-----
def displayWarnings():
	cv2.putText(frame, "WAKE UP!!!", (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	cv2.putText(frame, "WAKE UP!!!", (10,325),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	alarm()

#-----Main Program-----
def mainLoop():
	global go
	global flag
	cap=cv2.VideoCapture(1)
	while go == True:
		global gray
		global subjects
		global frame
		global eyeAvg
		global subject
		global frameTen
		ret, frame = cap.read()
		frame = imutils.resize(frame, width=450)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		subjects = detect(gray, 0)
		for subject in subjects:
			#ear = getEAR()
			#drawContoursInFrame()
			shape = predict(gray, subject)
			shape = face_utils.shape_to_np(shape)#converting to NumPy Array
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)
			ear = (leftEAR + rightEAR) / 2.0
			eyeAvg += ear 
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (40, 49, 222), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (40, 49, 222), 1)
			if frameTen % 50 == 0:
				eyeAvgTen = (eyeAvg/50)
				print(frameTen,eyeAvgTen)
				eyeAvgArray.append(round(eyeAvgTen,2))
				eyeAvg = 0
				frameTen = 0
			if ear < thresh:
				flag += 1
				print (flag)
				if flag >= frame_check:
					displayWarnings()
					sound = pyglet.media.load(r"alarm.wav", streaming=False)
					sound.play()
					print("warning")
			else:
				flag = 0
			frameTen += 1
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			go = False
			return str(eyeAvgArray)
		else:
			go = True
#-----InitiatingMainLoop TO-DO: PUT THIS IN A FUNCTION WHEN IMPORTING IN FUTURE-----
# while go == True:
# 	mainLoop()
#mainLoop()
#-----Close the Windows-----
def destroyWindows():
	cap.release()
	cv2.destroyAllWindows()
#-----At this point something triggered a break in the main loop meaning its time to stop the program-----
destroyWindows()
#-----This function is for testing and will be obsolete with Firebase integration
def getEyeData():
	return str(eyeAvgArray)
getEyeDataTest = getEyeData()
#----------
def TEST():
	return(thresh)
