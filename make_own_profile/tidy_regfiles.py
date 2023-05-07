import numpy as np

a222_op = [np.linspace(140,450,6), np.linspace(140,450,6), 
[[140,190,240],[330,390,450]], [[140,190,240],[330,390,450]], 
[[140,180,220],[340,395,450]], [[140,175,210],[350,400,450]], 
[[140,170,200],[50,90]], [[140,170,200],[50,90]]]
a223_op = [np.linspace(320,640,6),np.linspace(320,640,6),
 np.linspace(320,640,6),np.linspace(320,640,6),
  [[193,236,280],[320,365,410]],[[193,236,280],[320,365,410]],
  [[220,250,280],[320,355,390]],[[220,250,280],[320,355,390]]]

annu_num = 100
para_dict = {'a222':['1:37:33.0609,-12:59:20.358', a222_op,[0,0.5,1,1.5,2.5,3.5,5,6,7]],
'a223':['1:37:55.8571,-12:49:13.855', a223_op, [0,0.5,1,2,3.5,5,6.5, 7.5, 8.5]]}

savepath = './regfiles'
for j in [2,3]:
    for i in range(annu_num):
        iterator = 0
        if len(para_dict[f'a22{j}'][1][i]) ==6:
            for n in range(5):
                iterator +=1
                newf = open(f'a22{j}_annu_{i+1}_pandas_ds9_new_230113_{iterator}.reg', 'w')  
                newf.write(f"panda({para_dict[f'a22{j}'][0]},{para_dict[f'a22{j}'][1][i][n]},{para_dict[f'a22{j}'][1][i][n+1]},1,{para_dict[f'a22{j}'][2][i]}',{para_dict[f'a22{j}'][2][i+1]}',1)\n")
        else:
            for m in para_dict[f'a22{j}'][1][i]:
                for n in range(len(m)-1):
                    iterator +=1
                    newf = open(f'a22{j}_annu_{i+1}_pandas_ds9_new_230113_{iterator}.reg', 'w')  
                    newf.write(f"panda({para_dict[f'a22{j}'][0]},{m[n]},{m[n+1]},1,{para_dict[f'a22{j}'][2][i]}',{para_dict[f'a22{j}'][2][i+1]}',1)\n")
        newf.close()

        