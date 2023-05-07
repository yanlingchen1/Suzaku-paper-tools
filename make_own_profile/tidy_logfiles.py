import numpy as np
import pandas as pd
from glob import glob
from IPython import embed

# r_a222 = [0,1,2.5,3.5,5,7]
# r_a223 = [0,1,2,3,5.5,8]
# a222_op = [np.linspace(140,450,6), np.array([[140,190,240],[330,390,450]]), np.array([[140,180,220],[340,395,450]]), np.array([[140,175,210],[350,400,450]]), [[140,170,200],[50,90]]]
# a223_op = [np.linspace(320,640,6), np.linspace(320,640,6), np.linspace(320,640,6), np.array([[193,236,280],[320,365,410]]),np.array([[220,250,280],[320,355,390]])]
r_a222 = [0,0.5,1,1.5,2.5,3.5,5,6,7]
r_a223 = [0,0.5,1,2,3.5,5,6.5, 7.5, 8.5]
a222_op = [np.linspace(140,450,6), np.linspace(140,450,6), 
[[140,190,240],[330,390,450]], [[140,190,240],[330,390,450]], 
[[140,180,220],[340,395,450]], [[140,175,210],[350,400,450]], 
[[140,170,200],[50,90]], [[140,170,200],[50,90]]]
a223_op = [np.linspace(320,640,6),np.linspace(320,640,6),
 np.linspace(320,640,6),np.linspace(320,640,6),
  [[193,236,280],[320,365,410]],[[193,236,280],[320,365,410]],
  [[220,250,280],[320,355,390]],[[220,250,280],[320,355,390]]]

rlst = {'a222':r_a222,'a223':r_a223}
oplst = {'a222':a222_op,'a223':a223_op}

def cal_area(r,op):
    area_mat = np.zeros((5,len(r_a222)))
    for i in range(len(r_a222)-1):
        j = 0
        if len(op[i]) == 6:
            area_mat[:,i] = (r[i+1]**2-r[i]**2)*3.14*abs(np.diff(op[i]))/360
            j += 5
            print(j)
        else:
            for m in op[i]:
                for n in range(len(m)-1):
                    area_mat[j,i] = (r[i+1]**2-r[i]**2)*3.14*abs(m[n+1]-m[n])/360
                    j += 1
                    print(j)
    return area_mat
            
for j in [2,3]:
    data = np.ones((8, len(r_a222))) *np.nan
    newfname = f'a22{j}_annu_pandas_table_230113_ppspcm2parcmin2.csv'
    area = cal_area(rlst[f'a22{j}'], oplst[f'a22{j}'])
    print(area)
    for i in range(len(r_a222)-1):
        files = glob(f'a22{j}_annu_{i+1}_pandas_ds9_new_230113_*_ppspcm2pam2.log')
        for file in files:  
            n = int(file.split('.')[0].split('_')[-2])-1
            f = open(file)
            print(n,i,file)
            lst = f.readlines()
            if 'Error' in lst[1]:
                continue  
            else:
                sum_ph = lst[3].split('=')[-1]
                data[n][i] = float(sum_ph)/area[n][i]
            f.close()
    
    data[5] = np.nanmean(data[:5], axis=0)
    data[6] = np.nanstd(data[:5], axis=0)
    data[7] = data[6]/data[5]*100
    df = pd.DataFrame(data, index=[f'panda{i+1}' for i in range(5)] 
    + ['mean', 'std','std/mean(%)'],columns=[f'annu{i+1}' for i in range(len(r_a222))])
    df.to_csv(newfname)
    print(df)