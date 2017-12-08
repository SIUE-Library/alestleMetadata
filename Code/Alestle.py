import datetime

class Alestle():
    def __init__(self, u, a, p):
        
        self.url = u
        self.author = "Southern Illinois University Edwardsville"
        self.publisher = "Southern Illinois University Edwardsville"
        self.city = "Edwardsville"
        self.docType = "book"
        self.abstract = a
        self.pubdate = p

    #TODO: return the object with its comma delineated values, including needed default values
    #for the columns not included here.  A collection alestle.toString()'s should be a valid csv
    def toString(self):
        d = datetime.datetime.strptime(self.pubdate, "%B%d,%Y").strftime("%B %d, %Y")
        t = "The Alestle, "+d
        return t+","+self.url+","+self.url+",,,Southern Illinois University Edwardsville,,,,,,TRUE,,,,,,,FALSE,,,,,,,FALSE,,,,,,,FALSE,,,,,,,,Book,,"+d+","

#    def fillClass(inString):
        #Fils in the variables for the alestle class, given a string containing the entire newspaper.
        
print(Alestle("google or smth","","January3,1999").toString())
print(Alestle("google or smth","","February18,2004").toString())
print(Alestle("google or smth","","April30,2016").toString())
