from pydicom import *
import cv2
import os

# 適切にパスを設定してください。
input_dir = './Nodule154images/'
output_dir = './jpg_images/'


def main(input_dir, output_dir):
    list_of_files = os.listdir(input_dir)
    for dicom_file in list_of_files:
        d = dcmread(os.path.join(input_dir, dicom_file))
        
        window = d.WindowWidth
        level = d.WindowCenter
        arr = d.pixel_array

        """
        JPCLN001.dcmの場合、
        level + window/2 => 4094.5
        level - window/2 => -0.5
        4094.05 + abs(-0.5) = 4095(= 2**12 -1)なので、1画素当たり12bit使われていることがわかる。
        """
        max_pixelvalue = level + window/2
        min_pixelvalue = level - window/2
        
        # 画素値を0~255(8bit)に収まるように変換する。
        arr = 255*(arr - min_pixelvalue)/(max_pixelvalue - min_pixelvalue)
        
        arr[arr > 255] = 255
        arr[arr < 0] = 0
        
        cv2.imwrite(os.path.join(output_dir, dicom_file.replace("dcm", "jpg")), arr)


if __name__ == '__main__':
    main(input_dir, output_dir)