# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:55:19 2021

@author: krystal.lopresti
"""

import numpy as np
import matplotlib.pyplot as plt

def two_scales(ax1, time, data1, data2, c1, c2):
    ax2 = ax1.twinx()
    ax1.plot(time, data1, color=c1)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp')
    ax2.plot(time, data2, color=c2)
    ax2.set_ylabel('sin')
    return ax1, ax2

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
s2 = np.sin(2 * np.pi * t)

'''
# Create axes
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4))
ax1, ax1a = two_scales(ax1, t, s1, s2, 'r', 'b')
ax2, ax2a = two_scales(ax2, t, s1, s2, 'gold', 'limegreen')
'''

# Create axes
fig, ax1 = plt.subplots()
ax1, ax1a = two_scales(ax1, t, s1, s2, 'r', 'b')
ax1, ax1a = two_scales(ax1, t, s1, s2, 'r', 'b')

# Change color of each axis
def color_y_axis(ax, color):
    """Color your axes."""
    for t in ax.get_yticklabels():
        t.set_color(color)

color_y_axis(ax1, 'r')
color_y_axis(ax1a, 'b')


plt.tight_layout()
plt.show()


#%%
# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(t, s1, color="red", marker="o")
# set x-axis label
ax.set_xlabel("time(s)",fontsize=14)
# set y-axis label
ax.set_ylabel("exp",color="red",fontsize=14)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(t, s2,color="blue",marker="o", markersize = '2')
ax2.set_ylabel("sin",color="blue",fontsize=14)
plt.show()
'''
# save the plot as a file
fig.savefig('two_different_y_axis_for_single_python_plot_with_twinx.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
'''