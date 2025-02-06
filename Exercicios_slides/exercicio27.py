#Dado um número inteiro, seu valor invertido é ele lido de trás
#para frente

def invertido(x):
    invertido = 0
    while x > 0:
        invertido = invertido*10 + x%10
        x = x//10
    return invertido

