import SimpleITK as sitk
import numpy as np
import os

def read_image_dicom(file_path):
    image = sitk.ReadImage(file_path)
    array = sitk.GetArrayFromImage(image)
    return array

def save_image_dicom(image_array, output_file_path):
    image = sitk.GetImageFromArray(image_array)
    sitk.WriteImage(image, output_file_path)

def crop_single_dicom(input_file_path, output_file_path, crop_buffer=50):
    image_array = read_image_dicom(input_file_path)
    
    # Görüntünün en büyük maskesini al (örneğin sadece 0 olmayan pikseller)
    mask = image_array > 0
    coords = np.argwhere(mask)
    
    # Maske içindeki alanı bul
    z_min, y_min, x_min = coords.min(axis=0)
    z_max, y_max, x_max = coords.max(axis=0)
    
    # Crop yapılacak alanı belirle
    y_min = max(0, y_min - crop_buffer)
    y_max = min(image_array.shape[1], y_max + crop_buffer)
    x_min = max(0, x_min - crop_buffer)
    x_max = min(image_array.shape[2], x_max + crop_buffer)
    
    # Kırpılmış görüntüyü oluştur
    cropped_image = image_array[:, y_min:y_max, x_min:x_max]  # Z ekseni boyunca kırpmıyoruz
    
    # Kırpılmış görüntüyü DICOM formatında kaydet
    save_image_dicom(cropped_image, output_file_path)
    
    print(f"Kırpılmış dosya kaydedildi: {output_file_path}")

# Dosya yolları
input_file = '/home/saidakca/workspace/GLAM/sample_data/images/0_L-CC.dcm'
output_file = '/home/saidakca/workspace/GLAM/sample_data/cropped_images/0_L-CC_cropped.dcm'

crop_single_dicom(input_file, output_file)
