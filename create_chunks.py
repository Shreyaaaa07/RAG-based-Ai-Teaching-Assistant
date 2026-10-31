from unittest import result

import whisper
import json
import os

# model = whisper.load_model("large-v2")

audios = os.listdir("audios")

for audio in audios:
    print(audio)
    number = audio.split("_")[0]
    title = audio.split("_")[1]
    print(number, title)
    # result = model.transcribe(audio = "audios/samplee.mp3",
    #                           language = "hi",
    #                           task="translate",
    #                           word_timetamps=False )
    chunks = []
    for segment in result["segments"]:
        chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})      