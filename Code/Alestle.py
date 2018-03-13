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
        self.abstract = ""
        self.pubdate = ""

        self.fillClass()

    #return the object with its comma delineated values, including needed default values
    #for the columns not included here.  A collection alestle.toString()'s should be a valid csv
    def toString(self):
        t=""
        d=""
        if self.pubdate == "":
            t += "Error: Date is wrong at:\n"
        if self.abstract == "":
            t += "Error: Edition is wrong at:\n"
        try:
            d = datetime.datetime.strptime(self.pubdate, "%B%d,%Y").strftime("%Y-%m-%d")
            t += "The Alestle, "+d
            
        except:
            t += "Error AT: "+self.url+"\n"

        url = "146.163.15x.xxx/alestle/"+self.url
        return self.title+","+self.url+",,,Southern Illinois University Edwardsville,,,,,,FALSE,,,,,,,FALSE,,,,,,,FALSE,,,,,,,FALSE,,,,,,"+self.date+","
       
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
            self.abstract = self.abstract.replace(",", " ")
            print("UPDATED")