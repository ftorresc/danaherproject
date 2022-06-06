import argparse
import os
import random
import pyttsx3
import keyboard
import re

path = r"./danaherjohn/"
parser = argparse.ArgumentParser(description='Script for the Danaher project')
parser.add_argument('-v', '--voice', action='store_true', help='enter search entry')
groupa = parser.add_mutually_exclusive_group()
groupa.add_argument('-r', '--random', action='store_true', help='random mode')
groupa.add_argument('-s', '--search', action='store_true', help='search mode')
args=parser.parse_args()


def main():
    pass



if __name__ == '__main__':
    main()