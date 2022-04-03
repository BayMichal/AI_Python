from os import system
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
from scipy.stats import skew
from scipy.stats import kurtosis
import cv2
import matplotlib.pyplot as plt


def main():

    err_list=[]
    error_png=0
    black_error_png = 0
    h=0
    test_path = './*.png'
    path = './breast-histopathology-images/IDC_regular_ps50_idx5/*/*/*'

    test_x = 0
    ilosc_plk = 0

    for file in glob.glob(path):
        with Image.open(file) as im:

            extrema = im.convert("L").getextrema()
            if extrema[0] == extrema[1]:
                black_error_png+=1
                continue
            else:
                width, height = im.size
                if(width == 50 and height == 50):
                    image = cv2.imread(file,0)
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                    cl1 = clahe.apply(image)
                    cv2.imwrite(file,cl1)
                    #print(file)
                    
                    res = re.findall("(\d+)_idx", file)
                    if(test_x != res[1]):
                        test_x = res[1]
                        ilosc_plk += 1
                        print(ilosc_plk)
                        print(test_x)
                        print("\n")


                    if ( res[1] == 9077):
                        break

                    #debug_printer(data)
                    #logger(data)
                else:
                    error_png+=1
            
        im.close()

        


        

if __name__ == "__main__":
    main()
