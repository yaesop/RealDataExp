#!/bin/bash


for model in n; do  #nano small medium large; do
cd /media/yaesop/ARL_FZNV/DTRA/real_result/
mkdir detect_trained_${model}
cd ~/RealDataExp/yolov5/
python detect.py --imgsz 640 --save-txt --save-conf --nosave --source /media/yaesop/ARL_FZNV/DTRA/DTRA_png/ --weights yolov5_${model}_trained2.pt --project /media/yaesop/ARL_FZNV/DTRA/real_result/detect_trained_${model}/ --classes 0
done

