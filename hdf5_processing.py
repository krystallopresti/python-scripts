# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:10:37 2021

@author: krystal.lopresti
Recreating plots of h5py files and overlaying them

Did E1L1 for now for each of the days. Need to do the rest
"""

# import important function folders
import numpy as np
import h5py
import matplotlib.pyplot as plt
import os

# laser number definition for each of the scenarios this is the only part that needs to be changed every time the code is run
E_L = "E1_L1"
E = "E1" # channge this value when the E is being changed

os.chdir("C:/Users/krystal.lopresti/Documents\Houlihan/05_28_2021 Brun In GenA SN07/B39767/W4/R2C5D2/run1_05282021_burn_in_1")
# open single h5 file 
f = h5py.File("B39775_W4_R2C5D2_B1-D02_LIV.h5", "r")
# choose specific 
n1 = f.get(E_L) # future step is to change the variables to string variables where only the numbers for E and L have to be changed
n2 = n1.get('Results')
n3 = n2.get('result_data_set')
# works up tp here to get the dataset with 250 values
n4 = np.array(n3)
b = n4.tolist() # n4 to list to work with the values more readily

# for loop to create an array for the current and the power
i = 0
current = []
power = []
while i<250:
    c = b[i]
    current1 = c[0]
    current.append(current1)
    
    power1 = c[2]
    power.append(power1)
    i = i+1

# plot data
plt.plot(current, power)
s = plt.plot(current, power)
plt.title('Epi LIV ' + E_L)
plt.xlabel('Current (mA)')
plt.ylabel('Power (mW)')
plt.show()


# trial 2
os.chdir("C:/Users/krystal.lopresti/Documents/Houlihan/06_01_2021 Burn in GenA SN07 continued/B39767/W4/R2C5D2/run1_06012021_burn_in_2")
f2 = h5py.File("B39776_W4_R2C5D2_B1-D02_LIV.h5", "r")
# choose specific 
run2_n1 = f2.get('E1_L1') # future step is to change the variables to string variables where only the numbers for E and L have to be changed
run2_n2 = run2_n1.get('Results')
run2_n3 = run2_n2.get('result_data_set')
# works up tp here to get the dataset with 250 values
run2_n4 = np.array(run2_n3)
run2_b = run2_n4.tolist() # n4 to list to work with the values more readily

# for loop to create an array for the current and the power
ii = 0
run2_current = []
run2_power = []
while ii<250:
    run2_c = run2_b[ii]
    run2_current1 = run2_c[0]
    run2_current.append(run2_current1)
    
    run2_power1 = run2_c[2]
    run2_power.append(run2_power1)
    ii = ii+1
    
    # plot data
plt.plot(run2_current, run2_power)
o1 = plt.plot(run2_current, run2_power)
plt.title('Run2 Epi LIV ' + E_L)
plt.xlabel('Current (mA)')
plt.ylabel('Power (mW)')
plt.show()



# trial 3
os.chdir("C:/Users/krystal.lopresti/Documents/Houlihan/06_11_2021 Burn in GenA SN07 continued/B39767/W4/R2C5D2/run1_1101_06112021_burn_in_3")
f3 = h5py.File("B39767_W4_R2C7D2_B1-D02_LIV.h5", "r")
# choose specific 
run3_n1 = f3.get('E1_L1') # future step is to change the variables to string variables where only the numbers for E and L have to be changed
run3_n2 = run3_n1.get('Results')
run3_n3 = run3_n2.get('result_data_set')
# works up tp here to get the dataset with 250 values
run3_n4 = np.array(run3_n3)
run3_b = run3_n4.tolist() # n4 to list to work with the values more readily

# for loop to create an array for the current and the power
iii = 0
run3_current = []
run3_power = []
while iii<250:
    run3_c = run3_b[iii]
    run3_current1 = run3_c[0]
    run3_current.append(run3_current1)
    
    run3_power1 = run3_c[2]
    run3_power.append(run3_power1)
    iii = iii+1
    
    # plot data
plt.plot(run3_current, run3_power)
o1 = plt.plot(run3_current, run3_power)
plt.title('Run3 Epi LIV ' + E_L)
plt.xlabel('Current (mA)')
plt.ylabel('Power (mW)')
plt.show()



# trial 4
os.chdir("C:/Users/krystal.lopresti/Documents/Houlihan/06_15_2021 Burn in GenA SN07 continued/run4_06152021/B39767/W4/R2C5D2")
f4 = h5py.File("B39767_W4_R2C7D2_B1-D02_LIV.h5", "r")
# choose specific 
run4_n1 = f4.get('E1_L1') # future step is to change the variables to string variables where only the numbers for E and L have to be changed
run4_n2 = run4_n1.get('Results')
run4_n3 = run4_n2.get('result_data_set')
# works up tp here to get the dataset with 250 values
run4_n4 = np.array(run4_n3)
run4_b = run4_n4.tolist() # n4 to list to work with the values more readily

# for loop to create an array for the current and the power
iv = 0
run4_current = []
run4_power = []
while iv<250:
    run4_c = run4_b[iv]
    run4_current1 = run4_c[0]
    run4_current.append(run4_current1)
    
    run4_power1 = run4_c[2]
    run4_power.append(run4_power1)
    iv = iv+1
    
    # plot data
plt.plot(run4_current, run4_power)
o1 = plt.plot(run4_current, run4_power)
plt.title('Run4 Epi LIV ' + E_L)
plt.xlabel('Current (mA)')
plt.ylabel('Power (mW)')
plt.show()


## Combining trials 1 and 2
# line 1 points are current and power
# plotting the line 1 points 
fig1 = plt.plot(current, power, label = "5/28")
# line 2 points are run2_current and run2_power
# plotting the line 2 points 
fig1 = plt.plot(run2_current, run2_power, label = "6/1")
plt.xlabel('Current (mA)')
# Set the y axis label of the current axis.
plt.ylabel('Power (mW)')
# Set a title of the current axes.
plt.title('Run1 (5/28) and Run2 (6/1) ' + E_L)
# show a legend on the plot
plt.legend()
# Save Figure of trials 1 and 2
my_path = "C:/Users/krystal.lopresti/Documents/Houlihan/" + E + "/"
my_file = E_L + "Run1 5_28 and Run2 6_1.png"
os.path.join(my_path,my_file)
plt.savefig(my_path+ my_file) 
# Display a figure.
plt.show()


## Combining trials 3 and 4
# line 1 points are current and power
# plotting the line 1 points 
fig2 = plt.plot(run3_current, run3_power, label = "6/11")
# line 2 points are run2_current and run2_power
# plotting the line 2 points 
fig2 = plt.plot(run4_current, run4_power, label = "6/15")
plt.xlabel('Current (mA)')
# Set the y axis label of the current axis.
plt.ylabel('Power (mW)')
# Set a title of the current axes.
plt.title('Run3 (6/11) and Run4 (6/15) ' + E_L)
# show a legend on the plot
plt.legend()
# Save Figure of trials 3 and 4
my_file = E_L + "Run1 6_11 and Run2 6_15.png"
os.path.join(my_path,my_file) # same my_path variable as above
plt.savefig(my_path+ my_file) 
# display figure
plt.show()


