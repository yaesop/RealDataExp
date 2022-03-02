Experiment for the Archangel data.

- Preprocess 
	vid2frame.py - split the original video into multiple sub-images.
	annotations.py - Parse the original annotation file to txt files.
	training_anno.py - Parse the original annotation to YOLOv5 style annotation file for training. 
	run.sh - run the preprocessing for the archangel dataset

- yolov5
	Pulled from the YOLOv5 github. 
	Pretrained models are already in the directory. 
	run_train.sh -> bash script for training. may need to change the input/output directory
	run_real.sh -> bash script for inferencing.  may need to change the input/o
utput directory


***Dataset for training : /media/yaesop/ARL_FZNV/DTRA/training/
***Dataset for testing : /media/yaesop/ARL_FZNV/DTRA/DTRA_png/
***Dataset for calculating the result (groundtruth) : /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/
- Object-Detection-Metrics
	Calculate mAP from the result. 
	run.sh -> bash script to calculate the performance. It will output_[pose]_[model].txt
	run_plot -> bash script to plot the bar graph using the result from each output_[pose]_[model].
	

