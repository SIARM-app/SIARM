import torch
import cv2
import numpy as np
from PIL import Image

# Cargar el modelo personalizado
model_path = 'C:/Users/dorad/OneDrive/Documents/TESIS/MODELOS/modeloyolov5-full.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# Establecer el modelo en modo evaluación
model.eval()

# Cargar y preprocesar la imagen
image_path = 'C:/Users/dorad/OneDrive/Documents/TESIS/train_data/images/train/m1(195).jpg'
image = Image.open(image_path)

# Configurar la confianza mínima de detección
conf_threshold = 0.8

# Ejecutar la detección en la imagen
results = model(image)

# Obtener las predicciones de detección
predictions = results.pandas().xyxy[0]

# Filtrar las predicciones por confianza mínima
filtered_predictions = predictions[predictions['confidence'] >= conf_threshold]

# Mostrar las predicciones
print(filtered_predictions)

# Obtener la imagen como un array numpy
image_array = np.array(image)

# Dibujar los cuadros delimitadores en la imagen con etiqueta, porcentaje de certeza y marcación
for _, row in filtered_predictions.iterrows():
    x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
    confidence = row['confidence']
    label = row['name']
    text = f"{label}: {confidence:.2f}"
    color = (255, 0, 255)  # Color rojo (BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    cv2.rectangle(image_array, (x1, y1), (x2, y2), color, 2)
    cv2.rectangle(image_array, (x1, y1), (x1 + text_size[0], y1 - text_size[1] - 5), color, -1)
    cv2.putText(image_array, text, (x1, y1 - 5), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

# Convertir la imagen de nuevo a formato PIL
marked_image = Image.fromarray(image_array)

# Guardar la imagen marcada
marked_image_path = 'C:/Users/dorad/OneDrive/Documents/TESIS/RESULTADOS-MARCACION/m1(195)_marcadav5.jpg'
marked_image.save(marked_image_path)
