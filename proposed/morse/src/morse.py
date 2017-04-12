"""
MORSE CODE SIGNALER (for the Raspberry Pi)

Copyright 2017 George Boukeas (boukeas@gmail.com)

Licensed under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

The software is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantablity, fitness
for a particular purpose and noninfringement. In no event shall the authors or
copyright holders be liable for any claim, damages or other liability, whether
in an action of contract, tort or otherwise, arising from, out of or in
connection with the software or the use or other dealings in the software.
"""

from gpiozero import LED
from time import sleep

# morse dict: maps english letters to morse code (sequences of dots and dashes)
morse = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    ' ': ' '
}


# timing: change unit (in secs) to make slower or faster
unit = 0.25
# from Wikipedia: https://en.wikipedia.org/wiki/Morse_code
# International Morse code is composed of five elements:
# short mark, dot or "dit": "dot duration" is one time unit long
short = unit
# longer mark, dash or "dah": three time units long
longer = 3 * unit
# inter-element gap between the dots and dashes within a character:
# one dot duration or one unit long
inter_element_gap = unit
# short gap (between letters): three time units long
short_gap = 3 * unit - inter_element_gap
# medium gap (between words): seven time units long
medium_gap = 7 * unit - short_gap

# the led, on GPIO 17 (or wherever you connect it)
led = LED(17)

def blink(duration):
    led.on()
    sleep(duration)
    led.off()

def dot():
    blink(short)

def dash():
    blink(longer)

def space():
    sleep(medium_gap)

# mapping between morse symbols and functions to be called
signal = {
    '.': dot,
    '_': dash,
    ' ': space}

# interaction with the user
message = input("What's the message? ")

for character in message.lower():
    for symbol in morse[character]:
        # output to screen
        print(symbol, end='', flush=True)
        # output to LED
        signal[symbol]()
        sleep(inter_element_gap)
    print(' / ', end='', flush=True)
    sleep(short_gap)
print()
