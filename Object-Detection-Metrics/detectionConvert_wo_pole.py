import sys
import glob

altitude = sys.argv[1]
radius = sys.argv[2]
model = sys.argv[3]
position = sys.argv[4]
selected = []
data4al = []
if altitude == "15":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"_new/exp/labels/*.txt")
    
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-10"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 600 and frame_num < 1800:
            selected.append(res)
        elif radius == str(45) and  frame_num > 1901 and frame_num <3100 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3301 and frame_num < 4300 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4501 and frame_num < 5501 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5700 and frame_num < 6600 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 6550 and frame_num < 7600 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7801 and frame_num < 8500 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8700 and frame_num < 9200 :
            selected.append(res)
elif altitude == "20":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-11"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 600 and frame_num < 1800:
            selected.append(res)
        elif radius == str(45) and  frame_num > 2100 and frame_num <3100 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3301 and frame_num < 4300 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4601 and frame_num < 5501 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5700 and frame_num < 6700 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 6900 and frame_num < 7600 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7801 and frame_num < 8500 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8700 and frame_num < 9400 :
            selected.append(res)
elif altitude == "25":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-5"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 600 and frame_num < 1800:
            selected.append(res)
        elif radius == str(45) and  frame_num > 2100 and frame_num <3100 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3301 and frame_num < 4300 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4601 and frame_num < 5501 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5700 and frame_num < 6700 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 6900 and frame_num < 7600 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7801 and frame_num < 8500 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8700 and frame_num < 9400 :
            selected.append(res)
elif altitude == "30":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-6"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 700 and frame_num < 1800:
            selected.append(res)
        elif radius == str(45) and  frame_num > 2100 and frame_num <3100 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3301 and frame_num < 4300 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4501 and frame_num < 5501 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5700 and frame_num < 6700 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 6900 and frame_num < 7600 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7801 and frame_num < 8500 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8700 and frame_num < 9300 :
            selected.append(res)
elif altitude == "35":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-6"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        # 16500 - 17500 
        # 18000 - 18900 
        # 19201 - 20400 
        if radius == str(50) and frame_num > 19201   and frame_num < 20400:
            selected.append(res)
        elif radius == str(45) and  frame_num > 18000 and frame_num < 18900 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 16500 and frame_num < 17500 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 15300 and frame_num < 16200 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 14400 and frame_num < 15200 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 13300 and frame_num < 14300 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 12300 and frame_num < 13100 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 11600 and frame_num < 12200 :
            selected.append(res)
elif altitude == "40":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-8"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 600 and frame_num < 1900:
            selected.append(res)
        elif radius == str(45) and  frame_num > 2100 and frame_num <3200 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3501 and frame_num < 4500 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4800 and frame_num < 5700 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5900 and frame_num < 6800 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 7000 and frame_num < 7800 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7901 and frame_num < 8700 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8800 and frame_num < 9400 :
            selected.append(res)
elif altitude == "45":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-8"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        # 16500 - 17500 
        # 18000 - 18900 
        # 19201 - 20400 
        if radius == str(50) and frame_num > 19201   and frame_num < 20400:
            selected.append(res)
        elif radius == str(45) and  frame_num > 18000 and frame_num < 18900 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 16500 and frame_num < 17500 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 15300 and frame_num < 16200 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 14400 and frame_num < 15200 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 13300 and frame_num < 14300 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 12300 and frame_num < 13100 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 11600 and frame_num < 12200 :
            selected.append(res)
elif altitude == "50":
    dataset = glob.glob("/home/yaesop/real_result/detect_"+model+"/exp/labels/*.txt")
    for data in dataset:
        if data.split("/")[-1].startswith("DTRA_Trial-9"):
            data4al.append(data)
    for res in data4al:
        frame_num = int(res.split("/")[-1].split("_")[-2])
        if radius == str(50) and frame_num > 600 and frame_num < 1800:
            selected.append(res)
        elif radius == str(45) and  frame_num > 2100 and frame_num <3100 :
            selected.append(res)
        elif radius == str(40) and  frame_num > 3301 and frame_num < 4300 :
            selected.append(res)
        elif radius == str(35) and  frame_num > 4601 and frame_num < 5501 :
            selected.append(res)
        elif radius == str(30) and  frame_num > 5700 and frame_num < 6700 :
            selected.append(res)
        elif radius == str(25) and  frame_num > 6900 and frame_num < 7600 :
            selected.append(res)
        elif radius == str(20) and  frame_num > 7801 and frame_num < 8500 :
            selected.append(res)
        elif radius == str(15) and  frame_num > 8700 and frame_num < 9400 :
            selected.append(res)
