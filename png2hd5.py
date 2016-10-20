#!/usr/bin/env
import cv2
import h5py
import numpy as np

out = np.zeros((2,520,520), dtype=np.uint8)
out[0,:,:] = cv2.imread('png.png',0)
with h5py.File('h5.h5', 'w') as hf:
    hf.create_dataset('main', data=out)