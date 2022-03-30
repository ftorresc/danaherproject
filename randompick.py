import os
import random
import pyttsx3

path = r"./danaherjohn/"
#for file in os.listdir(path):
#    print (file)
files = os.listdir(path)
d = random.choice(files)

with open(path + d, 'r') as file:
    for line in file:
       # debugging purposes, allows to exclude non-complying files 
       # print(d)
        print(line)
        engine = pyttsx3.init()
        engine.say(line)
        engine.runAndWait()
# print(random.choice(os.listdir(path)))




# print(len(os.listdir(path)))