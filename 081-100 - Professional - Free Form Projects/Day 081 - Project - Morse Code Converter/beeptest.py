import winsound
from random import choice

frequency = 700  # Set Frequency To 2500 Hertz
duration_short = 100  # Set Duration To 100 ms == .1 second
duration_long = 300  # Set Duration To 300 ms == .3 second
winsound.Beep(frequency, duration_short)

sounds = [duration_long, duration_short]

for i in range(30):
    which = choice(sounds)
    winsound.Beep(frequency, which)
