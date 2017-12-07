import subprocess

def getPDFContents(filename):

    subprocess.check_output(["pdftotext", filename, filename[:-4]+".txt"])

getPDFContents("../Alestle/Ales_1996_01_23.pdf")