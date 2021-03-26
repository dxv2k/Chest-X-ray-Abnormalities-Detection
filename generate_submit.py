import numpy as np 
from glob import glob
import pandas as pd
import shutil, os
from tqdm.notebook import tqdm # progress bar

result_path = "run/exp/labels" 
test_df = pd.read_csv("./run/test.csv")
print(test_df.shape)

# YOLO cls  x   y   w   h   conf
# VOC  cls  conf    x1  y1  x2  y2 


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

# # for file_path in tqdm(glob('runs/detect/exp/labels/*txt')):
# for file_path in tqdm(glob(result_path + '/*txt')):
#     image_id = file_path.split('/')[-1].split('.')[0]
#     w, h = test_df.loc[test_df.image_id==image_id,['width', 'height']].values[0]
#     f = open(file_path, 'r')
#     data = np.array(f.read().replace('\n', ' ').strip().split(' ')).astype(np.float32).reshape(-1, 6)
#     data = data[:, [0, 5, 1, 2, 3, 4]]
#     bboxes = list(np.round(np.concatenate((data[:, :2], np.round(yolo2voc(h, w, data[:, 2:]))), axis =1).reshape(-1), 1).astype(str))
#     for idx in range(len(bboxes)):
#         bboxes[idx] = str(int(float(bboxes[idx]))) if idx%6!=1 else bboxes[idx]
#     image_ids.append(image_id)
#     PredictionStrings.append(' '.join(bboxes))

# YOLO cls  x   y   w   h   conf
# VOC  cls  conf    x1  y1  x2  y2 
cnt = 0 
curr_dir = "run/exp/labels"
for file_path in tqdm(os.listdir(curr_dir)): 
    cnt += 1 
    if cnt == 20: 
        break 
    if file_path.endswith(".txt"): 
        image_id = file_path.replace('.txt','') 
        print(image_id)
    # w, h = test_df.loc[test_df.image_id==image_id,['width', 'height']].values[0]
    # w, h = test_df.loc[test_df.image_id==image_id,[test_df.width, test_df.height]].values[1]
    # print(w,h)
    # if test_df.image_id == image_id:  
    #     w,h = test_df.width, test_df.height

    # LOGIC ERROR here
    # TODO: need to get specific width, height from given image_id
    # if image_id in test_df.image_id.values: 
    #     w,h = test_df.width, test_df.height
    #     print(w,h)
    w, h = test_df.loc[image_id,['width', 'height']].values[0]

    f = open(curr_dir + '/' + file_path, 'r')
    data = np.array(f.read().replace('\n', ' ').strip().split(' ')).astype(np.float32).reshape(-1, 6)
    # print("YOLO bbox ", data)

    data = data[:, [0, 5, 1, 2, 3, 4]] # convert to VOC format 
    # print("VOC format ", data)
#    bboxes = list(np.round(np.concatenate((data[:, :2], np.round(yolo2voc(h, w, data[:, 2:]))), axis =1).reshape(-1), 1).astype(str))
#     for idx in range(len(bboxes)):
#         bboxes[idx] = str(int(float(bboxes[idx]))) if idx%6!=1 else bboxes[idx]
#     image_ids.append(image_id)
#     PredictionStrings.append(' '.join(bboxes))

# print(image_ids, PredictionStrings)




# fill not exists img with 14 1 0 0 1 1 