#print(selected)
tmp = ""
gt = ""
gt_other1 = ""
gt_other2 = ""
if position == "standing":
    position_other1 = "lying"
    position_other2 = "kneeling"
elif position == "lying":
    position_other1 = "standing"
    position_other2 = "kneeling"
elif position == "kneeling":
    position_other1 = "standing"
    position_other2 = "lying"

for fileName in selected:
    with open(fileName) as f:
        gt_fileName = "/media/yaesop/ARL_FZNV/DTRA/DTRA_gt/"+position+"/" +fileName.split('/')[-1].split('.')[0]+".txt"
        gt_fileName_other1 = "/media/yaesop/ARL_FZNV/DTRA/DTRA_gt/"+position_other1+"/" +fileName.split('/')[-1].split('.')[0]+".txt"
        gt_fileName_other2 = "/media/yaesop/ARL_FZNV/DTRA/DTRA_gt/"+position_other2+"/" +fileName.split('/')[-1].split('.')[0]+".txt"
        with open(gt_fileName) as ff:
            for line in ff:
                gt = line.split(" ")
        with open(gt_fileName_other1) as ff1:
            for line in ff1:
                gt_other1 = line.split(" ")

        with open(gt_fileName_other2) as ff2:
            for line in ff2:
                gt_other2 = line.split(" ")
            
        for fLine in f: 
            min_x = float(fLine.split(" ")[1])*640-float(fLine.split(" ")[3])*640/2
            min_y = float(fLine.split(" ")[2])*640-float(fLine.split(" ")[4])*640/2
            max_x = float(fLine.split(" ")[1])*640+float(fLine.split(" ")[3])*640/2
            max_y = float(fLine.split(" ")[2])*640+float(fLine.split(" ")[4])*640/2
            #print(",om:",min_x, max_x, min_y, max_y)
            #print(float(gt_other1[1]), float(gt_other1[2]), float(gt_other1[1])+float(gt_other1[3]), float(gt_other1[2])+float(gt_other1[4]))
            if gt_other1 =="" or (float(gt_other1[1]) > max_x or min_x > float(gt_other1[1])+ float(gt_other1[3])) or (float(gt_other1[2]) > max_y or min_y > float(gt_other1[2])+ float(gt_other1[4])):
                overlapped1 = False
            else:
                overlapped1 = True

            if gt_other2 =="" or (float(gt_other2[1]) > max_x or min_x > float(gt_other2[1])+ float(gt_other2[3])) or (float(gt_other2[2]) > max_y or min_y > float(gt_other2[2])+ float(gt_other2[4])):
                overlapped2 = False
            else:
                overlapped2 = True
            #print(overlapped1, overlapped2)

            if fLine.startswith("0")  and not overlapped1 and  not overlapped2 and gt is not "" and abs(float(gt[1])+float(gt[3])/2-float(fLine.split(" ")[1])*640)<50 and abs(float(gt[2])+float(gt[4])/2-float(fLine.split(" ")[2])*640)<50:
                #print("here")
                #print(abs(float(gt[1])-float(fLine.split(" ")[1])*640-float(fLine.split(" ")[3])*640/2))   
                #print(fLine)   
                tmp+="person"   
                tmp+=" "
                tmp+= str(float(fLine.split(" ")[5]))
                tmp+=" "
                tmp+= str(float(fLine.split(" ")[1])*640-float(fLine.split(" ")[3])*640/2)
                tmp+=" "
                tmp+= str(float(fLine.split(" ")[2])*640-float(fLine.split(" ")[4])*640/2)
                tmp+=" "
                tmp+= str(float(fLine.split(" ")[3])*640)
                tmp+=" "
                tmp+= str(float(fLine.split(" ")[4])*640)
                tmp+='\n'

        file1 = open('../Object-Detection-Metrics/detections/'+fileName.split('/')[-1],"x")
        #print(tmp)
        #print("next")
        file1.write(tmp)
        tmp = ""
        file1.close() #to change file access modes
