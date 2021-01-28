# -*- coding: utf-8 -*-

"""
    a2p.py
    ~~~~~~~~~~~~~

    Arpabet code to unicode phoneme.

    :author: liuyork
    :copyright: (c) 2013.
"""
import nltk

phons = {'AA': u'ɑ', 'AE': u'æ', 'AH': u'ʌ', 'AO': u'ɔ', 'AR': u'ɛr',
         'AW': u'aʊ', 'AX': u'ə', 'AY': u'aɪ', 'B': u'b', 'CH': u'tʃ',
         'D': u'd', 'DH': u'ð', 'EH': u'ɛ', 'EL': u'ɔl', 'EN': u'n',
         'ER': u'ər', 'EY': u'eɪ', 'F': u'f', 'G': u'ɡ', 'HH': u'h',
         'IH': u'ɪ', 'IR': u'ɪr', 'IY': u'i', 'JH': u'dʒ', 'K': u'k',
         'L': u'l', 'M': u'm', 'N': u'n', 'NG': u'ŋ', 'OW': u'oʊ',
         'OY': u'ɔɪ', 'P': u'p', 'R': u'r', 'S': u's', 'SH': u'ʃ',
         'T': u't', 'TH': u'θ', 'UH': u'ʊ', 'UR': u'ʊr', 'UW': u'u',
         'V': u'v', 'W': u'w', 'Y': u'j', 'Z': u'z', 'ZH': u'ʒ', 'SIL': ''}

apb_dict = nltk.corpus.cmudict.dict()


def arpabet(word):
    try:
        arpabet = apb_dict[word]
        return arpabet
    except( Exception, e):
        print(e)
    return None


def phoneme(apb):
    s = ''
    for p in apb:
        if p.endswith(('0', '1', '2')):
            s += phons[p[0:-1]] + '\''
        else:
            s += phons[p]
    return s


if __name__ == "__main__":
    for word in ('the', 'dark', 'side', 'of', 'moon'):
        print( word + '  /' + phoneme(arpabet(word)[0]) + '/' )
