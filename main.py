#!/usr/bin/env python

import matplotlib.pyplot as plt

# Create a text file with a '+' sign in the filename
with open('Data/text_file_with_+_symbol_in_filename.txt', 'w') as f:
    f.write("This file will not be displayed or downloadable in the web interface.\n")

# Create a .png file with a '+' sign in the filename
fig = plt.figure()
ax = fig.gca()
ax.plot([0, 1, 2, 3, 4], [1, 2, 1, 1.3, 1])
fig.savefig('Data/png_file_with_+_symbol_in_filename.png')
