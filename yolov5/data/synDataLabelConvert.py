import json
import glob, os
import sys
# Opening JSON file
name = sys.argv[1]
altitude = sys.argv[2]
radius = sys.argv[3]
model = sys.argv[5]
position = sys.argv[6]
#print(position)
#imgs = glob.glob('../../yolov5/runs/detect/'+expNum+'/labels/*.txt')
datasetName = '/media/ARL_FZNV/DTRA/DTRA_png/*.png'
#print(datasetName.split('/'))
imgs = glob.glob(datasetName)
#print(datasetName)

#xywh -> 1,2,3,4
k=0
imgs.sort()
imgs_selected = []
for img in imgs:
    if img.split('/')[-1].split('.')[0].split("_")[4]==altitude and img.split('/')[-1].split('.')[0].split("_")[4]==radius:
        imgs_selected.append(img)
imgs_selected.sort()
for img in imgs_selected:
    fileName = '/home/yaesop/real_result/detect_'+model+'/exp/labels/'+ img.split('/')[7].split('.')[0]+".txt"
    #print(fileName)

    if os.path.exists(fileName):

        with open(fileName) as f:
            for fLine in f:
                tmp=""
                if fLine.startswith("0"):
                    tmp="person"   
                    tmp+=" "
                    tmp+= str(float(fLine.split(" ")[5]))
                    tmp+=" "
                    tmp+= str( float(fLine.split(" ")[1])*512)
                    tmp+=" "
                    tmp+= str( float(fLine.split(" ")[2])*512)
                    tmp+=" "
                    tmp+= str( float(fLine.split(" ")[3])*512)
                    tmp+=" "
                    tmp+= str(float(fLine.split(" ")[4])*512)
    else:
        tmp="person"   
        tmp+=" "
        tmp+= str(0)
        tmp+=" "
        tmp+= str(0)
        tmp+=" "
        tmp+= str(0)
        tmp+=" "
        tmp+= str(0)
        tmp+=" "
        tmp+= str(0)
    file1 = open('../../Object-Detection-Metrics/detections/'+fileName.split('/')[-1],"x")
    file1.write(tmp)
    file1.close() #to change file access modes
    k= k+1
