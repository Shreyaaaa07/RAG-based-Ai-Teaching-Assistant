from email.mime import audio

from torch import chunk
import whisper
import json

# Load the Whisper model
model = whisper.load_model("large-v2")
result = model.transsccribe(audio = "audios/1.mp3",
                            language = "hi",
                            task="translate",
                            word_timetamps=False )
print(result)                            
# print(result["text"])
# with open("output.json", "w")as f:
#     json.dump(f, result)    
print(result["segments"])
chunks = []
for segements in result["segments"]:
    chunks.append({"start": segements["start"], "end": segements["end"], "text": segements["text"]})             

print(chunks)

with open("chunks.json", "w") as f:
    json.dump(chunks, f)


    