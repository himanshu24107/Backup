import cv2 
ss = cv2.CascadeClassifier('stop_sign.xml') #Sorce:Internet

cap = cv2.VideoCapture("stop.mp4")

cap.set(4, 480)
cap.set(3,360)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Screen', img)
    SS = ss.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,x) in SS:
        print("Stop! Stop! Stop!")
    key = cv2.waitKey(30)
    if key == ord('x'):
        cap.release()
        cv2.destroyAllWindows
        break