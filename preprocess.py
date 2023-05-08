import pandas as pd

df = pd.read_csv('data/train.txt', sep=' ', header=None)

with open('data/labels.txt', 'w') as fout:
    for tag in df[1].unique():
        fout.write(tag + '\n')
