# AI_Python

Repozytorium zawiera moje poczatki ze sztuczną inteligencja. Składa się z:
- Bazy danych kwiata Irys z 3 rodzajami. Sztuczna inteligencja rozponaje je przy pomocy biblioteki ski-learn (Light GBM, sieci nuronowe). Jest to wysokopoziomowa biblioteka.
- Baza danych raka piersi:
  Baza zawierająca pomiary badań piersi (ski-learn (drzewo decyzyjne, regresja liniowa, Lasy losowe, Najbliżsi sąsiedzi)
  Baza zawierająca zdjęcia komórek kanałów sutkowych. Baza zawiera dane 277,524 próbki wymiary 50x50 198,738 IDC negatywnych i 78,786 IDC pozytywne. AI w bib. PyTorch.




Artifical Inteligence (Python) consist of:
Dataset Iris consist of 3 types Iris flower. AI learn how to tell the difference with IRIS flowers. This was my first AI project (secound, first was NILM and Matlab), so i used basic method to make a goal.Algorithms: (Light GMB, Neutral Networks)


Breast Cancer - 
- Sci-kit Learn (High level lib. Used Decission Tree, m. Regression,m. RandomForestClasifier, m. Neighbors) Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.


Source:
Creators:
1. Dr. William H. Wolberg, General Surgery Dept.
University of Wisconsin, Clinical Sciences Center
Madison, WI 53792
wolberg '@' eagle.surgery.wisc.edu

2. W. Nick Street, Computer Sciences Dept.
University of Wisconsin, 1210 West Dayton St., Madison, WI 53706
street '@' cs.wisc.edu 608-262-6619

3. Olvi L. Mangasarian, Computer Sciences Dept.
University of Wisconsin, 1210 West Dayton St., Madison, WI 53706
olvi '@' cs.wisc.edu

Donor:
Nick Street


2. Pytorch dataset 
Context
Invasive Ductal Carcinoma (IDC) is the most common subtype of all breast cancers. To assign an aggressiveness grade to a whole mount sample, pathologists typically focus on the regions which contain the IDC. As a result, one of the common pre-processing steps for automatic aggressiveness grading is to delineate the exact regions of IDC inside of a whole mount slide.

Content
The original dataset consisted of 162 whole mount slide images of Breast Cancer (BCa) specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted (198,738 IDC negative and 78,786 IDC positive). Each patch’s file name is of the format: uxXyYclassC.png — > example 10253idx5x1351y1101class0.png . Where u is the patient ID (10253idx5), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-IDC and 1 is IDC.

Acknowledgements
The original files are located here: http://gleason.case.edu/webdata/jpi-dl-tutorial/IDC_regular_ps50_idx5.zip
Citation: https://www.ncbi.nlm.nih.gov/pubmed/27563488 and http://spie.org/Publications/Proceedings/Paper/10.1117/12.2043872

Inspiration
Breast cancer is the most common form of cancer in women, and invasive ductal carcinoma (IDC) is the most common form of breast cancer. Accurately identifying and categorizing breast cancer subtypes is an important clinical task, and automated methods can be used to save time and reduce error.

https://www.kaggle.com/paultimothymooney/breast-histopathology-images
