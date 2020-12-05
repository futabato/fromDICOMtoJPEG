import numpy as np
import matplotlib.pyplot as plt 
from pydicom import *

d = dcmread('./Nodule154images/JPCLN001.dcm')

arr = d.pixel_array
plt.imshow(arr, cmap="gray")
plt.show()