import qrcode

# Data to encode
data = "https://github.com/aritrag"  # Replace with your actual GitHub URL

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("github_qr.png")
