import subprocess
import sys
import os

def getPDFContents(filename):
    try:
        subprocess.check_output(["pdftotext", "../Alestle/"+filename, "../Alestle/text/"+filename[:-4]+".txt"])
    except:
        pass

def getListOfPapers():
    dir = os.path.dirname(__file__)+"../Alestle"
    list = []
    for filename in os.listdir(dir):
        if(filename.endswith(".pdf")):
            list.append(filename)
    if len(list) == 0:
        print("No files found, quiting")
        sys.exit()
    return list

li = getListOfPapers()

print("List obtained: "+li[1])

for l in li:
    getPDFContents(l)