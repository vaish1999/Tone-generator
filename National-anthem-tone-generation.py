#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:41:20 2020

@author: vaishakh
"""

from tones import SINE_WAVE, SAWTOOTH_WAVE
from tones.mixer import Mixer

# Create mixer, set sample rate and amplitude
mixer = Mixer(44100, 0.5)

# Create two monophonic tracks that will play simultaneously, and set
# initial values for note attack, decay and vibrato frequency 
mixer.create_track(0, SAWTOOTH_WAVE, vibrato_frequency=7.0, vibrato_variance=30.0, attack=0.01, decay=0.1)
mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)

# Add a 1-second tone on track 0, slide pitch from c# to f#)
#mixer.add_note(0, note='a#', octave=5, duration=1.0, endnote='f#')

# You can add your own musical note over here!
text_file = open("musical-notes.txt", "r")
musical_notes = text_file.read().split(' ')[:-1]

# You can alter the playback speed of tone
speed=1

for i in range(len(musical_notes)):
    if i==8 or i==13 or i==14 or i==17 or i==22 or i==23 or i==24 or i==26 or i==28 or i==35 or i==36 or i==39 or i==42 or i==44 or i==47 or i==50 or i==54 or i==55 or i==58 or i==64 or i==69 or i==70 or i==71 or i==73 or i==78 or i==83 or i==85 or i==97 or i==100 or i==105 or i==106 or i==109 or i==114:
        k=0.75  #Aaroha tones
    elif i==43 or i==84 or i==92:
        k=1     #maha aaroha tones
    elif i==117 or i==120 or i==123 or i==132:
        k=1.1   #Jaya hey tones
    else:
        k=0.375 
    mixer.add_note(1, note=musical_notes[i], octave=5, duration=k*speed)

# Our National Anthem is sung with an increasing tone always.
# So, no avaroha tones!
# Mix all tracks into a single list of samples and write to .wav file

mixer.write_wav('National-Anthem.wav')

print("Done")

# Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
# return the sample list
samples = mixer.mix()

