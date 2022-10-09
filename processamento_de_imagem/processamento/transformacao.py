# Gustavo H Lopes
from skimage.transform import resize

def redimensionamento_imagem(imagem, proporcao):
    assert 0 <= proporcao <= 1, "Especifica uma  propoção válida entre 0 e 1."
    # height
    altura = round(imagem.shape[0] * proporcao)
    # width
    largura = round(imagem.shape[1] * proporcao)
    # Pega a imagem e redimensiona para caber no plot
    imagem_redimensionada = resize(imagem, (altura, largura), anti_aliasing=True)
    return imagem_redimensionada
