import pyautogui
import cv2
import numpy as np
 
# especificar la resolucion
resolution = (1920, 1080)
 
# especificar el codec
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# el nombre del archivo
filename = "Recording.avi"
 
# elframerate 
fps = 60.0
 
 
# creando el objeto
out = cv2.VideoWriter(filename, codec, fps, resolution)
 
# creando una ventana vacia
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
 
# cambiando el tamaño de la ventana
cv2.resizeWindow("Live", 480, 270)
 
while True:
    # tomando un screenshot usando PyAutoGUI
    img = pyautogui.screenshot()
 
    # convierte el screooshot en un array con numpy
    frame = np.array(img)
 
    # conversion de RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # escribiendo al archivo de salida
    out.write(frame)
     
    # para que aparezca la grabacion en pantalla
    cv2.imshow('Live', frame)
     
    # detener la grabacion con q
    if cv2.waitKey(1) == ord('q'):
        break
 
# Release 
out.release()
 
# cerrar
cv2.destroyAllWindows()