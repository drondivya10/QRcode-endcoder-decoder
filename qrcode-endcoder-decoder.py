import pyqrcode
import png
link = "https://www.instagram.com/dron.divya10__/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)


from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('instagram.png'))
print(decocdeQR[0].data.decode('ascii'))