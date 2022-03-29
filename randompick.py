import os
import random

path = r"./danaherjohn/"
#for file in os.listdir(path):
#    print (file)
files = os.listdir(path)
d = random.choice(files)

with open(path + d, 'r') as file:
    for line in file:
        print(line)
# print(random.choice(os.listdir(path)))




# print(len(os.listdir(path)))