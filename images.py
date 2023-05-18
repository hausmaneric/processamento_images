from setuptools import setup
import cv2

setup(
    name='meu_pacote',
    version='0.1',
    description='Um pacote para processamento de imagens',
    author='Eric Hausman',
    author_email='eric.hausman.m@gmail.com',
    packages=['meu_pacote'],
    install_requires=[
        'numpy',
        'opencv-python',
    ],
)



def redimensionar_imagem(imagem, largura, altura):
    return cv2.resize(imagem, (largura, altura))

def aplicar_filtro_gaussiano(imagem, tamanho_kernel, desvio_padrao):
    return cv2.GaussianBlur(imagem, (tamanho_kernel, tamanho_kernel), desvio_padrao)
