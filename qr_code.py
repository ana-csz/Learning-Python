import qrcode
import os

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_salvamento = os.path.join(diretorio_atual, 'youtube_qr.png')

img.save(caminho_salvamento)