import argparse
import os
import random
import pyttsx3
import keyboard
import re

path = r"./danaherjohn/"
parser = argparse.ArgumentParser(description='Script for the Danaher project')

group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--random', action='store_true', help='Randomly picks and displays one file.')
group.add_argument('-s', '--search', help='Searches for the given string among the files and displays it.')
parser.add_argument('-v', '--voice', action='store_true', help='Enables text to speech narration of the chosen file.')
args = parser.parse_args()

def rnd():
    files = os.listdir(path)
    d = random.choice(files)
    if args.voice:
        with open(path + d, 'r') as file:
            for line in file:
                # debugging purposes, allows to exclude non-complying files 
                # print(d)
                print("\n\n" + line)
                engine = pyttsx3.init()
                engine.say(line)
                engine.runAndWait()
    else:
        with open(path + d, 'r') as file:
            for line in file:
                # debugging purposes, allows to exclude non-complying files 
                # print(d)
                print("\n\n" + line)

def search():
    # print(args.search)
    match = False
    while not match:
        path = r"./danaherjohn/"
        #for file in os.listdir(path):
        #    print (file)
        files = os.listdir(path)
        d = random.choice(files)
        with open(path + d, 'r') as file:
                for line in file:
                    x = re.search(args.search, line)
                    if x:
                        if args.voice:
                            # print("FOUND")
                            print("\n\n" + line)
                            engine = pyttsx3.init()
                            engine.say(line)
                            engine.runAndWait()
                            match = True
                        else:
                            # print("FOUND")
                            print("\n\n" + line)
                            match = True
                    else:
                        # print("NOT FOUND")
                        pass


if __name__ == '__main__':
    if args.random:
        rnd()
    elif args.search:
        search()
    else:
        pass