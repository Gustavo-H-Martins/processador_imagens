from skimage.io import imread, imsave

def le_imagem(caminho, is_gray = False):
    imagem = imread(caminho, as_gray = is_gray)
    return imagem

def salva_imagem(imagem, caminho):
    imsave(caminho, imagem)
