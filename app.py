from PIL import Image
from pyzbar.pyzbar import decode

imagem = Image.open("wafferbar.png")
imagem = imagem.convert("L")

codigos_barras = decode(imagem)

if len(codigos_barras) > 0:
    codigo = codigos_barras[0].data.decode("utf-8")
    print("Código de barras identificado:", codigo)
else:
    print("Nenhum código de barras identificado.")