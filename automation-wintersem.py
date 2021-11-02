import os
from tkinter import filedialog
from tkinter import *
import shutil

root = Tk()
root.withdraw()
fs = filedialog.askdirectory()

os.chdir(fs)
os.mkdir("DEC")
os.mkdir("JAN")
os.mkdir("FEB")
os.mkdir("MAR")
os.mkdir("APR")

for i in os.listdir():
    fn, fe = os.path.splitext(i)
    l=fn.split("_")
    if len(l)>=9:
        for j in range(9,len(l)):
            l[8]+=l[j]
        s=l[7]+"_"+l[-1]+"_"+l[8]+fe
        os.rename(i,s)

for i in os.listdir():
    if "Dec" in i:
        a=fs+"//DEC"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Feb" in i:
        a=fs+"//FEB"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Mar" in i:
        a=fs+"//MAR"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Apr" in i:
        a=fs+"//APR"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Jan" in i:
        a=fs+"//JAN"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    else:
        continue

#FALLSEM2019-20_MAT2001_ETH_VL2019201000539_Reference_Material_I_08-Oct-2019_Samll_sample_t_-test_20
