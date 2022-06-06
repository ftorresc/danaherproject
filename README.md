# danaher-cli

## Overview
Danaher-cli is a terminal-based application that outputs [John Danaher's](https://www.instagram.com/danaherjohn/) instructional  Instagram post descriptions. It runs entirely offline to avoid the distractions of Instagram and social media.

## Usage
First, run the command `$ pip install -r requirements.txt` to install the required dependencies.
Once installed, `main.py` is the only file you will need to interact with. 

`python main.py -h` displays all possible arguments as well as help messages.

`python main.py -s searchterm` enters search mode and accepts a string to be searched among the files. Once a match is found, that file is displayed. 

`python main.py -r` enters random mode, choosing one file at random to display. Cannot be used with `-s`

`-v` is an optional argument to be run alongside either `-r` or `-s`. Initializes text to speech on the chosen file.

## Dependencies
* [pyttsx3](https://github.com/nateshmbhat/pyttsx3)

## Author

Project developed by [Fábio Cabral](https://github.com/ftorresc/) for the "Préparation au Projet" and "Projet en Informatique" classes at Université de Lausanne during the school year of 2021-2022.
