import numpy as np
import pandas as pd
from glob import glob
from IPython import embed



a222_op = [[140,450]]*18+[[[140,220],[340,450]]]*22+[[[140,210],[350,450]]]*10+[[[140,200],[355,450]]]*5+[[[140,205],[55,90]]]*25
a223_op = [[320,640]]*30+[[[160,280],[320,400]]]*30+[[[220,280],[320,395]]]*20
r_a222 = np.linspace(0,8,81)
r_a223 = np.linspace(0,8,81)
annu_num = 80


rlst = {'a222':r_a222,'a223':r_a223}
oplst = {'a222':a222_op,'a223':a223_op}

def cal_area(r,op):
    area_mat = np.zeros((2,len(r_a222)))
    for i in range(len(r_a222)-1):
        j = 0
        ele = np.array(op[i])
        if len(ele.shape) < 2:
            area_mat[:,i] = (r[i+1]**2-r[i]**2)*3.14*abs(np.diff(ele))/360
            j += 1
            print(j)
        else:
            for n in range(2):
                area_mat[j,i] = (r[i+1]**2-r[i]**2)*3.14*abs(ele[n][1]-ele[n][0])/360
                j += 1
                print(j)
    return area_mat
            
for j in [2,3]:
    data = np.ones((5, len(r_a222))) *np.nan
    newfname = f'a22{j}_annu_pandas_table_radial_230113_ppspcm2parcmin2.csv'
    area = cal_area(rlst[f'a22{j}'], oplst[f'a22{j}'])
    print(area)
    for i in range(len(r_a222)-1):
        files = glob(f'a22{j}_annu_{i+1}_pandas_ds9_radial_230113_*_ppspcm2pam2.log')
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
    
    data[2] = np.nanmean(data[:2], axis=0)
    data[3] = np.nanstd(data[:2], axis=0)
    data[4] = data[3]/data[2]*100
    df = pd.DataFrame(data, index=[f'panda{i+1}' for i in range(2)] 
    + ['mean', 'std','std/mean(%)'],columns=[f'annu{i+1}' for i in range(len(r_a222))])
    df.to_csv(newfname)
    print(df)