#!/bin/bash


for model in n s m l x; do  #nano small medium large; do
cd /home/yaesop/real_result/
mkdir detect_${model}
cd ~/RealDataExp/yolov5/
python detect.py --imgsz 640 --save-txt --save-conf --nosave --source /media/yaesop/ARL_FZNV/DTRA/DTRA_png/ --weights yolov5${model}.pt --project /home/yaesop/real_result/detect_${model}/ --classes 0


done

