import cv2
import numpy as np
import face_recognition as fr
import serial, time
import os,fnmatch
from gpiozero import LED
from numpy import savetxt
from numpy import loadtxt
from datetime import datetime


class SaFe:
    # 0 : null, 1 : ard, 2 : rPI
    def __init__(self, mode=0):
        self.mode = mode
        self.img = ""
        self.dir = "C:/Users/nukal/dev/SaGe"  
        self.inPath = "C:/Users/nukal/Pictures/Camera Roll"
        self.outPath = "C:/Users/nukal/dev/SaGe/images/un"
        self.out =  "C:/Users/nukal/dev/SaGe/images"

    def faceLoad(self):
        self.files = os.listdir(self.inPath)
        self.ext =  "*.jpg"
        for file in self.files:
            if fnmatch.fnmatch(file,self.ext):
                os.rename(self.inPath+"/"+file,self.outPath+"/"+file)
                self.img = file

    def faceHandle(self):
        self.imgTs = fr.load_image_file(self.inFace)
        print(self.inFace)
        self.imgTs = cv2.cvtColor(self.imgTs, cv2.COLOR_BGR2RGB)
        self.faLocTs = fr.face_locations(self.imgTs)[0]
        self.faEncTs = fr.face_encodings(self.imgTs)[0]
        cv2.rectangle(self.imgTs, (self.faLocTs[3], self.faLocTs[0]),
                      (self.faLocTs[1], self.faLocTs[2]), (255, 0, 255), 2)

    def faceRecog(self):
        self.result = fr.compare_faces([self.outFace], self.faEncTs)
        if self.result[0] == True:
            self.result = "H"
        else:
            self.result = "L"
        self.accu = fr.face_distance([self.outFace], self.faEncTs)
        print(self.result)
        print(self.accu*100, "Accuracy")

    def faceAdd(self, fa, num):
        self.imgTr = fr.load_image_file("images/un/"+fa)
        self.imgTr = cv2.cvtColor(self.imgTr, cv2.COLOR_BGR2RGB)
        self.faLocTr = fr.face_locations(self.imgTr)[0]
        self.outFace = fr.face_encodings(self.imgTr)[0]
        cv2.rectangle(self.imgTr, (self.faLocTr[3], self.faLocTr[0]),
                      (self.faLocTr[1], self.faLocTr[2]), (255, 0, 255), 2)
        face = "faEnc"+str(num)+".csv"
        savetxt(face, self.outFace, delimiter=',')
    # remeber to add face to "un" directory
    def faceRequests(self):
        # self.inFace = "images/un/"+input("Enter path to Face: ")
        self.inFace = "images/un/" + self.img
        for i in range(10):
            csv = "faEnc"+str(i)+".csv"
            try:
                self.outFace = loadtxt(csv, delimiter=",")
                self.faceHandle()
                self.faceRecog()
            except:
                pass    

    def ardHandle(self, port, Brate):
        a = self.result
        se = serial.Serial(port,Brate)
        if a == "H":
            se.write(b"H")
        se.close()

    def rPihandle(self, pin):
        l = LED(pin)
        if(self.result == 1):
            l.on()
        else:
            l.off()
    
    def faceClear(self):
        self.files = os.listdir(self.outPath)
        self.ext =  "*.jpg"
        for file in self.files:
            if fnmatch.fnmatch(file,self.ext):
                os.rename(self.outPath+"/"+file,self.out+"/"+file)

    def test(self):
        try:
            self.faceLoad()
            if self.img != "":
                self.faceRequests()
                self.faceClear()
            # self.ardHandle("COM5",9600)
        except:
            time.sleep(0.1)
        

while True:
    s = SaFe()
    # s.faceAdd("elon.jpg", 1)
    s.img = "elon.jpg"
    s.faceRequests()