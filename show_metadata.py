from pydicom import *

d = dcmread('./Nodule154images/JPCLN001.dcm')
print(d.file_meta)