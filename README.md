# PiRapGenerator
Make anyone rap the digits of pi

# Installation

This requires pydub to be installed (via pip) which requires ffmpeg to export audio<br>
(Must be added to PATH or use *pydub.AudioSegment.ffmpeg = "/path/to/ffmpeg"* or AudioSegment.converter idk anymore)

# Usage
Create audio clips of an exact length (in this case, 1/2 beat @ 140bpm = ~214ms) with the naming scheme shown (pi0, pi1, etc)<br>
Create a txt containing pi up to the number of digits you want and edit the path to it in the script<br>
Run the script using terminal/cmd as it runs roughly 2x faster than in IDLE Shell<br>
To cancel the render early, use CTRL+C to interrupt the program. This will then save the current file's progress.<br>
The chunk size can be changed, however a larger size may cause the program to run slower

# Info
No additional compression is done by default so each chunk will be the combined file size of each induvidual part<br>
Currently the final chunk will be named as if it failed.<br>
You may be limited by memory which is the cause of an 'Argument out of range' error.<br>
