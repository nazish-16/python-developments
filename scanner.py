import qrcode

data = input("Enter a website link: ")
title = input("Enter the title you want for your QR code (including file extension, e.g., 'qrcode.png'): ")

qr = qrcode.QRCode()

qr.add_data(data)
qr.make()
image = qr.make_image()

image.save(title)
print(f"QR code saved as {title}")
