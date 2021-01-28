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

phons = {'AA': "0x0E", 'AE': "0x0C", 'AH':"0x1B", 'AO':"0x12,0x11,0x11", 'AR': "0x0C,0x1C",
         'AW': '0x0F,0x10,0x11,0x16', 'AX':'0x0C,0x23', 'AY': '0x0F,0x0D,0x0B,0x03', 'B': '0x24', 'CH': '0x28,0x2D,0x32',
         'D': '0x25', 'DH': '0x36', 'EH': '0x0A', 'EL': '0x0A,0x20', 'EN': '0x0A,0x38',
         'ER': '0x1C', 'EY': '0x08,0x05,0x03', 'F': '0x34', 'G': '0x26', 'HH': '0x2C',
         'IH': '0x07', 'IR': '0x07,0x1D', 'IY': '0x05', 'JH': '0x25,0x31', 'K': '0x29,0x2C',
         'L': '0x20', 'M': '0x37', 'N': '0x38', 'NG': '0x39', 'OW': '0x11,0x16',
         'OY': '0x11,0x19,0x0F,0x07,0x06', 'P': '0x27', 'R': '0x1D', 'S': '0x30', 'SH': '0x32',
         'T': '0x28', 'TH': '0x35', 'UH': '0x15', 'UR': '0x16,0x1C', 'UW': '0x14,0x16,0x16',
         'V': '0x33', 'W': '0x23', 'Y': '0x04', 'Z': '0x2F', 'ZH': '0x2F', 'SIL': '0'}

apb_dict = nltk.corpus.cmudict.dict()


def say_it(chaine):
    print("say_it:" + chaine)
    #rondelle = chaine.split(",")
    #for i in rondelle:
    #    allo = int(i, 16)
    #    Command(0, allo)


def arpabet(word):
    try:
        arpabet = apb_dict[word]
        return arpabet

    except Exception as e:
        print
        "Error ! cannot process : " + str(e)
        arpabet = apb_dict["error"]
        return arpabet


def phoneme(apb):
    s = ''
    for p in apb:
        print(p),
        if p.endswith(('0', '1', '2')):
            s = phons[p[0:-1]]
            print(s)
            say_it(s)

        else:
            s = phons[p]
            print(s)
            say_it(s)
    return


def Strobe():
    #Arduino.digitalWrite(13, 0)
    #Arduino.digitalWrite(13, 1)
    print("Strobe")

def Command(register, value):
    print("Command")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #nltk.download()
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


# Related docs:
#
#   https://www.polaxis.be/2014/02/ssi-263-text-to-speech-in-python-via-nanpy-on-the-arduino/
#   https://gist.github.com/liuyork/4556798
#   https://github.com/jbeuckm/retroSpeak/blob/master/retroTTS.py
#
arpabet = nltk.corpus.cmudict.dict()
text="""robot human"""
words = nltk.word_tokenize(text)
for word in words:
    print("-------------")
    print(word)
    print(arpabet[word][1])
    print ( phoneme(arpabet[word][1]) )
    #Command(0,0)