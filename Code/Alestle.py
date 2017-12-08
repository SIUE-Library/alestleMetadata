import datetime
import re
class Alestle():
    def __init__(self, fileURL):
        #Title := "The Alestle, <Month> <Day>, <Year>"
        self.title = ""
        self.url = fileURL
        self.author = "Southern Illinois University Edwardsville"
        self.publisher = "Southern Illinois University Edwardsville"
        self.city = "Edwardsville"
        self.docType = "book"
        self.abstract = "Vol.99,No.99"
        self.pubdate = "January1,1900"

        self.fillClass()

    #return the object with its comma delineated values, including needed default values
    #for the columns not included here.  A collection alestle.toString()'s should be a valid csv
    def toString(self):
        if self.pubdate == "January1,1900":
            print("Date is wrong at:")
        if self.abstract == "Vol.99,No.99":
            print("Edition is wrong at:")
        try:
            d = datetime.datetime.strptime(self.pubdate, "%B%d,%Y").strftime("%B %d, %Y")
            t = "The Alestle, "+d
            return t+"|"+self.url+"|"+self.url+"||"+self.abstract+"|Southern Illinois University Edwardsville||||||TRUE|||||||FALSE|||||||FALSE|||||||FALSE||||||||Book||"+d+"|\n"

        except:
            print("ERROR AT: "+self.url+"\n")
       
    def fillClass(self):
        #Fils in the variables for the alestle class, given a string containing the entire newspaper.
        testString = open(self.url, "r")
        testString = testString.read()
        testString = testString.replace(" ", "")
        testString = testString.replace("\n", "")
        testString = testString.replace("\r", "")
        
        dateMatch = re.search("(January|February|March|April|May|June|July|August|September|October|November|December)(\d|\d\d,)(\d\d\d\d)",testString)
        if(dateMatch):
            self.pubdate = dateMatch.group(0)
        issueMatch = re.search("Vol(,|\.)(\d\d|\d)(,|\.)No(,|\.)(\d\d|\d)",testString)
        if(issueMatch):
            self.abstract = issueMatch.group(0)
        
