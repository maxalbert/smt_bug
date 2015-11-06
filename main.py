#!/usr/bin/env python

import os
import sys
from sumatra.parameters import build_parameters

print("Hello world.")

# It is important not to hard-code the name of the parameter file because
# Sumatra creates a parameter file 'on the fly' and passes its name to the
# script, thus we read its name from the command line arguments.
paramsfile = sys.argv[1]
parameters = build_parameters(paramsfile)

print("Parameters: {}".format(parameters))

# Change into the datastore directory to run the simulation there
wrkdir = os.path.join('Data', parameters['sumatra_label'])
os.chdir(wrkdir)

with open('sample_output.txt', 'w') as f:
    f.write('Hello world!\n')
