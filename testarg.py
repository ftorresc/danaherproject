import argparse
import os
import random
import pyttsx3

path = r"./danaherjohn/"
parser = argparse.ArgumentParser(description='Script for the danaher project thngy')

parser.add_argument('-v', '--voice', action='store_true', help='enter search entry')
group = parser.add_mutually_exclusive_group()
parser.add_argument('-r', '--random', action='store_true', help='random mode')
parser.add_argument('-s', '--search', action='store_true', help='search mode')
args = parser.parse_args()

def rnd():
    files = os.listdir(path)
    d = random.choice(files)
    if args.voice:
        with open(path + d, 'r') as file:
            for line in file:
                engine = pyttsx3.init()
                engine.say(line)
                engine.runAndWait()
    else:
        with open(path + d, 'r') as file:
            for line in file:
                # debugging purposes, allows to exclude non-complying files 
                print(d)
                print(line)

def search():
    print("SERACH MODE")


if __name__ == '__main__':
    if args.random:
        rnd()
    elif args.search:
        search()
    else:
        pass