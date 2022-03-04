#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done



for position in standing lying kneeling; do 
for mdl in n s m l x ; do  #nano small medium large; do

    python plotting.py $mdl $position

done
done

#for position in stand squat prone; do 
#for mdl in n s m l x ; do  #nano small medium large; do
#    python plot_2compare.py $mdl $position 
#done
#done


