import numpy as np
import cv2

def uniao(imagem1: str, imagem2: str) -> np.array:
    array1 = cv2.imread(imagem1)
    array2 = cv2.imread(imagem2)

    retorno = []
    for i in range(len(array1)):
        linha = []
        for j in range(len(array1[0])):
            linha.append(max(array1[i][j][0], array2[i][j][0]))
        retorno.append(linha)
    return np.array(retorno)

def intersecao(imagem1: str, imagem2: str) -> np.array:
    array1 = cv2.imread(imagem1)
    array2 = cv2.imread(imagem2)

    retorno = []
    for i in range(len(array1)):
        linha = []
        for j in range(len(array1[0])):
            linha.append(min(array1[i][j][0], array2[i][j][0]))
        retorno.append(linha)
    return np.array(retorno)

def diferenca(imagem1: str, imagem2: str) -> np.array:
    array1 = cv2.imread(imagem1)
    array2 = cv2.imread(imagem2)

    retorno = []
    for i in range(len(array1)):
        linha = []
        for j in range(len(array1[0])):
            linha.append(max(array1[i][j][0] - array2[i][j][0], 0))
        retorno.append(linha)
    return np.array(retorno)

cv2.imshow("uniao1e2", uniao("imagem1.bmp", "imagem2.bmp"))
cv2.imshow("intersecao1e3", intersecao("imagem1.bmp", "imagem3.bmp"))
cv2.imshow("diferenca2e3", diferenca("imagem2.bmp", "imagem3.bmp"))

cv2.imwrite("uniao1e2.bmp", uniao("imagem1.bmp", "imagem2.bmp"))
cv2.imwrite("intersecao1e3.bmp", intersecao("imagem1.bmp", "imagem3.bmp"))
cv2.imwrite("diferenca2e3.bmp", diferenca("imagem2.bmp", "imagem3.bmp"))
