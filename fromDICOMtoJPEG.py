from pydicom import dicom
import cv2
import os

# 適切にパスを設定してください。
input_dir = './Nodule154images/'
output_dir = './jpg_images/'

def main(input_dir, output_dir):
    images_path = os.listdir(input_dir)
    for _, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(images_path, image))
        pixel_array_numpy = ds.pixel_array
        image = image.replace('.dcm', '.jpg')
        cv2.imwrite(os.path.join(output_dir, image), pixel_array_numpy)

if __name__ == '__main__':
    main(input_dir, output_dir)