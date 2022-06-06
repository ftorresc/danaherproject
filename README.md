# danaher-cli

## Overview
Danaher-cli is a terminal-based application that outputs [John Danaher's](https://www.instagram.com/danaherjohn/) instructional  Instagram post descriptions. It runs entirely offline to avoid the distractions of Instagram and social media.

## Usage
First, run the command `$ pip install -r requirements.txt` to install the required dependencies.
Once installed, `main.py` is the only file you will need to interact with. 

`python main.py -h` displays all possible arguments as well as help messages.

`python main.py -s searchterm` enters search mode and accepts a string to be searched among the files. Once a match is found, that file is displayed. 

`python main.py -r` enters random mode, choosing one file at random to display. Cannot be used with `-s`

`-v` is an optional argument to be run alongside either `-r` or `-s`. Initializes text to speech on the chosen file. As of this version, TTS cannot be stopped while it's running unless the terminal is closed.

`teststop.py` is a still non-functional attempt at stopping pyttsx3 once it is running. 

The folder `danaheraudio` contains all 100 audio excerpts initially extracted to train the voice model. The subfolder `halfsize` contains the 50 excerpts used for the actual training. Both folders contain a `list.txt` file containing the annotations.

The folder `txtfiles` contains the corpus from which the main script pulls files. Extracted using [Instaloader](https://instaloader.github.io/).

The folder `voicemodel` contains two synthesized sentences using the model trained. The model itself could not be included to Github's upload size limit.

## Dependencies
* [pyttsx3](https://github.com/nateshmbhat/pyttsx3)

## Author

Project developed by [Fábio Cabral](https://github.com/ftorresc/) for the "Préparation au Projet" and "Projet en Informatique" classes at Université de Lausanne during the school year of 2021-2022.
