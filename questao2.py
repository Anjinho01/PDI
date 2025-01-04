import numpy as np
import cv2

mascara1 = np.array([[  0, 1/5,   0],
                     [1/5, 1/5, 1/5],
                     [  0, 1/5,   0]])
mascara2 = np.array([[1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9]])
mascara3 = np.array([[1/32, 3/32, 1/32],
                     [3/32, 16/32, 3/32],
                     [1/32, 3/32, 1/32]])
mascara4 = np.array([[  0, 1/8,   0],
                     [1/8, 4/8, 1/8],
                     [  0, 1/8,   0]])

imagem = cv2.imread("lena_ruido.bmp")


cv2.imshow("original", imagem)
cv2.imshow("mascara 1", cv2.filter2D(imagem, -1, mascara1))
cv2.imshow("mascara 2", cv2.filter2D(imagem, -1, mascara2))
cv2.imshow("mascara 3", cv2.filter2D(imagem, -1, mascara3))
cv2.imshow("mascara 4", cv2.filter2D(imagem, -1, mascara4))
cv2.imshow("mediana", cv2.medianBlur(imagem, 3))

cv2.imwrite("mascara1.bmp", cv2.filter2D(imagem, -1, mascara1))
cv2.imwrite("mascara2.bmp", cv2.filter2D(imagem, -1, mascara2))
cv2.imwrite("mascara3.bmp", cv2.filter2D(imagem, -1, mascara3))
cv2.imwrite("mascara4.bmp", cv2.filter2D(imagem, -1, mascara4))
cv2.imwrite("mediana.bmp", cv2.medianBlur(imagem, 3))
