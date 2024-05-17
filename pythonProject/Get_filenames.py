# get file names under all subdirectory and save to csv

import pandas as pd
import os

def get_filenames(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            file_list.append(os.path.join(root, file))

    return file_list

path = '/test'
all_fnas = get_filenames(path)


df = pd.DataFrame(all_fnas, columns=['filename'])
df.to_csv('all_filenames.csv', index=False)

