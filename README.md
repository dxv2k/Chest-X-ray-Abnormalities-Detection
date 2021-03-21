# Chest-X-ray-Abnormalities-Detection
VinBigData Chest X-ray Abnormalities Detection 
(Dataset)[https://www.mediafire.com/file/xwiio9bezjfc1l2/yolo_data.zip/file]: 
- Already convert to YOLO format
- Dataset folder structure similar to YOLOv5  

# Usage: 
## Train args:
- python train.py --img 640 --batch 4 --epochs 5 --data ../dataset.yaml --weights yolov5x.pt --workers 0   

# Note: 
- workers should set to 0 (I'm using RTX 2070) 
