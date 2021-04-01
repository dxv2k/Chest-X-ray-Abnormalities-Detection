# Chest-X-ray-Abnormalities-Detection
VinBigData Chest X-ray Abnormalities Detection 
(Dataset)[https://www.mediafire.com/file/xwiio9bezjfc1l2/yolo_data.zip/file]: 
- Already convert to YOLO format
- Dataset folder structure similar to YOLOv5  

# Usage: 
## Train args:
'''
python train.py --img 640 --batch 4 --epochs 5 --data ../dataset.yaml --weights yolov5x.pt --workers 0   
'''

'''
python train.py --img 640 --batch 8 --epochs 30 --data ../dataset.yaml --weights runs/train/exp9/weights/last.pt --workers 0 
'''

## Detect args: 
'''
python detect.py --weight runs/train/exp19/weights/last.pt --img 640 --conf 0.25 --iou 0.4 --source H:\test_set_chest_xray\test --save-txt --save-conf --exist-ok
'''
# Note: 
- workers should set to 0 (I'm using RTX 2070) 


# RESULT: 
- exp15 - 0.064 
- exp17 - 0.116
- exp19 - 0.084 