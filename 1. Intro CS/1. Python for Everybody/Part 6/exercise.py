# -*- coding: utf-8 -*-

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
fvalue = float(piece)
print(fvalue) 