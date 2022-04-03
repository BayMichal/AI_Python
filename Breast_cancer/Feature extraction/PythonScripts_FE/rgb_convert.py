import glob
from PIL import Image
import os.path
import numpy as np

path = './pre-processing/*/*/*'

for i in range(0, 50*50*3):
    print("c"+str(i)+',', end='')

print("class")

rak="class1.png"
nierak= "class0.png"
i=0


for file in glob.glob(path):
    with Image.open(file) as img:
        data=0
        img = img.resize((50,50),Image.ANTIALIAS)
        data = np.array(img)
        
        for y in range(0,50):
            for x in range(0,50):
                for z in range(0,3):
                    print(str(data[x][y][z])+',', end='')                    
        
        if rak in file:
            print("y")
        if nierak in file:
            print("n")

