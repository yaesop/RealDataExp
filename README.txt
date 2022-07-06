Experiment for the real data

yolov5/ contains the script to run the evaluation (run_real.sh).
You should modify the run_real.sh for each experiment set.

Object-detection.../ contains the code to change formats of the produced result files and groundtruth files into eligible format. 
You should modify run.sh for each experiment set. 

If you are using combined version, you should make sure that the python code has contains the "_combined" in the end of the file names. 

run_plot_data1.sh and run_plot_data2.sh will create the graphs for each dataset results. (Here, if _data1 means the experiments that are evaluated on data1. Nothing to do with the dataset that is used during the training.)

