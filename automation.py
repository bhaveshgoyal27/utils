import os
from tkinter import filedialog
from tkinter import *
import shutil

root = Tk()
root.withdraw()
fs = filedialog.askdirectory()
print(fs)
os.chdir(fs)
#os.mkdir("JUL")
os.mkdir("AUG")
os.mkdir("SEPT")
os.mkdir("OCT")
#os.mkdir("NOV")
#os.mkdir("DEC")
months = ["Jul","Aug","Sep","Oct","Nov","Dec"]
for i in os.listdir():
    fn, fe = os.path.splitext(i)
    l=fn.split("_")
    if len(l)>=9:
        if l[7][3:5].isdigit():
            a = int(l[7][3:5])
            b = months[a-7]
            c = l[7][:3]+b+l[7][5:]
            l[7] = c
        for j in range(9,len(l)):
            l[8]+=l[j]
        s=l[7]+"_"+l[-1]+"_"+l[8]+fe
        os.rename(i,s)

for i in os.listdir():
    if "Aug" in i:
        a=fs+"//AUG"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Sep" in i:
        a=fs+"//SEPT"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Oct" in i:
        a=fs+"//OCT"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Nov" in i:
        a=fs+"//NOV"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    elif "Dec" in i:
        a=fs+"//DEC"+"//"+i
        b=fs+"//"+i
        shutil.move(b,a)
    else:
        continue

#FALLSEM2019-20_MAT2001_ETH_VL2019201000539_Reference_Material_I_08-Oct-2019_Samll_sample_t_-test_20
