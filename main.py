import torch
import cv2
import numpy as np
from PIL import Image

# Cargar el modelo personalizado
model_path_TUMOR = 'C:/Users/dorad/OneDrive/Documents/TESIS/MODELOS/modeloyolov5-full.pt'
model_TUMOR = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path_TUMOR)

model_path_CEREBRO = 'C:/Users/dorad/OneDrive/Documents/TESIS/MODELOS/BRAIN_yoloV5.pt'
model_CEREBRO = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path_CEREBRO)

# Establecer el modelo en modo evaluación
model_TUMOR.eval()

model_CEREBRO.eval()

# Cargar y preprocesar la imagen
image_path = 'C:/Users/dorad/OneDrive/Documents/TESIS/train_data/images/train/m1(14).jpg'
image = Image.open(image_path)


# Configurar la confianza mínima de detección
conf_threshold_TUMOR = 0.74

conf_threshold_CEREBRO = 0.5


# Ejecutar la detección en la imagen
results_TUMOR = model_TUMOR(image)

results_CEREBRO = model_CEREBRO(image)

# Obtener las predicciones de detección
predictions_TUMOR = results_TUMOR.pandas().xyxy[0]

predictions_CEREBRO = results_CEREBRO.pandas().xyxy[0]

# Filtrar las predicciones por confianza mínima
filtered_predictions_TUMOR = predictions_TUMOR[predictions_TUMOR['confidence'] >= conf_threshold_TUMOR]

filtered_predictions_CEREBRO = predictions_CEREBRO[predictions_CEREBRO['confidence'] >= conf_threshold_CEREBRO]

# Mostrar las predicciones
print(filtered_predictions_TUMOR)
print(filtered_predictions_CEREBRO)


# Obtener la imagen como un array numpy
image_array_TUMOR = np.array(image)

image_array_CEREBRO = image_array_TUMOR

# Acumulador de areas, en caso de tener multiples tumores
Area_tumor = 0.0
Area_CEREBRO = 0.0
# Dibujar los cuadros delimitadores en la imagen con etiqueta, porcentaje de certeza y marcación
for _, row in filtered_predictions_TUMOR.iterrows():
    x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

    #Aqui se calcula el area
    Area = (x2 - x1)*(y2-y1)
    Area_tumor = Area_tumor + Area

    confidence = row['confidence']
    label = row['name']
    text = f"{label}: {confidence:.2f}"
    color = (255, 0, 255)  # Color rojo (BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    cv2.rectangle(image_array_TUMOR, (x1, y1), (x2, y2), color, 2)
    cv2.rectangle(image_array_TUMOR, (x1, y1), (x1 + text_size[0], y1 - text_size[1] - 5), color, -1)
    cv2.putText(image_array_TUMOR, text, (x1, y1 - 5), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)


# Convertir la imagen de nuevo a formato PIL
marked_image_TUMOR = Image.fromarray(image_array_TUMOR)

# Guardar la imagen marcada
str_img_name = image_path.rsplit('/', 1)[-1]        #En esta linea se obtiene el nombre de la imagen para su guardado igual
marked_image_path_TUMOR = 'C:/Users/dorad/OneDrive/Documents/TESIS/RESULTADOS-MARCACION/' + str_img_name
marked_image_TUMOR.save(marked_image_path_TUMOR)

for _, row in filtered_predictions_CEREBRO.iterrows():
    x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

    Area_CEREBRO = (x2 - x1) * (y2 - y1)

#    confidence = row['confidence']
    #    label = row['name']
    #text = f"{label}: {confidence:.2f}"
    #color = (0, 0, 255)  # Color rojo (BGR)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #font_scale = 1
    #thickness = 2
    #text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    #cv2.rectangle(image_array_CEREBRO, (x1, y1), (x2, y2), color, 2)
    #cv2.rectangle(image_array_CEREBRO, (x1, y1), (x1 + text_size[0], y1 - text_size[1] - 5), color, -1)
    #cv2.putText(image_array_CEREBRO, text, (x1, y1 - 5), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

# Poner en pantalla el area
print("\n\nArea TUMOR: ", Area_tumor)
print("Area CEREBRO: ",Area_CEREBRO )

# Area de Cerebro --100%
# Area de Tumor ----x
print("\nEl porcentaje del cerebro que se dectó como tumor es: ", round((Area_tumor *100 / Area_CEREBRO),2), " %")


# Convertir la imagen de nuevo a formato PIL
#marked_image_TUMOR = Image.fromarray(image_array_TUMOR)
marked_image_CEREBRO = Image.fromarray(image_array_CEREBRO)


# Guardar la imagen marcada
#marked_image_path_TUMOR = 'C:/Users/dorad/OneDrive/Documents/TESIS/RESULTADOS-MARCACION/m1(196)_marcadav5.jpg'
#marked_image_TUMOR.save(marked_image_path_TUMOR)

#marked_image_path_CEREBRO = 'C:/Users/dorad/OneDrive/Documents/TESIS/RESULTADOS-MARCACION-CEREBRO/m1(196)_CEREBRO.jpg'
#marked_image_CEREBRO.save(marked_image_path_CEREBRO)
