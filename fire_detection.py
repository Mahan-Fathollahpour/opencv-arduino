#IMPORT LIBRARIES
import cv2
import serial
import time

#setup haarcascade file
fire_cascade = cv2.CascadeClassifier('fire.xml')
#setup the port which Arduino is connected to it
Arduino = serial.Serial('COM4',9600)
#setup webcam to capture
cap = cv2.VideoCapture(0) 
#start the loop mode :
while True:
    ret,frame = cap.read() 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    fire = fire_cascade.detectMultiScale(frame, 12,8) #for detecting fire from xml file
    for (x,y,w,h) in fire:
        #insert rectange where the fire detected
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        print( 'Fire!!!') 
        Arduino.write(str.encode('f')) 
        time.sleep(0.2) 
        
    cv2.imshow('result', frame)
    Arduino.write(str.encode('s')) 
    k = cv2.waitKey(100) & 0xff
    #press ESC to Exit >>>
    if k == 27:
       break
#close the port and webcam
Arduino.close()
cap.release()
cv2.destroyAllWindows()