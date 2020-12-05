from pydicom import *

d = dcmread('./Nodule154images/JPCLN001.dcm')
print(d[0x0028, 0x0101])