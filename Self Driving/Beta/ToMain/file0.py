# ENGINE PORT
# Himanshu_Dubey    Accuracy: 79%
import torch
import cv2

model = torch.hub.load('ultralytics/yolov5','yolov5n')

cap =cv2.VideoCapture(1)

while True:

    img = cap.read()[1]
    if img is None:
        break
    result = model(img)
    df = result.pandas().xyxy[0]

    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
         
        conf = df['confidence'][ind]
        text = label +' '+ str(conf.round(decimals=2))

        cv2.rectangle(img,(x1,y1), (x2,y2), (255,255,0),2)
        cv2.putText(img,text,(x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,0),2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()

cap2 =cv2.VideoCapture("output2.mp4")

while True:

    img = cap2.read()[1]
    if img is None:
        break
    result = model(img)
    df = result.pandas().xyxy[0]

    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
         
        conf = df['confidence'][ind]
        text = label +' '+ str(conf.round(decimals=2))

        cv2.rectangle(img,(x1,y1), (x2,y2), (255,255,0),2)
        cv2.putText(img,text,(x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,0),2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap2.release()
cv2.destroyAllWindows()

cap3 =cv2.VideoCapture("output.mp4")

while True:

    img = cap3.read()[1]
    if img is None:
        break
    result = model(img)
    df = result.pandas().xyxy[0]

    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
         
        conf = df['confidence'][ind]
        text = label +' '+ str(conf.round(decimals=2))

        cv2.rectangle(img,(x1,y1), (x2,y2), (255,255,0),2)
        cv2.putText(img,text,(x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,0),2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap3.release()
cv2.destroyAllWindows()
