import cv2
import numpy as np

imagen = cv2.imread('D:\Cosas Ariel\Fotos Berjovina\IMG-20230417-WA0000.jpg')


imagen_filtrada = cv2.GaussianBlur(imagen,(5,5),0)


bordes = cv2.Canny(imagen_filtrada,100,200)


imagen_binarizada = cv2.theshold(imagen_filtrada,128,255,cv2.THRESH_BINARY)

cv2.imshow('Imagen Original',imagen)
cv2.imshow('Imagen Filtrada',imagen_filtrada)
cv2.imshow('Deteccion de Borde',bordes)
cv2.imshow('Imagen Binarizada',binarizada)

cv2.waitkey(0)
cv2.destroyAllWindows()