import numpy as np

test_npy_path = '/home/chuanzhi/mnt_2T/wz/datasets/shrimp/forDM/train/IMG_000011.npy'
# test_npy_path = '/home/chuanzhi/mnt_2T/wz/datasets/shrimp/forDM/train/IMG_000012.npy'

np_array = np.load(test_npy_path)
print(np_array)