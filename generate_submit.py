import numpy as np 
from glob import glob
import pandas as pd
import shutil, os
from tqdm.notebook import tqdm # progress bar

result_path = "run/exp/labels" 
# local_detect_path = r"I:\github\Chest-X-ray-Abnormalities-Detection\yolov5\runs\detect\exp\labels"
local_detect_path = r"C:\Users\KnightV\Documents\github\Chest-X-ray-Abnormalities-Detection\yolov5\runs\detect\exp\labels"
test_df = pd.read_csv("./run/test.csv")


# function get from kaggle
def yolo2voc(image_height, image_width, bboxes):
    """
    yolo => [xmid, ymid, w, h] (normalized)
    voc  => [x1, y1, x2, y1]
    
    """ 
    bboxes = bboxes.copy().astype(float) # otherwise all value will be 0 as voc_pascal dtype is np.int
    
    bboxes[..., [0, 2]] = bboxes[..., [0, 2]]* image_width
    bboxes[..., [1, 3]] = bboxes[..., [1, 3]]* image_height
    
    bboxes[..., [0, 1]] = bboxes[..., [0, 1]] - bboxes[..., [2, 3]]/2
    bboxes[..., [2, 3]] = bboxes[..., [0, 1]] + bboxes[..., [2, 3]]
    
    return bboxes

image_ids = []
PredictionStrings = []


# YOLO cls  x   y   w   h   conf
# VOC  cls  conf    x1  y1  x2  y2 
# local_detect_path = r"I:\github\Chest-X-ray-Abnormalities-Detection\yolov5\runs\detect\exp\labels"
local_detect_path = r"C:\Users\KnightV\Documents\github\Chest-X-ray-Abnormalities-Detection\yolov5\runs\detect\exp\labels"
# curr_dir = "run/exp/labels"
# for file_path in tqdm(os.listdir(curr_dir)): 
# for file_path in tqdm(os.listdir(local_detect_path)): 
for file_path in os.listdir(local_detect_path): 
    if file_path.endswith(".txt"): 
        image_id = file_path.replace('.txt','') 
        # print(image_id)

    w, h = test_df.loc[test_df.image_id == image_id,['width', 'height']].values[0]
    # print(w,h)

    # f = open(curr_dir + '/' + file_path, 'r')
    f = open(local_detect_path + '/' + file_path, 'r')
    data = np.array(f.read().replace('\n', ' ').strip().split(' ')).astype(np.float32).reshape(-1, 6)
    # print("YOLO bbox ", data)

    data = data[:, [0, 5, 1, 2, 3, 4]] # convert to VOC format 
    # print("VOC format ", data)
    bboxes = list(np.round(np.concatenate((data[:, :2], np.round(yolo2voc(h, w, data[:, 2:]))), axis =1).reshape(-1), 1).astype(str))
    for idx in range(len(bboxes)):
        bboxes[idx] = str(int(float(bboxes[idx]))) if idx%6!=1 else bboxes[idx]
    image_ids.append(image_id)
    PredictionStrings.append(' '.join(bboxes))

# print(image_ids, PredictionStrings)

pred_df = pd.DataFrame({'image_id':image_ids,
                        'PredictionString':PredictionStrings})

# fill not exists img with 14 1 0 0 1 1 
sub_df = pd.merge(test_df, pred_df, on = 'image_id', how = 'left').fillna("14 1 0 0 1 1")
sub_df = sub_df[['image_id', 'PredictionString']]
sub_df.to_csv('./submission.csv',index = False)
sub_df.tail()
