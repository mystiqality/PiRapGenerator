from pydub import AudioSegment
import time as t
import os

#pi0 = AudioSegment.from_wav("pi0.wav")

#sortedDir = sorted(dirList, key = lambda x: int(x.split("Rap")[1]))

ready = False
count = 0


wavList = []


for file in os.listdir():
    name, fType = os.path.splitext(file)
    if fType == ".wav":
        wavList.append(name)


sortedList = sorted(wavList, key = lambda x: int(x.split("Rap")[1]))

print(sortedList)


for wavName in sortedList:
    if(count % 20 == 0 and count != 0):
        song.export(str(count) + ".wav", format="wav")
        ready = False
        
    
    if(ready == False):
        fileName = wavName + ".wav"
        song = AudioSegment.from_wav(fileName)
        ready = True
        count += 1
        print(wavName+ " - " + str(count))
        
    else:
        fileName = wavName + ".wav"
        song += AudioSegment.from_wav(fileName)
        count += 1
        print(wavName+ " - " + str(count))


song.export(str(count) + ".wav", format="wav")
t.sleep(5)

