import os
import SimpleITK as sitk

def convert_png_to_dicom(png_folder, dicom_folder):
    # PNG klasöründeki tüm dosyaları listele
    png_files = [f for f in os.listdir(png_folder) if f.endswith('.png')]

    for png_file in png_files:
        png_path = os.path.join(png_folder, png_file)
        dicom_path = os.path.join(dicom_folder, png_file.replace('.png', '.dcm'))

        # PNG dosyasını oku
        image_png = sitk.ReadImage(png_path, sitk.sitkUInt16)

        # DICOM olarak kaydet
        writer = sitk.ImageFileWriter()
        writer.SetFileName(dicom_path)
        writer.Execute(image_png)
        print(f'Converted {png_file} to DICOM and saved as {dicom_path}')

# PNG ve DICOM dosyalarının dizinlerini tanımla
png_folder = "input_path"
dicom_folder = "output_path"

# Dönüşüm fonksiyonunu çağır
convert_png_to_dicom(png_folder, dicom_folder)
