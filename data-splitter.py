import pandas as pd
import numpy as np
# validates wether the position of the splitting points actually correspond to the splitting points in the original dataset (csv_file)
def val_split_pos(split = np.array, csv_file = np.array, collumn = 0):
    i=0
    while(split.size > i):
        if ((split[collumn][i]  != csv_file[collumn][i])):
            return False
        i += 1
    return True

def val_multiple(split = np):
    # if(split[1].isin[split]):
    return 999

path =  'Data/2451_Shooting.csv'
csv_file = pd.read_csv(path)
np_array = csv_file.to_numpy()

min_aX=-15.00
row = 0
collumn = 0
splits = {}
# print(np_array[1][0])

while(len(np_array) > row):
    if(np_array[row][collumn] < min_aX):
        splits[row] = np_array[row][collumn]
    row += 1
print("{},{}".format(splits , len(splits)))
# print(splits[3360])

# print('Values fit: {} | any Values found: {} | doubled Values: {}'.format(val_split_pos(splits, csv_file), splits.size, val_multiple()) )