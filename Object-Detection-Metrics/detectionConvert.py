import sys
import glob

altitude = sys.argv[1]
radius = sys.argv[2]
model = sys.argv[3]
position = sys.argv[4]
selected = []
data4al = []
if altitude == "15":
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
    dataset = glob.glob("/media/yaesop/ARL_FZNV/real_result/detect_"+model+"/exp/labels/*.txt")
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
for fileName in selected:
    with open(fileName) as f:
        for fLine in f: 
            #print(fLine)   
            if fLine.startswith("0"):
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
