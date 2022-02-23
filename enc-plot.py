import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['figure.figsize'] = 20, 10
matplotlib.rcParams.update({'font.size': 50})

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.15, bottom=0.2, right=0.9, top=0.9)

lines = open('enc.txt', 'r')

v = []
c = []
for line in lines:
    if 'voltage2' in line:
        line = line.strip().split(': ')
        v.append(float(line[1]))
    if 'current2' in line:
        line = line.strip().split(': ')
        c.append(float(line[1]))

p = []
for i, j in zip(v, c):
    p.append(i*j/1000.0)

ax.plot(p)
ax.set_ylabel('Power Consumption (mW)')
ax.set_xlabel('Timeline')

plt.savefig('figures/energy-encoding.png')

plt.show()
