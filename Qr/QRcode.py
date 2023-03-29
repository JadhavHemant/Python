import qrcode
qr=qrcode.QRCode(
    version= 15,
    box_size=10,
    border=5
)

data=input("Enter Data : ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_color="white")
img.show("")


