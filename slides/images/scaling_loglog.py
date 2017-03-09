#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Use Latin Modern type 1 fonts
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern']})

# Data from Mira runs (nodes, neutrons/sec)
data = [(128, 1.97094e6),
        (256, 3.95749e6),
        (512, 7.88299e6),
        (1024, 1.58193e7),
        (2048, 3.13780e7),
        (4096, 6.25105e7),
        (8192, 1.25958e8),
        (16384, 2.51868e8),
        (32768, 4.82503e8),
        (49152, 7.40938e8)]

cores, rate = zip(*data)
cores = 16*np.asarray(cores)
rate = np.asarray(rate)
ideal = cores*rate[0]/cores[0]


plt.loglog(cores, rate, 'bo', label='Measured')
plt.loglog(cores, ideal, 'k--', label='Ideal')
#plt.gca().set_xscale('log',basex=2)
plt.xlabel('Number of Cores', fontsize=16)
plt.ylabel('Particles per second', fontsize=16)
plt.grid(True, which='both')
plt.legend(loc='upper left')
plt.title('Parallel scaling on ALCF Mira')

# Save figure
plt.savefig('scaling_loglog.pdf', bbox_inches='tight')
