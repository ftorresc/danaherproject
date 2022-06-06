''' Script to format the .txt file necessary for voice model training'''

with open('./danaheraudio/list.txt', 'w') as file:
    for i in range(1,101):
        file.write("wavs/" + str(i) + ".wav|\n")