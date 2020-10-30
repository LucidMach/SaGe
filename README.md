# SaGe
## (Safe-Gate)
> A Face Recognition based Security System

### What Is SAGE? 
Safe-gate is a doorlock system which uses face recognition to unlock a door.
It can be used through a web-app(IoT) or even simply rigged to a camera on a door

### How To Install & Use?
1. clone/download the repo
2. run the command in conda prompt 
	> conda env create --file sage.yml 
3. activate sage through conda
4. run and enjoy

### How It Works?
1. It constantly checks a directory for images, either from cam/web-server.
2. It extracts face-encodings from the image, and moves the image out of the dir.
3. It compares encoding matrix with the registered(stored encoded) matrices
4. It writes the output to a serial port & gpio
