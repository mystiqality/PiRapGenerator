from pydub import AudioSegment
import time as t

piRendered = ""
total = 0

## USER MODIFIABLE VALUES ##

chunkSize = 1000
piTxtName = "pi250k.txt"

pi0 = AudioSegment.from_wav("./digits/pi0.wav")
pi1 = AudioSegment.from_wav("./digits/pi1.wav")
pi2 = AudioSegment.from_wav("./digits/pi2.wav")
pi3 = AudioSegment.from_wav("./digits/pi3.wav")
pi4 = AudioSegment.from_wav("./digits/pi4.wav")
pi5 = AudioSegment.from_wav("./digits/pi5.wav")
pi6 = AudioSegment.from_wav("./digits/pi6.wav")
pi7 = AudioSegment.from_wav("./digits/pi7.wav")
pi8 = AudioSegment.from_wav("./digits/pi8.wav")
pi9 = AudioSegment.from_wav("./digits/pi9.wav")

## END ##




pi = open(piTxtName, "r").read()
digits = {"0":pi0, "1":pi1, "2":pi2, "3":pi3, "4":pi4, "5":pi5, "6":pi6, "7":pi7, "8":pi8, "9":pi9}

try:
    for char in pi:
        # if first character, create variables
        if(len(piRendered) == 0):
            song = digits[char]
            piRendered = char
            total += 1
            
        # if chunk size met, export audio then create new chunk
        elif(len(piRendered) % chunkSize == 0):
            name =  "piRap" + str(total) + ".wav"
                        
            song.export(name, format="wav")
                        
            print("Saved file: " + name)
                        
            song = digits[char]
            piRendered = char
            total += 1
        
        else:
            piRendered += char
            song += digits[char]

            total += 1
            print(str(len(piRendered)) + " - " + str(total))
            


except:
    print("\nStopping")
    pass




song.export(".\output\piRapFail.wav", format="wav")
t.sleep(5)
