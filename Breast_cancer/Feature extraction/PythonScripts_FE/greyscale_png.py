import glob
from PIL import Image
import os.path
import numpy as np

path = './pre-processing/*/*/*'

for i in range(0, 50*50):
    print("c"+str(i)+',', end='')

print("class")

rak="class1.png"
nierak= "class0.png"
i=0
black_error_png=0

for file in glob.glob(path):
    with Image.open(file) as img:
        extrema = img.convert("L").getextrema()
        if(extrema[0] == extrema[1]):
            black_error_png+=1
            continue
        else:
            width, height = img.size
            if(width == 50 and height == 50):
            #img = img.resize((50,50),Image.ANTIALIAS)
                data = np.array(img)

                for y in range(0,50):
                    for x in range(0,50):
                           print(str(data[y][x])+',', end='')                    
                
                if rak in file:
                    print("y")
                if nierak in file:
                    print("n")
            else:
                continue
    img.close()

