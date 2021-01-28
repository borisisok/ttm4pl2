# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from __future__ import division
import random
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL
import nltk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    nltk.download()
    arpabet = nltk.corpus.cmudict.dict()
    for word in ('barbels', 'barbeque', 'barbequed', 'barbequeing', 'barbeques'):
        print(arpabet[word])


    notes = [64, 64+7, 64+12]

    outfile = MidiFile()

    track = MidiTrack()
    outfile.tracks.append(track)

    track.append(Message('program_change', program=12))

    delta = 300
    ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for i in range(4):
        note = random.choice(notes)
        track.append(Message('note_on', note=note, velocity=100, time=delta))
        for j in range(delta // ticks_per_expr):
            pitch = MAX_PITCHWHEEL * j * ticks_per_expr // delta
            track.append(Message('pitchwheel', pitch=pitch, time=ticks_per_expr))
        track.append(Message('note_off', note=note, velocity=100, time=0))

    outfile.save('test.mid')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
