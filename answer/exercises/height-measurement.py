''' άσκηση από το http://pythonies.mysch.gr/chapters/answer.pdf
'''

import math

print("Απόσταση από τον παρατηρητή μέχρι το αντικείμενο (σε μέτρα):")
distance = float(input())

print("Απόσταση από τον έδαφος μέχρι το επίπεδο των ματιών του παρατηρητή (σε μέτρα):")
eyelevel = float(input())

print("Γωνία από το οριζόντιο επίπεδο προς την κορυφή του αντικειμένου (σε μοίρες):")
angle = float(input())

height = eyelevel + distance * math.tan(math.pi * angle / 180)
print("Το ύψος του αντικειμένου είναι", height, "μέτρα.")

