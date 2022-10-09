# Gustavo H. Lopes
import numpy as np
from skimage.color import rgbzgray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def encontra_diferenca(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Especificando duas imagens com a mesma dimensão."
    imagem1_cinza = rgbzgray(imagem1)
    imagem2_cinza = rgbzgray(imagem2)
    (score, diferenca_imagem) = structural_similarity(imagem1_cinza, imagem2_cinza, full=True)
    print(f"Similaridade das imagens:{score}")
    normalizando_dif_imagem = (diferenca_imagem.np.min(diferenca_imagem))/(np.max(diferenca_imagem)-np.min(diferenca_imagem))
    return normalizando_dif_imagem

    def transfer_histograma(imagem1, imagem2):
        combinacao_imagem = match_histograms(imagem1, imagem2, multichannel=True)
        return transfer_histograma