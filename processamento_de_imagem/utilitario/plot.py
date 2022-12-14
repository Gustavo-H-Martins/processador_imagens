from turtle import color
from matplotlib import image
import matplotlib.pyplot as plt
from pyparsing import alphanums

def plota_imagem(imagem):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plota_resultado(*args):
    numero_imagens = len(args)
    fig, axis = plt.subplots(nrows=1, ncols= numero_imagens, figsize=(12,4))
    nomes_lst = ['imagem {}'.format(i) for i in range(1, numero_imagens)]
    nomes_lst.append('Resultado')
    for ax, nome, imagem in zip(axis, nomes_lst, args):
        ax.set_title(nome)
        ax.imshow(imagem, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plota_histograma(imagem):
    fig, axis = plt.subplots(nrows=1, ncols= 3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} Histograma'.format(color.title()))
        ax.hist(imagem[:, :, index].ravel(), bins= 256, color= color, alpha = 0.8)
    fig.tight_layout()
    plt.show()
    