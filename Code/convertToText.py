import subprocess
import sys
import os


#takes a name of an alestle document.  goes to the alestle folder and finds that document.
#takes that document and takes the plaintext, converting it to a .txt.  stores that in
#the text/ directory of the Alestle folder.  will fail if "../Alestle/filename" does not exist.
#will also fail if "../Alestle/text/" directory does not exist.
#IF it does fail, the program will exit and the general Error (usually IO) will be printed
def getPDFContents(filename):
    try:
        subprocess.check_output(["pdftotext", "../Alestle/"+filename, "../Alestle/text/"+filename[:-4]+".txt"])
    except:
        pass


#goes into "../Alestle" folder and returns each file in that folder such that it end in ".pdf"
#if no such files are found this fact will be printed before the program is exited.
#NOTE THAT the "../Alestle" is not included in the filenames in the list!  Only the name of
#thr pdf itself is!
def getListOfPapers():

    #find Alestle directory, which is in the parent directory
    dir = os.path.dirname(__file__)+"../Alestle"
    list = []

    #os.listdir return a list of every file in dir.  we iterate through this.
    for filename in os.listdir(dir):
        #pdf's only are appended to list
        if(filename.endswith(".pdf")):
            list.append(filename)
    #if no pdf was found print and exit
    if len(list) == 0:
        print("No files found, quiting")
        sys.exit()
    #otherwise, return the populated list
    return list



###PROGRAM STARTS EXECUTION###


#get the list of papers, iterate through it.  at each paper, process into text.
for l in getListOfPapers():
    getPDFContents(l)


###PROGRAM STOPS  EXECUTION###