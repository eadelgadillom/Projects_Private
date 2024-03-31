from PIL import Image
import numpy as np
import cv2
import os
from glob import glob

# Ruta de la carpeta con los archivos TIFF
folder_tif = r"D:\Tesis maestria\Luna\GIS\Hillshades"

# Obtener la lista de archivos TIFF en la carpeta
tif_files = glob(os.path.join(folder_tif, "*.tif"))

# Variables para el video
video = None
height, width = None, None

# Iterar sobre cada archivo TIFF
for tif_file in tif_files:
    # Abrir el archivo TIFF
    img = Image.open(tif_file)

    # Convertir la imagen PIL a formato de imagen OpenCV (BGR)
    img_cv2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Obtener las dimensiones de la imagen
    height, width, _ = img_cv2.shape

    # Inicializar el video una vez que se obtengan las dimensiones
    if video is None:
        video = cv2.VideoWriter(
            "output_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10, (width, height)
        )

    # Añadir la imagen al video
    video.write(img_cv2)

# Liberar el objeto VideoWriter
if video is not None:
    video.release()
