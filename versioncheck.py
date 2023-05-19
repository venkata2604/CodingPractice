import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf
import cv2
import numpy


print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
print(f"opencv {cv2.__version__}")
print(f"numpy {numpy.__version__}")
print("GPU is", "available" if tf.test.is_gpu_available() else "NOT AVAILABLE")
print(f"Tensor Flow devices: {tf.config.list_physical_devices('GPU')}")
