import numpy as np
import cv2

A = 2
W = 9*A - 1
laplaciano = np.array([[0,  1,  0], 
                       [1, -4,  1], 
                       [0,  1,  0]])
blur_enfraquecido = np.array([[1/125,1/125,1/125,1/125,1/125],
                              [1/125,1/125,1/125,1/125,1/125],
                              [1/125,1/125,1/125,1/125,1/125],
                              [1/125,1/125,1/125,1/125,1/125],
                              [1/125,1/125,1/125,1/125,1/125]])
high_boost = np.array([[-1/9, -1/9, -1/9], 
                       [-1/9,  W/9, -1/9],
                       [-1/9, -1/9, -1/9]])
prewitt_horizontal = np.array([[-1, 0, 1],
                               [-1, 0, 1],
                               [-1, 0, 1]])
prewitt_vertical = np.array([[-1,-1,-1],
                             [ 0, 0, 0],
                             [ 1, 1, 1]])
sobel_horizontal = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
sobel_vertical = np.array([[-1,-2,-1],
                             [ 0, 0, 0],
                             [ 1, 2, 1]])


imagem = cv2.imread("lena_gray.bmp")

resultado_laplaciano = cv2.filter2D(imagem, -1, laplaciano)
resultado_blur = cv2.filter2D(imagem, -1, blur_enfraquecido)
resultado_high_boost = cv2.filter2D(imagem, -1, high_boost)
resultado_prewitt_horizontal = cv2.filter2D(imagem, -1, prewitt_horizontal)
resultado_prewitt_vertical = cv2.filter2D(imagem, -1, prewitt_vertical)
resultado_sobel_horizontal = cv2.filter2D(imagem, -1, sobel_horizontal)
resultado_sobel_vertical = cv2.filter2D(imagem, -1, sobel_vertical)

cv2.imshow("original", imagem)
cv2.imshow("laplaciano", resultado_laplaciano)
cv2.imshow("unsharp", imagem - resultado_blur)
cv2.imshow("high boost", resultado_high_boost)
cv2.imshow("prewitt horizontal", resultado_prewitt_horizontal)
cv2.imshow("prewitt vertical", resultado_prewitt_vertical)
cv2.imshow("sobel horizontal", resultado_sobel_horizontal)
cv2.imshow("sobel vertical", resultado_sobel_vertical)

cv2.imwrite("laplaciano.bmp", resultado_laplaciano)
cv2.imwrite("unsharp.bmp", imagem - resultado_blur)
cv2.imwrite("highboost.bmp", resultado_high_boost)
cv2.imwrite("prewitthorizontal.bmp", resultado_prewitt_horizontal)
cv2.imwrite("prewittvertical.bmp", resultado_prewitt_vertical)
cv2.imwrite("sobelhorizontal.bmp", resultado_sobel_horizontal)
cv2.imwrite("sobelvertical.bmp", resultado_sobel_vertical)

