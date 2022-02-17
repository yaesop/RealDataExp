import sys
import argparse
import glob
import cv2
import json
print(cv2.__version__)
a = argparse.ArgumentParser()
a.add_argument("--pathIn", help="path to video")
a.add_argument("--pathOut", help="path to images")
a.add_argument("--vidName", help="video name")
args = a.parse_args()
print(args)

#count = 0
#vidcap = cv2.VideoCapture(pathIn)# create a folder to store extracted images
import os
folder = 'DTRA_png'  
#os.mkdir(folder)
# use opencv to do the job
import cv2
videos = glob.glob(args.pathIn+ args.vidName +'/seq_mp4/*.mp4')
videos.sort()
vi = []
for vid in videos:
    if int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 2101 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 3601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 3301 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 4501 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 5701 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 6601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 8001 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 8901:
        vi.append(vid)

curr = 0

for section in range(6):
    
    if section == 0:
        xmin = 0
        ymin = 0
        xmax = 640
        ymax = 640
    elif section == 1:
        xmin = 640
        ymin = 0
        xmax = 1280
        ymax = 640
    elif section == 2:
        xmin = 1280
        ymin = 0
        xmax = 1920
        ymax = 640
    elif section == 3:
        xmin = 0
        ymin = 440
        xmax = 640
        ymax = 1080
    elif section == 4:
        xmin = 640
        ymin = 440
        xmax = 1280
        ymax = 1080
    elif section == 5:
        xmin = 1280
        ymin = 440
        xmax = 1920
        ymax = 1080
    for v in vi:
        print(v)
        vidcap = cv2.VideoCapture(v)
        count = 0
        sec = 0
        frameRate = 1/30 # Change this number to 1 for each 1 second
        f = open(v.replace(".mp4",".json"))
        data = json.load(f)
        #print(data)
        k = 0
        bbox = []
        
        for i in data:
            standing_tmp = ""
            frame_num = int(v.split('/')[-1].split('.')[0].split('-')[-1]) + k
            #print("new i ") 
            for ob in i:
                #print("ob ",ob) 
                if ob['category'].startswith('mannequin'):
                    pos = ob['category'].split('-')[-1]
                    #print(pos)
                    if ob['x']> xmin and ob['y']> ymin and ob['x']+ ob['width']< xmax and ob['y']+ ob['height']< ymax:
                        x = ob['x']
                        y = ob['y']
             
                        height = ob['height']
                        width = ob['width']
                        standing_tmp+= '0'
                        standing_tmp+=" "
                        standing_tmp+= str((x- xmin + width/2)/640) 
                        standing_tmp+=" "
                        standing_tmp+= str((y- ymin + height/2)/640) 
                        standing_tmp+=" "
                        standing_tmp+= str(width/640)
                        standing_tmp+=" "
                        standing_tmp+= str(height/640)
                        standing_tmp+="\n"
                    
            #print(standing_tmp)
            if len(v.split('/')[-1].split('.')[0].split('-')) ==  3:
                file1_s = open(args.pathOut + "training/labels/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1]  + "_%d_%d.txt" % (frame_num , section), "x")
            else:
                file1_s = open(args.pathOut + "training/labels/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1] + '-'+ v.split('/')[-1].split('.')[0].split('-')[2] + "_%d_%d.txt" % (frame_num , section), "x")
            
            file1_s.write(standing_tmp)
            standing_tmp = ""
            file1_s.close() #to change file access modes
            
            k = k + 1
        
    

