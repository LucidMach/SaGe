import cv2
import numpy as np
import face_recognition as fr
import serial
from gpiozero import LED
from numpy import savetxt
from numpy import loadtxt

inFace = "images/"+input("Enter path to Face: ")
mode = input("Enter Mode [2 for rPI, 1 for arduino, 0 for null]: ")
outFace = loadtxt("faEnc.csv", delimiter=",")

imgTs = fr.load_image_file(inFace)
imgTs = cv2.cvtColor(imgTs, cv2.COLOR_BGR2RGB)


def faceAdd(fa):
    imgTr = fr.load_image_file("images/"+fa)
    imgTr = cv2.cvtColor(imgTr, cv2.COLOR_BGR2RGB)
    faLocTr = fr.face_locations(imgTr)[0]
    outFace = fr.face_encodings(imgTr)[0]
    cv2.rectangle(imgTr, (faLocTr[3], faLocTr[0]),
                  (faLocTr[1], faLocTr[2]), (255, 0, 255), 2)
    savetxt("faEnc.csv", outFace, delimiter=',')


# faceAdd("suraj.jpg")

faLocTs = fr.face_locations(imgTs)[0]
faEncTs = fr.face_encodings(imgTs)[0]
cv2.rectangle(imgTs, (faLocTs[3], faLocTs[0]),
              (faLocTs[1], faLocTs[2]), (255, 0, 255), 2)
result = fr.compare_faces([outFace], faEncTs)

if result[0] == True:
    result = "H" # nodemcu problem high = low 
else:
    result = "L" # nodemcu problem low = high
accu = fr.face_distance([outFace], faEncTs)
print(result)
print(accu*100, "Accuracy")

if(mode == "1"):
    port = "COM5"
    Brate = 9600
    a = result
    se = serial.Serial(port,Brate)
    if a == "H":
        se.write(b"H")
    elif a == "L":
        se.write(b"L")
    se.close()    
if(mode == "2"):
    l = LED(22)
    if(result == "H"):
        l.on()
    else:
        l.off()

cv2.imshow("ElonTest", imgTs)
cv2.waitKey(0)
