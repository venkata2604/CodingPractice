import cupy as cp
import time

import cupy.fft
import cupyx.scipy.fft as cufft
import scipy.fft


tic_g = time.process_time()

# # L2 Normalisation
# x_gpu = cp.array([1, 2, 3])
# l2_gpu = cp.linalg.norm(x_gpu)
#
# print(x_gpu.device)

a = cp.random.random(100).astype(cp.complex128)
print(a.device)
for i in range(100000):
    # b = cupy.fft.fft(a)
    with scipy.fft.set_backend(cufft):
        b = scipy.fft.fft(a)


# print(b)

toc_g = time.process_time()

print("elapsed time gpu:", toc_g-tic_g)
