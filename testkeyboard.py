import os
import random
import re

match = False
path = r"./test/"
#for file in os.listdir(path):
#    print (file)
files = os.listdir(path)
d = random.choice(files)


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
# print(random.choice(os.listdir(path)))


while not match:
    path = r"./txtfiles/"
    #for file in os.listdir(path):
    #    print (file)
    files = os.listdir(path)
    d = random.choice(files)
    with open(path + d, 'r') as file:
            for line in file:
                x = re.search("mount", line)
                if x:
                    print("FOUND")
                    print("\n\n" + line)
                    match = True
                else:
                    print("NOT FOUND")
