#program na nalezeni medveda pomoci kamery 
from ultralytics import YOLO
import numpy as np
import cv2 
import cvzone
import urllib.request

url = 'http://192.168.137.92/cam-hi.jpg'#url adresa esp cam 
model = YOLO('yolov8n.pt')#zvoleni jaky model se pouzije 
classesfile='coco.names'
classNames=[]
with open(classesfile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')
object_id = classNames.index('pottedplant')# zjisti class id objektu co hledam
cap = cv2.VideoCapture(url)#nacte video z kamery do promene 
cap.set(3,720)#sirka okna s videem
cap.set(4,480)#vyska okna s videem
while True:
    # Read a frame from the video stream
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    #ret, frame = cap.read()
    im = cv2.imdecode(imgnp,-1)
    results = model(im, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])#zjisti classu objektu 
            if object_id == cls:#pokud se classa objektu shoduje s objektem co hledam stane se nasledujici 
                x1,y1,x2,y2 = box.xyxy [0] #x1 je pozice leveho horniho rohu objektu v ose x, x2 je velikost objektu v ose x v px 
                x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)#prevedeni hodnot na int pro lepsi praci s nima 
                print('X=',x1,'Y=',y1,'W=',x2,'H=',y2)#vypisuje velikost objektu a jeho polohu v px 
                center_x,center_y = x1+(x2/2),y1+(y2/2)#vypocet stredu objektu pro lepsi lokalizaci medveda
                center_x,center_y = int(center_x), int(center_y)#prevede hodnoty na int aby se dali pouzit ve funkci ukazujici stred  
                print('center:',center_x,center_y)#vypise udaje 
                cv2.rectangle(im,(x1,y1),(x2,y2),(255,0,255),3)#nakresli box okolo detekovane veci 
                conf = box.conf[0]#jistota modelu 
                conf = float(conf*100)
                rounded_conf = int(conf)#zaokrouhli jistotu modelu na dve desetina mista 
                print('confidence:',rounded_conf)
                #class names 
                cv2.circle(im, (center_x,center_y),10, (255,0,255), thickness=-1)
                cls = int(box.cls[0])#ulozi classu daneho objektu do promenne 
                cvzone.putTextRect(im, f'{classNames[cls]}{rounded_conf}',(max(0,x1), max(35,y1)))#vykresli nazev classy objektu spolecne s confidence do videa 
                print(classNames[cls])#vypise klassu objektu
    cv2.imshow('footage',im)
    key=cv2.waitKey(1000)
    if key==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
