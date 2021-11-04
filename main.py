import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=2)
data = "https://github.com/i3012"
# i have given the path of my github

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="pink")
img.save("imene.png")