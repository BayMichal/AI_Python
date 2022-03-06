import re
import numpy as np
from PIL import Image
import colorsys
import glob
import matplotlib
import pandas as pd
from pandas import DataFrame as df
import statistics
from tabulate import tabulate
import os.path
import time, sys
from tqdm import tqdm

jest = "class1.png"
niema = "class0.png"

def debug_printer(data):
        print("----------------------------------------------------------------------------------------------")
        print(tabulate([['Srednie arytmetyczne', data[0], data[1], data[2]],
        ['Dominanty',                            data[3], data[4], data[5]],
        ['Odchylenie standardowe',               data[6], data[7], data[8]],
        ['Wariacje',                             data[9], data[10], data[11]],
        ['ID    ',                               data[12],data[13], "   "]],
        headers=["Operation", "H", "S", "V"]))
        print("-----------------------------------------------------------------------------------------")


def logger(data):
    for i in range(len(data)):
        print(str(data[i])+',', end='')

  

def main():
    #Sumy
    _h = 0
    _s = 0
    _v = 0
    

    h=0
    test_path = './*.png'
    path = './breast-histopathology-images/IDC_regular_ps50_idx5/*/*/*'

  
    print("srH"+','+"srS"+','+"srV"+','+"dH"+','+"dS"+','+"dV"+','+"odH"+','+"odS"+','+"odV"+','+"wH"+','+"wS"+','+"wV"+','+"id"+',',  end='')
    print("class")


    for file in glob.glob(path):
        with Image.open(file) as im:
            zH = []
            zS = []
            zV = []
            im = im.resize((50,50),Image.ANTIALIAS)
            hsv_data = matplotlib.colors.rgb_to_hsv((np.array(im)/255.)) 
            for y in range(0,50):
                for x in range(0,50):
                    for z in range(0,3):
                        # Sumy HSV
                        print
                        #Jesli wymiar H, to pakuj tylko te ktore powinny być H (2500)
                        if( z == 0 ):
                            #_h += hsv_data[x][y][z]
                            zH.append(hsv_data[x][y][0])

                        #Jesli wymiar S, to pakuj tylko te ktore powinny być S (2500)
                        if( z == 1 ):
                            #_s += hsv_data[x][y][z]
                            zS.append(hsv_data[x][y][1])
                        
                        #Jesli wymiar Z, to pakuj tylko te ktore powinny być V (2500)
                        if( z == 2):
                            #_v += hsv_data[x][y][z]
                            zV.append(hsv_data[x][y][2])
                        
                        #print(str(hsv_data[x][y][z])+',', end='')
             #Srednia
            srH = statistics.mean(zH)
            srS = statistics.mean(zS)
            srV = statistics.mean(zV)
            
            #Dominanta
            dH = statistics.mode(zH)
            dS = statistics.mode(zS)
            dV = statistics.mode(zV)

            #Odchylenie Standardowe
            odsH = statistics.stdev(zH)
            odsS = statistics.stdev(zS)
            odsV = statistics.stdev(zV)

            #Wariancja
            warH = statistics.variance(zH, xbar=None)
            warS = statistics.variance(zS, xbar=None)
            warV = statistics.variance(zV, xbar=None)
            
            data = [srH, srS, srV, dH, dS, dV, odsH, odsS, odsV, warH, warS, warV]

            #ID pacjenta
            
            res = re.findall("(\d+)_idx", file)
            data.append(res[1])

            for i in range(0,len(data)):
                print(str(data[i])+',', end='')
                 
            if jest in file:
                print('y')
            if niema in file:
                print('n')
            

            #debug_printer(data)
            #logger(data)
            

        im.close()
        


        

if __name__ == "__main__":
    main()






        




	





