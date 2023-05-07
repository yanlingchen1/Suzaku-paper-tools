import numpy as np
import pandas as pd
import sys

type = sys.argv[1]
num = 99
pixarea = 2.316e-3**2*3600
for x in [0,1,3]:
    data = np.ones((4,num))*np.nan
    for j in range(num):
        ctsfile = f'annu{j}_xis{x}_{type}_purects.log'
        expfile = f'annu{j}_xis{x}_{type}_s.log'
        filelst = [ctsfile, expfile]
        for i in range(2):  
            # print(filelst[i])
            f = open(filelst[i])
            lst = f.readlines()
            if 'Error' in lst[1]:
                continue  
            else:
                sum_ph = lst[3].split('=')[-1]
                data[i][j] = float(sum_ph)
            f.close()
    data = data.T
    data[:,2] = data[:,0]/data[:,1]/pixarea
    data[:,3] = np.sqrt(data[:,0])/data[:,1]/pixarea
    df = pd.DataFrame(data, index=[f'annu{i+1}' for i in range(num)]
    ,columns=['cts','exp','ctr', 'err'])
    df.to_csv(f'xis{x}_{type}.csv')
    print(df)