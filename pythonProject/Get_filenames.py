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



#### add kingdoms ####
#read xlsx
kingdoms = pd.read_excel('MAGsKingdom.xlsx')
genomes = pd.read_csv('all_genomes.txt', header=None)
# add kingdom to genomes
genomes['kingdom'] = ''

for i in range(len(genomes)):
    genome_name = genomes.iloc[i,0].split('/')[-1]
    try:
        kingdom = kingdoms[kingdoms['Name'] == genome_name]['kingdom'].values[0]
        genomes['kingdom'][i] = kingdom
    except:
        print(genome_name)
        genomes['kingdom'][i] = 'NA'

# save to csv
genomes.to_csv('all_genomes_kingdom.csv', index=False)