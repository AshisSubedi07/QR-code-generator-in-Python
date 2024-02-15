import qrcode
from PIL import Image

#Creating varable to design QR code
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=18, border=4,)
qr.add_data("https://github.com/AshisSubedi07")
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='pink')
img.save('GW-ASHIS_GTH.png')