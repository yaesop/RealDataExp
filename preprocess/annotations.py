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
    for v in videos:
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
            kneeling_tmp = ""
            lying_tmp = ""
            frame_num = int(v.split('/')[-1].split('.')[0].split('-')[-1]) + k
            #print("new i ") 
            for ob in i:
                #print("ob ",ob) 
                if ob['category'].startswith('mannequin'):
                    pos = ob['category'].split('-')[-1]
                    #print(pos)
                    if pos.startswith(" standing") and ob['x']> xmin and ob['y']> ymin and ob['x']+ ob['width']< xmax and ob['y']+ ob['height']< ymax:
                        x = ob['x']
                        y = ob['y']
             
                        height = ob['height']
                        width = ob['width']
                        standing_tmp+= "person"
                        standing_tmp+=" "
                        standing_tmp+= str(x- xmin) 
                        standing_tmp+=" "
                        standing_tmp+= str(y- ymin) 
                        standing_tmp+=" "
                        standing_tmp+= str(width)
                        standing_tmp+=" "
                        standing_tmp+= str(height)
                        standing_tmp+="\n"
                    elif pos.startswith(" kneeling") and ob['x'] > xmin and ob['y']> ymin and ob['x']+ ob['width']< xmax and ob['y']+ ob['height']< ymax:
                        x = ob['x']
                        y = ob['y']
                        height = ob['height']
                        width = ob['width']
                        kneeling_tmp+= "person"
                        kneeling_tmp+=" "
                        kneeling_tmp+= str(x- xmin) 
                        kneeling_tmp+=" "
                        kneeling_tmp+= str(y- ymin) 
                        kneeling_tmp+=" "
                        kneeling_tmp+= str(width)
                        kneeling_tmp+=" "
                        kneeling_tmp+= str(height)
                        kneeling_tmp+="\n"
                    elif pos.startswith(" lying down") and ob['x']> xmin and ob['y']> ymin and ob['x']+ ob['width']< xmax and ob['y']+ ob['height']< ymax:
                        x = ob['x']
                        y = ob['y']
                        height = ob['height']
                        width = ob['width']
                        lying_tmp+= "person"
                        lying_tmp+=" "
                        lying_tmp+= str(x- xmin) 
                        lying_tmp+=" "
                        lying_tmp+= str(y- ymin) 
                        lying_tmp+=" "
                        lying_tmp+= str(width)
                        lying_tmp+=" "
                        lying_tmp+= str(height)
                        lying_tmp+="\n"
            
            #print(standing_tmp)
            if len(v.split('/')[-1].split('.')[0].split('-')) ==  3:
                file1_s = open(args.pathOut + "DTRA_gt/standing/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1]  + "_%d_%d.txt" % (frame_num , section), "x")
            else:
                file1_s = open(args.pathOut + "DTRA_gt/standing/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1] + '-'+ v.split('/')[-1].split('.')[0].split('-')[2] + "_%d_%d.txt" % (frame_num , section), "x")
            
            file1_s.write(standing_tmp)
            standing_tmp = ""
            file1_s.close() #to change file access modes

            if len(v.split('/')[-1].split('.')[0].split('-')) ==  3:
                file1_k = open(args.pathOut + "DTRA_gt/kneeling/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1]  + "_%d_%d.txt" % (frame_num , section), "x")
            else:
                file1_k = open(args.pathOut + "DTRA_gt/kneeling/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1] + '-'+ v.split('/')[-1].split('.')[0].split('-')[2] + "_%d_%d.txt" % (frame_num , section), "x")
            
            file1_k.write(kneeling_tmp)
            kneeling_tmp = ""
            file1_k.close() #to change file access modes

            if len(v.split('/')[-1].split('.')[0].split('-')) ==  3:
                file1_l = open(args.pathOut + "DTRA_gt/lying/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1]  + "_%d_%d.txt" % (frame_num , section), "x")
            else:
                file1_l = open(args.pathOut + "DTRA_gt/lying/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-' + v.split('/')[-1].split('.')[0].split('-')[1] + '-'+ v.split('/')[-1].split('.')[0].split('-')[2] + "_%d_%d.txt" % (frame_num , section), "x")
            
            file1_l.write(lying_tmp)
            lying_tmp = ""
            file1_l.close() #to change file access modes


            k = k + 1
        
    

