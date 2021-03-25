from glob import glob
import os
from pathlib import Path    
import pandas as pd

# for file_path in glob("run/exp/labels/*.txt"): 
#     # image_id = file_path.split('/')[-1].split('.')[0]
#     image_id = file_path.split('/')
#     iamge_id = file_path.split('labels\\')
#     print(image_id)

# path = "run\exp\labels\00a2145de1886cb9eb88869c85d74080.txt"
path = "run\exp\labels\0a8dc3de200bc767169b73a6ab91e948.txt"

# _, tail = os.path.split("run\exp\labels\00a2145de1886cb9eb88869c85d74080.txt")
# print(tail)
# print(Path(path).name) 

curr_dir = "run\exp\labels"

# os.listdir

# for name in os.listdir(curr_dir): 
#     if name.endswith(".txt"): 
#        print(name) 

test_df = pd.read_csv("./run/test.csv")
curr_dir = "run/exp/labels"
# for file_path in os.listdir(curr_dir): 
#     if file_path.endswith(".txt"): 
#         image_id =  file_path 
#     # print(image_id)
#     w, h = test_df.loc[test_df.image_id==image_id,['width', 'height']].values[0]
#     print(w,h)


print(test_df.width) 
# print(test_df.image_id, test_df.width) 