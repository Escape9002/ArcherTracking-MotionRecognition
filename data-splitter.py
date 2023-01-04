import pandas as pd
import numpy as np
import csv

import time

import matplotlib.pyplot as plt

# validates wether the position of the splitting points actually correspond to the splitting points in the original dataset (csv_file)
def val_split_pos(split = [], np_array = np.array, collumn = 0, benchmark = False):
    if benchmark: start = time.perf_counter()
    i=0
    for row,value in split:
        if not (value == np_array[row][collumn]):
            return False

    if benchmark: print("valsplitpos time: {}".format(time.perf_counter()-start))
    return True

# searches for multiple peaks at the same points to avoid too small splits
def del_val_multiple(split, benchmark = False):
    if benchmark: start = time.perf_counter()
    single_vals = []
    for i in range(len(split)-1):
        if not (split[i][1] == split[(i+1)][1]):
            single_vals.append(split[i][0])
    if benchmark: print("delvalmult t: {}".format(time.perf_counter()-start))
    return single_vals

# splits the dataset at a givin value, no smoothening or anything, you have to applay del_va_multiple to have correct results
def normal_splitting(collumn = 0, min_aX = -15.00, np_array = np.array, splits = [], benchmark = False):
    if benchmark: start = time.perf_counter()
    row = 0
    while(len(np_array) > row):
        if(np_array[row][collumn] < min_aX):
            splits.append([row,np_array[row][collumn]])
        row += 1

    if benchmark: print("normalsplittimg t: {}".format(time.perf_counter()-start))
    return del_val_multiple(splits)

def split_data_iterative(np_array = np.array, splits = [], benchmark = False):
    if benchmark: start = time.perf_counter()

    old = 0
    splitted = []

    for i in range(len(splits)):
        tmp = np_array[old:splits[i]].copy()
        splitted.append(tmp)
        old = splits[i]
    
    if benchmark: print("splitdataez: {}".format(time.perf_counter()-start))
    return splitted
    
def save_dataset(filename = "",splitted_dataset = [], header = ["aX","aY","aZ"], benchmark = False):
    if benchmark: start = time.perf_counter()
    i = 0
    for data in splitted_dataset:
        with open("splitted_data/{}_{}".format(filename, i), 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        i += 1
    if benchmark: print("save_dataset t: {}".format(time.perf_counter()-start))



def show_dataset(splitted_dataset = [], del_f=0,del_l=1,benchmark = False):
    if benchmark: start = time.perf_counter()
    if del_l > len(splitted_dataset):
        print("Choose smaller del_l")
        return

    print("Found Datasets: {}".format(len(splitted_dataset)))

    fig, axs = plt.subplots((del_l-del_f), sharex=True, sharey=True)
    
    axis = 0
    while (del_f < del_l):
        axs[axis].plot(splitted_dataset[del_f])
        axs[axis].set_title("splitted_dataset {}".format(del_f))
        print(del_f)
        del_f += 1
        axis += 1

    plt.show()
    if benchmark: print("show_dataset t: {}".format(time.perf_counter()-start))

##################################################
########## THE REAL PROGRAMM #####################
##################################################

path =  'data/2451_Shooting.csv'
csv_file = pd.read_csv(path)
np_array = csv_file.to_numpy()

min_aX = -15.00
collumn = 0
normalized_splits = []

normalized_splits = normal_splitting(collumn, min_aX, np_array, benchmark=True)
splitted_dataset = split_data_iterative(np_array, normalized_splits, benchmark=True)

show_dataset(splitted_dataset,0,len(splitted_dataset), benchmark=True)
# save_dataset("4455", splitted_dataset, benchmark=True)

####################################################
print("########### ANOTHER FILE ####################")
####################################################

path =  'data/4455_Shooting.csv'
csv_file = pd.read_csv(path)
np_array = csv_file.to_numpy()

min_aX = -15.00
collumn = 0
normalized_splits = []

normalized_splits = normal_splitting(collumn, min_aX, np_array, benchmark=True)
splitted_dataset = split_data_iterative(np_array, normalized_splits, benchmark=True)

show_dataset(splitted_dataset,13,26, benchmark=True)
# save_dataset("4455", splitted_dataset, benchmark=True)