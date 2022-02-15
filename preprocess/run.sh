#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/standing
#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/kneeling
#rm -rf /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/lying
#cd /media/yaesop/ARL_FZNV/DTRA/DTRA_gt/
#mkdir standing
#mkdir kneeling
#mkdir lying
cd ~/RealDataExp/preprocess
for vid in DTRA_Trial-1_CIR_VIS_15m_45deg_cam DTRA_Trial-2_CIR_VIS_20-25m_45deg_cam DTRA_Trial-3_CIR_VIS_15-20m_45deg_cam  DTRA_Trial-4_CIR_VIS_15-20m_45deg_cam DTRA_Trial-5_CIR_VIS_25-30m_45deg_cam DTRA_Trial-6_CIR_VIS_30-35m_45deg_cam DTRA_Trial-7_CIR_VIS_40-45m_45deg_cam DTRA_Trial-8_CIR_VIS_40-45m_45deg_cam DTRA_Trial-9_CIR_VIS_50m_45deg_cam  DTRA_Trial-10_CIR_VIS_15m_45deg_cam DTRA_Trial-11_CIR_VIS_20-25m_45deg_cam ; do  
    #python vid2frame.py --pathIn /media/yaesop/ARL_FZNV/DTRA/ --pathOut /media/yaesop/ARL_FZNV/DTRA/ --vidName ${vid}
    python annotations.py --pathIn /media/yaesop/ARL_FZNV/DTRA/ --pathOut /media/yaesop/ARL_FZNV/DTRA/ --vidName ${vid}
done 



