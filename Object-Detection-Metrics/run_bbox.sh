#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
#cd ~/RealDataExp/Object-Detection-Metrics/
rm -rf output.txt
rm -rf tmp/output.txt

for position in lying; do
for  radius in 15 20 25 30 35 40 45 50; do
for  altitude in 15 20 25 30 35 40 45 50  ; do

    echo $altitude $radius >> output.txt
    python bbox_size.py $altitude $radius $position #>> output.txt

done
done
    mv output.txt output_${position}_size.txt
    rm -rf output.txt
done
 

for position in standing kneeling; do 


    python plotting_size.py $position


done
