import cv2

# cargar cascada
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# leer imagen
img = cv2.imread('news.jpg')

# convertir a escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# detectar caras
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.105, minNeighbors=5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey()   
cv2.destroyAllWindows()
