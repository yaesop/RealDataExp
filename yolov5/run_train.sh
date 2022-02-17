#!/bin/bash

python train.py --imgsz 640 --data data/real.yaml --nosave --freeze 200 --weights yolov5n.pt --device 0

#n 270 layers -> freezed 200 layers

