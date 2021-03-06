import os, sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors
import matplotlib as mpl

#x, y = np.random.rand(2, 100) * 4
#hist, xedges, yedges = np.histogram2d(x, y, bins=15, range=[[5, 80], [5, 80]])
model = sys.argv[1]
position = sys.argv[2]

#######nano result #####
result = []
text_file = open("/home/yaesop/syn_result/output_"+ model +"_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result.append(float(tmp))
    k=k+1
result = np.array(result)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_"+model+"_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk = 0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result[kk] = result[kk] + float(tmp)
            kk=kk+1
        k=k+1


for r in range(len(result)):

    result[r] = result[r]/4

result_tmp=[]
#print(result)
#print(result_tmp)
for r in range(len(result)):
    
    if r % 16 >= 2 and r % 16 < 10 and r< 154 and r>= 32: 
        #print(r )   
        result_tmp.append(result[r])
print(len(result_tmp))
zpos=np.array(result_tmp)

fig=plt.figure(figsize=(6, 6), dpi=180)
ax1=fig.add_subplot(111, projection='3d')

ylabels = np.array([15, 20, 25, 30, 35, 40, 45, 50])

#xlabels = np.flip(xlabels)
ypos = np.arange(ylabels.shape[0])
xlabels = np.array([15, 20, 25, 30, 35, 40, 45, 50])
#xlabels = np.flip(ylabels)
xpos = np.arange(xlabels.shape[0])

xposM, yposM = np.meshgrid(xpos, ypos, copy=False)


zpos = zpos.ravel()

dx=0.3
dy=0.3
dz=zpos


ax1.w_xaxis.set_ticks(xpos + dx/5.)
ax1.w_xaxis.set_ticklabels(xlabels)

ax1.w_yaxis.set_ticks(ypos + dy/5.)
ax1.w_yaxis.set_ticklabels(ylabels)
ax1.set_title("")

#values = np.linspace(0.2, 1.,zpos.ravel().shape[0])

colors_val = cm.jet_r(zpos/100)

ax1.bar3d(xposM.ravel(), yposM.ravel(), dz*0, dx, dy, dz, color=colors_val)
ax1.set_xlabel('Height')
ax1.set_ylabel('Radius')
ax1.set_zlim3d(0,100)
#ax1.view_init(0, 0)
#ax1.set_box_aspect
colourMap = plt.cm.ScalarMappable(cmap=plt.cm.jet_r)
colourMap.set_array(zpos)
colourMap.set_clim(0,100)
fig.colorbar(colourMap, shrink=0.4)
plt.title(position+" position "+"yolo-"+model+'\n'+ "Average: "+str(sum(zpos)/64))
plt.savefig('/home/yaesop/real_result/syn_'+model+'_'+position+'.png')
print(model, " ", position,":", sum(zpos)/64)
#plt.show()


#plt.show()
