import Alestle
import os

list = []
for filename in os.listdir("../Alestle/text"):
    tmp = (Alestle.Alestle("../Alestle/text/"+filename).toString())
    print(tmp)
    list.append(tmp)

print(len(list))

wrong = 0
total = 0

for l in list:
    if "Error" in l:
        wrong += 1
    total += 1

print("We succeeded with "+str(total-wrong)+" out of "+str(total))
