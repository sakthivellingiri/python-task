import qrcode

data = input("Enter your url link: ").strip()
file_name = input("Enter your file name: ").strip() ##name should be in amazon.jpg or amazon.png
qr = qrcode.QRCode(box_size=40, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(file_name)
print(f"Image save successfully in name {file_name}")