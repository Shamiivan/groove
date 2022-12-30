import midiutil

# create a midi file with a single track
midi = midiutil.MIDIFile(2)

# set track name
track = 0
time = 0
midi.addTrackName(track, time, "C Major Scale")
midi.addTempo(track, time, 120)

# add some notes
channel = 0
pitch = 60
time = 0
duration = 2
volume = 100

for i in range(8):
    midi.addNote(track, channel, pitch, time, duration, volume)
    pitch += 1
    time += 2

track = 1
time = 0
midi.addTrackName(track, time, "E minor Scale")

# add some notes
pitch = 63
time =0
duration = 2
volume = 100

for i in range(16):
    midi.addNote(track, channel, pitch, time, duration, volume)
    pitch += 1
    time +=1

# write to the midi file 
with open("scale.midi", "wb") as f:
    midi.writeFile(f)