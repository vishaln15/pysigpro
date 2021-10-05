import numpy as np

def hMob(x):
    row = np.array(x)
    return (np.sqrt(np.var(np.gradient(x)) / np.var(x)))