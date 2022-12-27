import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# validates wether the position of the splitting points actually correspond to the splitting points in the original dataset (csv_file)
def val_split_pos(split = [], np_array = np.array, collumn = 0):
    i=0
    for row,value in split:
        if not (value == np_array[row][collumn]):
            return False
    return True

# searches for multiple peaks at the same points to avoid too small splits
def del_val_multiple(split):
    single_vals = []
    for i in range(len(split)-1):
        if not (split[i][1] == split[(i+1)][1]):
            single_vals.append(split[i][0])

    return single_vals

# splits the dataset at a givin value, no smoothening or anything, you have to applay del_va_multiple to have correct results
def normal_splitting(collumn = 0, min_aX = -15.00, splits = [], np_array = np.array):
    row = 0
    while(len(np_array) > row):
        if(np_array[row][collumn] < min_aX):
            splits.append([row,np_array[row][collumn]])
        row += 1

    return del_val_multiple(splits)

def split_data(np_array = np.array, splits = []):
    # data_splitted = np.array([])
    data_splitted = np.empty((len(np_array),3), dtype=float)
    old = 0

    for i in range(len(splits)):
        tmp = np_array[old: splits[i]].copy()
        print(tmp)
        data_splitted = np.append(data_splitted, tmp , 0) 
        
        print("{} | {} ".format(old, splits[i]))
        old = splits[i]
        

    return data_splitted


##################################################
##########THE REAL PROGRAMM ######################
##################################################

path =  'Data/2451_Shooting.csv'
csv_file = pd.read_csv(path)
np_array = csv_file.to_numpy()
print(np_array)

min_aX = -15.00
collumn = 0
splits = []
normalized_splits = []

normalized_splits = normal_splitting(collumn, min_aX, splits, np_array)

# print("all: {} \n normalized: {} ".format(splits, normalized_splits))
print("\n##############################################################################\n")

splitted_dataset = split_data(np_array, normalized_splits)

print("0 ::: {}".format(splitted_dataset[0][0]))
print("1 ::: {}".format(splitted_dataset[1][0]))

#for i in range(len(splitted_dataset)):
#    plt.plot(splitted_dataset[i])
#    plt.ylabel("splitted_datasert {}".format(i))
#    plt.show()