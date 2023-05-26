#!/usr/bin/env python3
import pandas as pd
import glob
import time

csv_files = glob.glob('data/in_csv/*.csv')
start_time = time.strftime("%Y%m%d_%H:%M:%S")

for a in csv_files:
    print(a)

data_list = []
for file in csv_files:
    data_list.append(pd.read_csv(file))

df = pd.concat(data_list, axis=0, sort=True)
df.to_csv('data/out_csv/' + start_time + '.csv', index=False)