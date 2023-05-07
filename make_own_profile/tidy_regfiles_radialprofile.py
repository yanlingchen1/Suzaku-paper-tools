import numpy as np

a222_op = [[140,450]]*18+[[[140,220],[340,450]]]*22+[[[140,210],[350,450]]]*10+[[[140,200],[355,450]]]*5+[[[140,205],[55,90]]]*25
a223_op = [[320,640]]*30+[[[160,280],[320,400]]]*30+[[[220,280],[320,395]]]*20

annu_num = 80
para_dict = {'a222':['1:37:33.0609,-12:59:20.358', a222_op,np.linspace(0,8,81)],
'a223':['1:37:55.8571,-12:49:13.855', a223_op, np.linspace(0,8,81)]}

savepath = './'
for j in [2,3]:
    for i in range(annu_num):
        iterator = 0
        ele = np.array(para_dict[f'a22{j}'][1][i])
        if len(ele.shape)==1:
            iterator +=1
            newf = open(f'{savepath}/a22{j}_annu_{i+1}_pandas_ds9_radial_230113_{iterator}.reg', 'w')  
            newf.write(f"panda({para_dict[f'a22{j}'][0]},{ele[0]},{ele[1]},1,{para_dict[f'a22{j}'][2][i]}',{para_dict[f'a22{j}'][2][i+1]}',1)\n")
        else:
            for n in range(2):
                iterator +=1
                newf = open(f'{savepath}/a22{j}_annu_{i+1}_pandas_ds9_radial_230113_{iterator}.reg', 'w')  
                newf.write(f"panda({para_dict[f'a22{j}'][0]},{ele[n][0]},{ele[n][1]},1,{para_dict[f'a22{j}'][2][i]}',{para_dict[f'a22{j}'][2][i+1]}',1)\n")
            
        newf.close()

        