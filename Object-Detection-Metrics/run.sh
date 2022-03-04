#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
cd ~/RealDataExp/Object-Detection-Metrics/
rm -rf output.txt
for model in n s m l x; do
for position in standing kneeling lying; do
for  radius in 15 20 25 30 35 40 45 50; do
for  altitude in 15 20 25 30 35 40 45 50  ; do

    rm -rf groundtruths/
    mkdir groundtruths
    rm -rf detections/
    mkdir detections
    #python detectionConvert_wo_pole.py $altitude $radius $model $position
    python detectionConvert.py $altitude $radius $model $position
    cd ~/RealDataExp/Object-Detection-Metrics/detections
    for f in ./*.txt; do
        #echo "$f"
        cp  /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/"$position"/"$f" ../groundtruths/
    done
    cd ~/RealDataExp/Object-Detection-Metrics/
    python pascalvoc.py --threshold 0.5 -detformat xywh -gtformat xywh -np  > tmp/output.txt
    echo $altitude $radius >> output.txt
    cat tmp/output.txt >> output.txt
done
done
    mv output.txt output_${position}_${model}_trained.txt
    rm -rf output.txt
done
done 
