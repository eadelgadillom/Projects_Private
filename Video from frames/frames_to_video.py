import cv2
from astropy.io import fits
from glob import glob
import os
import numpy as np

# Ruta de la carpeta con los archivos FITS
folder_fits = (
    r"C:\Users\eduar\OneDrive\Escritorio\SharpCap Captures\2024-08-20\Moon1\20_58_53"
)

# Ruta de la carpeta de salida para el video
output_folder = r"C:\Users\eduar\OneDrive\Escritorio\SharpCap Captures\2024-08-20\Moon1\20_58_53\Output"

# Asegurarse de que la carpeta de salida existe
os.makedirs(output_folder, exist_ok=True)

# Nombre del archivo de salida
output_filename = "Moon_3.mp4"

# Ruta completa del archivo de video de salida
output_path = os.path.join(output_folder, output_filename)

# Obtener la lista de archivos FITS en la carpeta
fits_files = glob(os.path.join(folder_fits, "*.fits"))

# Variables para el video
video = None
height, width = None, None

# Iterar sobre cada archivo FITS
for fits_file in fits_files:
    # Abrir el archivo FITS
    hdul = fits.open(fits_file)

    # Obtener los datos de la imagen FITS
    fits_data = hdul[0].data.T

    # Escalar los valores de píxeles a 0-255
    fits_data = (
        (fits_data - np.min(fits_data)) / (np.max(fits_data) - np.min(fits_data)) * 255
    )

    # Convertir la imagen FITS a formato de imagen OpenCV (uint8)
    fits_data_uint8 = np.uint8(fits_data)

    # Obtener las dimensiones de la imagen
    height, width = fits_data_uint8.shape

    # Inicializar el video una vez que se obtengan las dimensiones
    if video is None:
        video = cv2.VideoWriter(
            output_path, cv2.VideoWriter_fourcc(*"DIVX"), 4, (width, height)
        )

    # Añadir la imagen al video
    video.write(cv2.cvtColor(fits_data_uint8, cv2.COLOR_GRAY2BGR))

# Liberar el objeto VideoWriter
if video is not None:
    video.release()

print(f"Video guardado en: {output_path}")
