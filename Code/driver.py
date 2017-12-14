import Alestle
import os

csv = ""
for filename in os.listdir("../Alestle/text"):
    tmp = (Alestle.Alestle("../Alestle/text/"+filename).toString())
    print(tmp)
    if not "Error" in tmp:
        csv += tmp


wrong = 0
total = 0

print("We succeeded with "+str(total-wrong)+" out of "+str(total))
file = open("out.csv","w+")
file.write(csv)