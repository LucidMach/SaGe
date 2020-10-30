import os,fnmatch

inPath = "C:/Users/nukal/OneDrive/Pictures/Camera Roll"
outPath = "C:/Users/nukal/dev/SaGe/images"
files = os.listdir(inPath)
ext =  "*.jpg"
for file in files:
    if fnmatch.fnmatch(file,ext):
        print(file)
        os.rename(inPath+"/"+file,outPath+"/"+file)