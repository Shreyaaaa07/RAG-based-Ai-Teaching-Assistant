from pydoc import text
from unittest import result
from xml.parsers.expat import model

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
    result = model.transcribe(audio = f"audios/sample.mp3",
                             language = "hi",
                               task="translate",
                              word_timetamps=False )
    chunks = []
    for segment in result["segments"]:
        chunks.append({ " number": number, "title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

    chunks_with_metadata = {chunks: chunks, text: result["text"]}
              

    with open(f"chunks_{number}.json", "w") as f:
        json.dump(chunks_with_metadata, f)