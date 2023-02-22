# ref: https://rinovation.tistory.com/160

from itertools import groupby
import numpy as np

def get_process_order(data):
    i = 1
    rlt = np.array([],dtype='int')
    for _, g in groupby(data):
        tmp = np.array([i for _ in range(len(list(g)))],dtype='int')
        rlt = np.concatenate([rlt, tmp],axis=0)
        i +=1
    return rlt
