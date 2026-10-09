#converts the videos to mp3
import os
import subprocess
files = os.listdir("videos")
print(files)
for file in files:
    tutorial_number = file.split("[")[0].split(" #")[1]
print(tutorial_number)