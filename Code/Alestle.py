import datetime
import convertToText.py
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
        fillClass()

    #TODO: return the object with its comma delineated values, including needed default values
    #for the columns not included here.  A collection alestle.toString()'s should be a valid csv
    def toString(self):
        d = datetime.datetime.strptime(self.pubdate, "%B%d,%Y").strftime("%B %d, %Y")
        t = "The Alestle, "+d
        return t+","+self.url+","+self.url+",,,Southern Illinois University Edwardsville,,,,,,TRUE,,,,,,,FALSE,,,,,,,FALSE,,,,,,,FALSE,,,,,,,,Book,,"+d+","

    def fillClass(self):
        #Fils in the variables for the alestle class, given a string containing the entire newspaper.
        testString = convertToText.getPDFContents(self.url)
        testString = testString.replace(" ", "")
        dateMatch = re.search("(January|February|March|April|May|June|July|August|September|October|November|December)(\d|\d\d,)(\d\d\d\d)",testString)
        if(dateMatch)
            self.pubdate = dateMatch.group(0)
        issueMatch = re.search("Vol\.(\d|\d\d),No\.(\d\d|\d)",testString)
        if(issueMatch)
            self.abstract = issueMatch.group(0)
        
