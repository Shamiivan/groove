from music21 import *
from collections import defaultdict, OrderedDict
# from itertools import groupby, izip_longest
# from grammar import *
from typing import List


filename = "data/xml_mxl/canon_in_d.mxl"
# Get musical data from a MIDI file
def get_musical_data(filename: str):
    #pasrce the midi data for sarate melody and accompaniment parts
    midi_data = converter.parser(filename)
    
    #get melody part, compress into single voice    
    pass

def extract(stream:object, obj_to_extract:object) -> List[object]:
    notes =[]
    for elem in stream.recurse():
        if isinstance(elem, obj_to_extract):
            notes.append(elem)
    return notes 



midi_data = converter.parse(filename)
notes = extract(midi_data, stream.Voice)
for note in notes:
    print(note.pitch)