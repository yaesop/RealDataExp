#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/standing
#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/kneeling
#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/lying
#cd /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/
#mkdir standing
#mkdir kneeling
#mkdir lying
cd ~/RealDataExp/preprocess
for vid in DTRA_Trial-10_CIR_VIS_15m_45deg_cam DTRA_Trial-11_CIR_VIS_20-25m_45deg_cam ; do  
    #python vid2frame.py --pathIn /media/yaesop/ARL_FZNV/DTRA/ --pathOut /media/yaesop/ARL_FZNV/DTRA/ --vidName ${vid}
    #python annotations.py --pathIn /media/yaesop/ARL_FZNV/DTRA/ --pathOut /media/yaesop/ARL_FZNV/DTRA/ --vidName ${vid}
    python training_anno.py --pathIn /media/yaesop/ARL_FZNV/DTRA/ --pathOut /media/yaesop/ARL_FZNV/DTRA/ --vidName ${vid}
done 



