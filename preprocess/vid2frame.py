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
folder = 'DTRA_png_new2'  
#os.mkdir(folder)
# use opencv to do the job
import cv2
videos = glob.glob(args.pathIn+ args.vidName +'/seq_mp4/*.mp4')
videos.sort()
vi = []
#for vid in videos:
#    if int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 2101 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 3601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 3301 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 4501 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 5701 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 6601 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 8001 or int(vid.split('/')[-1].split('.')[0].split('-')[-1]) == 8901:
#        vi.append(vid)

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
        def getFrame(sec, bbox, curr):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                frame_num = int(v.split('/')[-1].split('.')[0].split('-')[-1]) + count
                len_num = len(v.split('-')[-1])
                #cv2.rectangle(image, (bbox[curr][0], bbox[curr][1]), (bbox[curr][2], bbox[curr][3]), (0, 255, 0))
                #print(v.split('/')[-1].split('.')[0].split('-'))
                if len(v.split('/')[-1].split('.')[0].split('-')) ==  3:
                    cv2.imwrite(args.pathOut + "DTRA_png_new2/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-'+ v.split('/')[-1].split('.')[0].split('-')[1]  + "_%d_%d.png" % (frame_num , section), image[ymin:ymax, xmin:xmax]) # Save frame as PNG file   
                else:
                    cv2.imwrite(args.pathOut + "DTRA_png_new2/"+ v.split('/')[-1].split('.')[0].split('-')[0] + '-'+ v.split('/')[-1].split('.')[0].split('-')[1] + '-'+ v.split('/')[-1].split('.')[0].split('-')[2]  + "_%d_%d.png" % (frame_num , section), image[ymin:ymax, xmin:xmax]) # Save frame as PNG file   
            print("capturing "+ str(count), " section:" , str(section))
            return hasFrames
        sec = 0
        frameRate = 1/30 # Change this number to 1 for each 1 second
        f = open(v.replace(".mp4",".json"))
        data = json.load(f)
        #print(data)
        k = 0
        bbox = []
        temp = []
        frame_num = int(v.split('/')[-1].split('.')[0].split('-')[-1]) + k
        
        success = getFrame(sec, bbox, curr)
        while success:
            curr = curr + 1
            count = count + 1
            sec = sec + frameRate
            success = getFrame(sec, bbox, curr)
            #if count==299:
            #    break
    

