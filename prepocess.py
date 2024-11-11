from music21 import *
from collections import defaultdict, OrderedDict
# from itertools import groupby, izip_longest
# from grammar import *
from typing import List


filename = "data/xml_mxl/canon_in_d.mxl"
# Get musical data from a MIDI file
def get_musical_data(filename: str):
    #pasrce the midi data for sarate melody and accompaniment parts
    score = converter.parse(filename)

    #get melody part, compress into single voice
    melody_voice = get_element_by_class(score, stream.Voice)
    return melody_voice


def get_element_by_class(stream:object, obj_to_extract:object) -> List[object]:
    elements =[]
    for elem in stream.recurse():
        if isinstance(elem, obj_to_extract):
            elements.append(elem)
    return elements


m = get_musical_data(filename)
m.show()
