import pandas as pd
import numpy as np

import time
import timeit

# import matplotlib.pyplot as plt

# validates wether the position of the splitting points actually correspond to the splitting points in the original dataset (csv_file)
def val_split_pos(split = [], np_array = np.array, collumn = 0):
    start = time.perf_counter()
    i=0
    for row,value in split:
        if not (value == np_array[row][collumn]):
            return False

    print("valsplitpos time: {}".format(time.perf_counter()-start))
    return True

# searches for multiple peaks at the same points to avoid too small splits
def del_val_multiple(split):
    start = time.perf_counter()
    single_vals = []
    for i in range(len(split)-1):
        if not (split[i][1] == split[(i+1)][1]):
            single_vals.append(split[i][0])
    print("delvalmult t: {}".format(time.perf_counter()-start))
    return single_vals

# splits the dataset at a givin value, no smoothening or anything, you have to applay del_va_multiple to have correct results
def normal_splitting(collumn = 0, min_aX = -15.00, splits = [], np_array = np.array):
    start = time.perf_counter()
    row = 0
    while(len(np_array) > row):
        if(np_array[row][collumn] < min_aX):
            splits.append([row,np_array[row][collumn]])
        row += 1

    print("normalsplittimg t: {}".format(time.perf_counter()-start))
    return del_val_multiple(splits)

def split_data(np_array = np.array, splits = []):
    start = time.perf_counter()
    # data_splitted = np.array([])
    data_splitted = np.empty((0,len(splits)))
    print(data_splitted)
    old = 0

    for i in range(len(splits)):
        tmp = np_array[old: splits[i]].copy()
        print("tmp: {}".format(tmp))
        data_splitted = np.append(data_splitted, [tmp], axis=1)

        print("data_splitted: {}".format(data_splitted[i]))
        old = splits[i]
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    print("splitdata t: {}".format(time.perf_counter()-start))
    return data_splitted

def split_data_ez(np_array = np.array, splits = []):
    start = time.perf_counter()
    old = 0
    splitted = []

    for i in range(len(splits)):
        tmp = np_array[old:splits[i]].copy()
        splitted.append(tmp)
    print("splitdataez: {}".format(time.perf_counter()-start))

    return splitted


##################################################
##########THE REAL PROGRAMM ######################
##################################################

print(" Started")
path =  'Data/2451_Shooting.csv'
csv_file = pd.read_csv(path)
np_array = csv_file.to_numpy()
# print(np_array)

min_aX = -15.00
collumn = 0
splits = []
normalized_splits = []

normalized_splits = normal_splitting(collumn, min_aX, splits, np_array)

# print("all: {} \n normalized: {} ".format(splits, normalized_splits))
print("\n##############################################################################\n")

split_data_ez(np_array, normalized_splits)

#print("0 ::: {}".format(splitted_dataset[0][0]))
#print("1 ::: {}".format(splitted_dataset))



#for i in range(len(splitted_dataset)):
#    plt.plot(splitted_dataset[i])
#    plt.ylabel("splitted_datasert {}".format(i))
#    plt.show()
