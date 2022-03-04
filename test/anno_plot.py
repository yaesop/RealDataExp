import cv2
path = '/media/yaesop/ARL_FZNV/DTRA/DTRA_png_new/DTRA_Trial-10_CIR_VIS_15m_45deg_cam_10sec_5942_1.png'

myimg = cv2.imread(path)
with open('/media/yaesop/ARL_FZNV/DTRA/DTRA_gt/lying/DTRA_Trial-10_CIR_VIS_15m_45deg_cam_10sec_5942_1.txt') as f:
    for line in f:
        bbox= line.split(" ")
        #print(bbox)
        minx = float(bbox[1])
        maxx = float(bbox[1]) + float(bbox[3])
        miny = float(bbox[2])
        maxy = float(bbox[2]) + float(bbox[4])
        print(minx, maxx, miny, maxy)
        pts1 = int(minx), int(miny)
        pts2 = int(maxx), int(maxy)
        cv2.rectangle( myimg, pts1,pts2, (255, 0, 0), 2)
#cv2.imwrite("./test_gt.png",myimg)

"""with open('/home/yaesop/real_result/detect_s/exp/labels/DTRA_Trial-10_CIR_VIS_15m_45deg_cam_10sec_8941_5.txt') as f:
    for line in f:
        bbox= line.split(" ")
        #print(bbox)
        minx = 640*(float(bbox[1])- float(bbox[3])/2)
        maxx = 640*(float(bbox[1])+ float(bbox[3])/2)
        miny = 640*(float(bbox[2])- float(bbox[4])/2)
        maxy = 640*(float(bbox[2])+ float(bbox[4])/2)
        print(minx, maxx, miny, maxy)
        pts1 = int(minx), int(miny)
        pts2 = int(maxx), int(maxy)
        cv2.rectangle( myimg, pts1,pts2, (0, 255, 0), 2)"""
cv2.imwrite("./test_gt_detected_1.png",myimg)
#cv2.rectangle(myimg, (250, 150), (250+10, 250+20), (0, 255, 0))
#
#cv2.imshow("myimg",myimg)

#myimg = cv2.imread(path)


