''' Script to format the .txt file necessary for the transcription of the voice lines'''

with open('./danaheraudio/list.txt', 'w') as file:
    for i in range(1,101):
        file.write("wavs/" + str(i) + ".wav|\n")