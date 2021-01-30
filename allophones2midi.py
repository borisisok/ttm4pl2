import sys
import random
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL

allophones = {
'/AR/':  0,
'/AW/':  1,
'/AX/':  2,
'/AY/':  3,
'/BB1/': 4,
'/BB2/': 5,
'/CH/':  6,
'/DD1/': 7,
'/DD2/': 8,
'/DH1/': 9,
'/DH2/': 10,
'/EH/':  11,
'/EL/':  12,
'/ER1/': 13,
'/ER2/': 14,
'/EY/':  15,
'/FF/':  16,
'/GG1/': 17,
'/GG2/': 18,
'/GG3/': 19,
'/HH1/': 20,
'/HH2/': 21,
'/IH/':  22,
'/IY/':  23,
'/JH/':  24,
'/KK1/': 25,
'/KK2/': 26,
'/KK3/': 27,
'/LL/':  28,
'/MM/':  29,
'/NG/':  30,
'/NN1/': 31,
'PA1':   32,
'PA2':   33,
'PA3':   34,
'PA4':   35,
'PA5':   36,
'/AA/':  37,
'/AE/':  38,
'/AO/':  39,
'/AR/':  40,
'/AW/':  41,
'/AX/':  42,
'/AY/':  43,
'/BB1/': 44,
'/BB2/': 45,
'/CH/':  46,
'/DD1/': 47,
'/DD2/': 48,
'/DH1/': 49,
'/DH2/': 50,
'/EH/':  51,
'/EL/':  52,
'/ER1/': 53,
'/ER2/': 54,
'/EY/':  55,
'/FF/':  56,
'/GG1/': 57,
'/GG2/': 58,
'/GG3/': 59,
'/HH1/': 60,
'/HH2/': 61,
'/IH/':  62,
'/IY/':  63,
'/JH/':  64,
'/KK1/': 65,
'/KK2/': 66,
'/KK3/': 67,
'/LL/':  68,
'/MM/':  69,
'/NG/':  70,
'/NN1/': 71,
'/NN2/': 72,
'/OR/':  73,
'/OW/':  74,
'/OY/':  75,
'/PP/':  76,
'/RR1/': 77,
'/RR2/': 78,
'/SH/':  79,
'/SS/':  80,
'/TH/':  81,
'/TT1/': 82,
'/TT2/': 83,
'/UH/':  84,
'/UW1/': 85,
'/UW2/': 86,
'/VV/':  87,
'/WH/':  88,
'/WW/':  89,
'/XR/':  90,
'/YR/':  91,
'/YY1/': 92,
'/YY2/': 93,
'/ZH/':  94,
'/ZZ/':  95,
'/NN2/': 96,
'/OR/':  97,
'/OW/':  98,
'/OY/':  99,
'/PP/':  100,
'/RR1/': 101,
'/RR2/': 102,
'/SH/':  103,
'/SS/':  104,
'/TH/':  105,
'/TT1/': 106,
'/TT2/': 107,
'/UH/':  108,
'/UW1/': 109,
'/UW2/': 110,
'/VV/':  111,
'/WH/':  112,
'/WW/':  113,
'/XR/':  114,
'/YR/':  115,
'/YY1/': 116,
'/YY2/': 117,
'/ZH/':  118,
'/ZZ/':  119,
'PA1':   120,
'PA2':   121,
'PA3':   122,
'PA4':   123,
'PA5':   124,
'/AA/':  125,
'/AE/':  126,
'/AO/':  127
}

notes = []

if __name__ == '__main__':

    for line in sys.stdin:
        for allophone in line.split():
            note = 0
            if allophone in allophones:
                print(allophones[allophone])
                notes.append(allophones[allophone])
            elif "/"+allophone+"/" in allophones:
                print(allophones["/"+allophone+"/"])
                notes.append(allophones["/"+allophone+"/"])
        break

    midiname = sys.argv[1]
    outfile = MidiFile()

    track = MidiTrack()
    outfile.tracks.append(track)

    track.append(Message('program_change', program=1))

    delta = 300
    ticks_per_expr = 20
    for note in notes:
        track.append(Message('note_on', note=note, velocity=100, time=delta))
        #for j in range(delta // ticks_per_expr):
            #pitch = MAX_PITCHWHEEL * j * ticks_per_expr // delta
            #track.append(Message('pitchwheel', pitch=pitch, time=ticks_per_expr))
        track.append(Message('note_off', note=note, velocity=100, time=0))

    outfile.save(midiname + ".mid")
