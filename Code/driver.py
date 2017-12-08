import Alestle
import os

testObject =  Alestle.Alestle("../Alestle/text/Ales_2002_06_26.txt")
print(testObject.toString())

for filename in os.listdir("../Alestle/text"):
    print(Alestle.Alestle("../Alestle/text/"+filename).toString())