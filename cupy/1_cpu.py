import numpy as np
import time
import scipy.fft
from numba import njit

tic_c = time.process_time()

# # L2 Normalisation
x_cpu = np.array([1, 2, 3])
# l2_cpu = np.linalg.norm(x_cpu)
a = np.random.random(100).astype(np.complex128)


# @njit(parallel=True)
def calc(num):
    for i in range(100000):
        b = np.fft.fft(a) * (i+1)
    # l2_cpu = np.linalg.norm(num)
    # print("value:", b)
    return b


res = calc(a)
# print(res)

toc_c = time.process_time()

print("elapsed time cpu:", toc_c - tic_c)
